# online-library-shop-monitoring
An online library is interested in monitoring its transactions.

This project consists in a simple backend library shop, a kafka ecosystem with debezium plugins consuming in realtime
the data produced by the backend. Then the data is collected by pinot and enriched in realtime by presto queries. 

# How to start the project
- Inside the root folder text: ```docker-compose -f ./docker-compose-application.yaml up```
- To restart the infrastructure: ```docker compose -f ./docker-compose-application.yaml up --build```
- ```docker compose -f docker-compose-application.yaml down --remove-orphans```

# How to run the simple shop app
- First, Enter or create a virtualenv. Example: ```python -m venv venv``` and ```source ./venv/bin/activate```
- Then, install all the dependencies using: ```pip install -r requirements.txt```
- Inside the shop app container, enter into the terminal and text: ```python manage.py makemigrations``` ```python manage.py migrate```


## Overview
APP >> KAFKA >> PINOT >> PRESTO