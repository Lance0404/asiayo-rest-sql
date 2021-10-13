# asiayo-rest-sql

### 


### Start service with docker
* `docker-compose build` to build docker image `asiayo_web` locally
* (Optional) or `docker-compose up -d --build` to rebuild image before up
* `docker-compose up -d` to init the services accordingly
* `docker-compose logs -f --tail=10` to check the services are healthy    

### db migration
* (Optional) prefix the command with `docker-compose exec web ` if you are doing it from the container
* `alembic init -t async migrations` to generate alembic configs
* `alembic revision --autogenerate -m "init"` to generate the first migration file
* `alembic upgrade head` to apply the migration
* `alembic downgrade -1` to go back one revision

* **Beware** that the `sqlalchemy.url` within the `alembic.ini` may differ depending on how you start the app, with or without docker.


#### Debug
* `sudo chown lance -R *` to have permission to modify files generated from within container
* there are some issues during the alembic ops related to VSCode, which can fixed by restarting the IDE.

### Misc
* my notes during development, [README_dev.md](doc/README_dev.md)