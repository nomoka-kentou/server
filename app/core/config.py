from pydantic import BaseModel, MySQLDsn


class Settings(BaseModel):
    # todo: env化したい
    username = 'user'
    password = 'password'
    hostname = 'host'
    port = 12345
    databasename = 'name'

    DATABASE_URL: MySQLDsn = f'mysql+pymysql://{username}:{
        password}@{hostname}:{port}/{databasename}?charset=utf8'


settings = Settings()
