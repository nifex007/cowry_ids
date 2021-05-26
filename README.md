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
virtuanlenv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
python manage.py migrate
```