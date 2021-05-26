# cowry_ids

### SET UP APP WITH DOCKER

This assumes you have docker installed. <br>Run these commands below in your terminal in the directory where `Dockerfile` and `docker-compose.yml` can be found.

```bash
cd cowry_ids
docker-compose up --build
````
Go to  `http://0.0.0.0:8000/api/identifiers`


### SET UP APP WITH VIRTUALENV

This assumes you have virtualenv installed 

```bash
cd cowry_ids
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Go to `http://127.0.0.1:8000/api/identifiers`

## Tests 
### Docker
`sudo docker-compose run web python manage.py test`

### Virtual environment
`python manage.py test`