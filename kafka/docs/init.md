# Postgres Configuration to allow debezium to work

```sql
CREATE ROLE replication_role WITH REPLICATION LOGIN;
GRANT replication_role TO admin;
```
Or, if you want to have all privileges
```sql
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO admin;
```