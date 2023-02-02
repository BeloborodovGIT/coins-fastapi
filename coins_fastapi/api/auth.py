from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import models
from ..services.auth import AuthService, get_current_user
from ..database import get_session

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)


@router.post(
    '/sign-up/',
    response_model=models.Token,
    status_code=status.HTTP_201_CREATED,
)
def sign_up(
    user_data: models.UserCreate,
    session: Session = Depends(get_session)
):  
    return AuthService(session).register_new_user(user_data)


@router.post(
    '/sign-in/',
    response_model=models.Token,
)
def sign_in(
    auth_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session)
):
    return AuthService(session).authenticate_user(
        auth_data.username,
        auth_data.password,
    )


@router.get(
    '/user/',
    response_model=models.User,
)
def get_user(user: models.User = Depends(get_current_user)):
    return user