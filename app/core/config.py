import os
import secrets
from pathlib import Path

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):

    HOST: str = '0.0.0.0'
    PORT: int = 3000
    # 是否开发模式
    DEV: bool = os.environ.get('DEV', False)

    SUPERUSER: str = 'admin'
    SUPERUSER_PASSWORD: str = 'admin123'
    API_V1_STR: str = '/api/v1'
    TZ: str = 'Asia/Shanghai'

    TABLE_PREFIX = 't_'
    # 密钥
    SECRET_KEY: str = secrets.token_urlsafe(32)

    # token默认过期时间：7天
    ACCESS_TOKEN_EXPIRE_MINUTES = 7 * 24 * 60

    @property
    def ROOT_PATH(self):
        return Path(__file__).parents[2]

    @property
    def CONFIG_PATH(self):
        return self.ROOT_PATH / 'config'

    @property
    def TEMP_PATH(self):
        return self.CONFIG_PATH / 'temp'

    @property
    def MYSQL_USERNAME(self):
        return os.environ.get('MYSQL_USERNAME', 'root')

    @property
    def MYSQL_PASSWORD(self):
        return os.environ.get('MYSQL_PASSWORD', 'root')

    @property
    def MYSQL_HOST(self):
        return os.environ.get('MYSQL_HOST', '127.0.0.1')

    @property
    def MYSQL_PORT(self):
        return os.environ.get('MYSQL_PORT', '3306')

    @property
    def MYSQL_DATABASE(self):
        return os.environ.get('MYSQL_DATABASE', 'my_gpt')


settings = Settings()
