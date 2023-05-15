# online-library-shop-monitoring
An online library is interested in monitoring its transactions.

This project consists in a simple backend library shop, a kafka ecosystem with debezium plugins consuming in realtime
the data produced by the backend. Then the data is collected by pinot and enriched in realtime by presto queries. 

# How to run
- Inside the root folder text: ```docker-compose -f ./docker-compose-application.yaml up```
- To restart the infrastructure: ```docker compose -f ./docker-compose-application.yaml up --force-recreate```

# Creating tables
- Inside the shop app container, enter into the terminal and text: ```python manage.py makemigrations``` ```python manage.py migrate```

