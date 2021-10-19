# asiayo-rest-sql

* [requirement](doc/2021-10_Backend-Pre-test.pdf)
* [answer for sql quiz](doc/answers.sql)

### Start RESTful application 
1. `cd project`
1. `poetry install`
1. `poetry shell`
1. `uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000` to start the app locally 
1. OpenAPI UI: `http://localhost:8000/docs`

### Test
* I only wrote integration tests related to the requirement
* test cases [here](project/tests/test_currency.py)
* How to run:
    1. `cd project`
    1. `poetry install` (omit if done already)    
    1. `poetry shell` (omit if done already)
    1. `pytest`

---
## Additional feature
* Below are additional features developed for my own interest, free for trial. 
1. Support Create(POST) and Read(GET) operations related to the sql quiz with a actual Postgresql database
1. (Undone) Yet to secceed with using sqlalchemy's async session to do an async group_by sql op

### Start service with docker
* at the project root path, e.g. ./asiayo-rest-sql
* (Optional) `docker-compose build` to build docker image `asiayo_web` locally
* (Optional) or `docker-compose up -d --build` to rebuild image then up
* `docker-compose up -d` to init the services accordingly
* `docker-compose logs -f --tail=10 web` to check the services are healthy    
* OpenAPI UI: `http://localhost:8000/docs`


### Database initialization
* I use alembic to initialize the psql db 
* `docker-compose exec web alembic upgrade head` to apply the migration
* **Beware** that the `sqlalchemy.url` within the `alembic.ini` may differ depending on how you start the app, with or without docker.
* should be `sqlalchemy.url = postgresql+asyncpg://postgres:postgres@db:5432/foo` if running commands from the docker

---
### Misc
* my notes during development, [README_dev.md](doc/README_dev.md)