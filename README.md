**GitHub Activity Pipeline** is a learning project for analyzing public GitHub repository activity using JSON data from GH Archive.

The planned pipeline will store raw data in Amazon S3, process it with Python, and load it into PostgreSQL as one fact table and two dimension tables. Apache Airflow will orchestrate the workflow, with Docker providing the runtime environment on Linux.

The project is under development, with source code and change history managed in Git.
