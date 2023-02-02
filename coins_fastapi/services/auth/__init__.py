from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.hash import bcrypt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from ... import models

from ... import database

from ...settings import config


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/sign-in/')


def get_current_user(token: str = Depends(oauth2_scheme)) -> models.User:
    return AuthService.verify_token(token)

def check_admin(user: models.User = Depends(get_current_user)) -> models.User:
    if user.role == database.RoleENUM.ADMIN:
        return user
    else:
        raise HTTPException(status.HTTP_403_FORBIDDEN)


class AuthService:
    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.verify(plain_password, hashed_password)

    @classmethod
    def hash_password(cls, password: str) -> str:
        return bcrypt.hash(password)

    @classmethod
    def verify_token(cls, token: str) -> models.User:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )
        try:
            payload = jwt.decode(
                token,
                config.jwt_secret,
                algorithms=[config.jwt_algorithm],
            )
        except JWTError:
            raise exception from None

        user_data = payload.get('user')

        try:
            user = models.User.parse_obj(user_data)
        except ValidationError:
            raise exception from None

        return user

    @classmethod
    def create_token(cls, user: models.UserCreate) -> models.Token:
        user_data = models.User.from_orm(user)
        now = datetime.utcnow()
        payload = {
            'iat': now,
            'nbf': now,
            'exp': now + timedelta(seconds=config.jwt_expires_sec),
            'sub': str(user_data.id),
            'user': user_data.dict(),
        }
        token = jwt.encode(
            payload,
            config.jwt_secret,
            algorithm=config.jwt_algorithm,
        )
        return models.Token(access_token=token)

    def __init__(self, session: Session = Depends(database.get_session)):
        self.session = session

    def register_new_user(
        self,
        user_data: models.UserCreate,
    ) -> models.Token:
        user = database.Users(
            login=user_data.login,
            name=user_data.name,
            password_hash=self.hash_password(user_data.password),
        )
        self.session.add(user)
        self.session.commit()

        return self.create_token(user)

    def authenticate_user(
        self,
        name: str,
        password: str,
    ) -> models.Token:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'},
        )

        user: database.Users = (
            self.session
            .query(database.Users)
            .filter(database.Users.name == name)
            .first()
        )

        if not user:
            raise exception

        if not self.verify_password(password, user.password_hash):
            raise exception

        return self.create_token(user)