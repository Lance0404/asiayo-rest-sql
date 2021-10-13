

### TODO
1. study how to setup relation with SQLModel
1. async group by sql op
1. async pytest


### Dev locally
* create a file `project/app/.env`
* append `DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/foo` into it
* so `load_dotenv` in `project/app/db.py` would be able to override it.
* as for docker, it's defined in docker-compose.yml

### Docker
* `docker-compose exec web bash` to have a peek at the container
* `docker-compose down -v` to bring down the existing containers and volumes
* `docker-compose up -d db` to only start the db container
* `chown lance:lance -R ./` to fix permission on files generated from within the contained

### Alembic
* (Optional) prefix the command with `docker-compose exec web ` if you are doing it from the container
* `alembic init -t async migrations` to generate alembic configs
* `alembic revision --autogenerate -m "init"` to generate the first migration file
* `alembic upgrade head` to apply the migration
* `alembic downgrade -1` to go back one revision
* **Beware** that the `sqlalchemy.url` within the `project/alembic.ini` may differ depending on how you start the app, with or without docker.
* should be `sqlalchemy.url = postgresql+asyncpg://postgres:postgres@localhost:5432/foo` if running commands locally

### Reference
1. [fastapi-sqlmodel](https://testdriven.io/blog/fastapi-sqlmodel/)
2. [undo last migration](https://stackoverflow.com/a/48242325/8937834)
3. [asyncio orm avoid lazyloads](https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html#asyncio-orm-avoid-lazyloads)
4. [httpx](https://www.python-httpx.org/)
5. [Developing and Testing an Asynchronous API with FastAPI and Pytest](https://testdriven.io/blog/fastapi-crud/#test-setup)
