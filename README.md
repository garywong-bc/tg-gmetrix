## to reset DB files

```bash
rm -rf ./docker/mysql/data/* && rm -rf ./docker/mysql/data/.*
```

## To log into DB

❯ docker-compose exec db /bin/bash

Owner

> mysql -u ${MYSQL_USER} -D ${MYSQL_DATABASE} -p${MYSQL_PASSWORD}

Root

> mysql -u root -D ${MYSQL_DATABASE} -p${MYSQL_ROOT_PASSWORD}

## To log into Python container

❯ docker-compose exec python /bin/bash

## Python rqmts

```bash
pip3 install mysql.connector
pip3 install haralyzer-api
```

> pip3 freeze > requirements.txt

> pip3 install -r requirements.txt

WHEN READY, follow
https://www.docker.com/blog/containerized-python-development-part-1/
to bake my python image
