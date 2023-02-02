from pydantic import BaseSettings

class Config(BaseSettings):
    
    #конфиг запуска сервера
    server_host: str = '127.0.0.1'
    server_port: int = 8080
    
    #конфиг авторизации
    jwt_secret: str
    jwt_algorithm: str = 'HS256'
    jwt_expires_sec: int = 600

    #конфиг подключения к бд
    db_host: str = '127.0.0.1'
    db_port: str = 5432
    db_login: str = 'postgres'
    db_password: str = 'admin'
    db_name: str = 'coins'

    @property
    def db_address(self):
        return f'{self.db_host}:{self.db_port}'

    @property
    def db_connetion_string(self):
        return f'postgresql+psycopg2://{self.db_login}:{self.db_password}@{self.db_address}/{self.db_name}'


config = Config(
    _env_file='.env',
    _env_file_encoding='utf-8'
)