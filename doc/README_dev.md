

### TODO
1. study how to setup relation with SQLModel

### Docker
* `docker-compose exec web bash` to have a peek at the container
* `docker-compose down -v` to bring down the existing containers and volumes
* `docker-compose up -d db` to only up db as container

### Reference
1. [fastapi-sqlmodel](https://testdriven.io/blog/fastapi-sqlmodel/)
2. [undo last migration](https://stackoverflow.com/a/48242325/8937834)
3. [asyncio orm avoid lazyloads](https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html#asyncio-orm-avoid-lazyloads)
4. [httpx](https://www.python-httpx.org/)
5. [Developing and Testing an Asynchronous API with FastAPI and Pytest](https://testdriven.io/blog/fastapi-crud/#test-setup)
