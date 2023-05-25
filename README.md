# online-library-shop-monitoring
An online library is interested in monitoring its transactions.

This project consists in a simple backend library shop, a kafka ecosystem with debezium plugins consuming in realtime
the data produced by the backend. Then the data is collected by pinot and enriched in realtime by presto queries. 

# How to start the project kafka app
- To start the kafka infrastructure: ```docker compose -f docker-compose-kafka.yaml up -d```
- To stop: ```docker compose -f docker-compose-application.yaml down --remove-orphans```

# How to run the simple shop app
- To start the shop app: ```docker compose -f ./docker-compose-application.yaml up --build -d```
- To stop: ```docker compose -f docker-compose-application.yaml down --remove-orphans```
- To run locally for development purposes:
  - Enter or create a virtualenv. Example: ```python -m venv venv``` and ```source ./venv/bin/activate```
  - Then, install all the dependencies using: ```pip install -r requirements.txt```
  - And, text ```python manage.py runserver```

# Config Db
- Following: https://access.redhat.com/documentation/pt-br/red_hat_integration/2019-12/html/change_data_capture_user_guide/debezium-connector-for-postgresql#configuring_the_replication_slot
- We need to configure the postgres to run in replication mode to be able to capture the changes in our data
- Then we clone the sample config file and change these configs:
  - command to clone the config```docker run -i --rm postgres:13 cat /usr/share/postgresql/postgresql.conf.sample > ./postgres/custom-config.conf```
  - change the config file setting:: wal_level=logical  max_wal_senders=1  max_replication_slots=2
  - create custom hba_file to give replication permission to the user 
  - How to access psql: Go to db terminal and type: "psql -U admin library"
  - To see the current config type: SHOW ALL;
  - To see where is the config_file type: SHOW config_file;
  - To see where is the hba_file type: SHOW hba_file;
  - To create the a role the allows the user to work with replication we type:
  - ```create role replication REPLICATION LOGIN;```
  - ```grant replication to admin```
  - When everything is up and running we need to add our connector into the Kafka Connect API. For a while we are using this config:
    ```json
      {
          "name": "library",  
          "config": {  
                  "connector.class" : "io.debezium.connector.postgresql.PostgresConnector",  
                  "database.hostname" : "db",  
                  "database.port" : "5432",  
                  "database.user" : "admin",  
                  "database.password" : "pass",   
                  "database.dbname" : "library",  
                  "tasks.max" : "1",
                  "topic.prefix" : "library-shop",
                  "plugin.name": "pgoutput" // THE DEFAULT IS decoderbufs BUT WE ALL USING pgoutput
          }
      }
    ```
    - Send this payload to POST http://localhost:8083/connectors everything should work well
    - The link where you find all the possible configurations (https://debezium.io/documentation/reference/2.3/connectors/postgresql.html#postgresql-property-plugin-name)

## Overview
APP >> KAFKA >> PINOT >> PRESTO
```docker compose -f docker-compose-application.yaml -f docker-compose-kafka.yaml -f docker-compose-pinot.yaml up```

### Connect
kafka-topics --bootstrap-server kafka:29092 --list
