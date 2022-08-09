
from functools import lru_cache

from pydantic import BaseSettings, conint


class Config(BaseSettings):
    DB_ECHO_LOG: bool = True
    SHOW_DOCS: bool = True
    DIR_CODE: str = "app"

    HOST: str = "0.0.0.0"
    PORT: conint(ge=5000, lt=9999) = 5000

    UVICORN_WORKERS_COUNT: conint(ge=1, lt=32) = 2
    UVICORN_LOG_LEVEL: str = "debug"
    UVICORN_RELOAD: bool = True

    DB_MIN_POOL_SIZE: int = 1
    DB_MAX_POOL_SIZE: int = 300

    PG_MASTER_USER: str = "mydb_user"
    PG_MASTER_DB_NAME: str = "mydb"
    PG_MASTER_PASSWORD: str = "mydb_secret"
    PG_MASTER_HOST: str = "db-jail"
    PG_MASTER_PORT: int = 5432
    PGB_MASTER_PORT: int = 6432
    PGB_MASTER_HOST: str = "pgbouncer-jail"



    @property
    def db_master_uri(self) -> str:
        return (
            f"postgresql+asyncpg://{self.PG_MASTER_USER}:"
            f"{self.PG_MASTER_PASSWORD}@{self.PGB_MASTER_HOST}:{self.PGB_MASTER_PORT}/"
            f"{self.PG_MASTER_DB_NAME}?prepared_statement_cache_size=0&statement_cache_size=0"
        )

    @property
    def db_master_alembic_uri(self) -> str:
        return (
            f"postgresql+asyncpg://{self.PG_MASTER_USER}:"
            f"{self.PG_MASTER_PASSWORD}@{self.PGB_MASTER_HOST}:{self.PGB_MASTER_PORT}/"
            f"{self.PG_MASTER_DB_NAME}?prepared_statement_cache_size=0&statement_cache_size=0"
        )


@lru_cache
def get_settings() -> Config:
    return Config()
