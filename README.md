# online-library-shop-monitoring
An online library is interested in monitoring its transactions.

# How to run
- Inside the root folder text: ```docker-compose -f ./docker-compose-base.yaml up```
- To restart the infrastructure: ```docker compose -f ./docker-compose-base.yaml up --force-recreate```

# Creating tables
- Inside the shop app container, enter into the terminal and text: ```python manage.py makemigrations``` ```python manage.py migrate```
