# orm-and-me
Test orm

do : docker-compose exec app-jail sh -c 'alembic upgrade head' 

sqla+fastapi : https://github.com/grillazz/fastapi-sqlalchemy-asyncpg
sqla+pgbouncer-transaction : https://github.com/sqlalchemy/sqlalchemy/issues/6467#issuecomment-1187595547