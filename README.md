#  Data Engineering Capstone Project

![IBM Data Engineering](https://img.shields.io/badge/IBM-Data%20Engineering-blue)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![MySQL](https://img.shields.io/badge/MySQL-OLTP-orange)
![MongoDB](https://img.shields.io/badge/MongoDB-NoSQL-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Data%20Warehouse-blue)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-ETL-red)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-Big%20Data-orange)
![PySpark](https://img.shields.io/badge/PySpark-ML-orange)
![Cognos](https://img.shields.io/badge/IBM%20Cognos-Analytics-purple)

## 📌 Project Overview

This project is my **Data Engineering Capstone Project** from the **IBM Data Engineering Professional Certificate** on Coursera.

The project simulates the role of a **Junior Data Engineer** working for an e-commerce organization. The objective is to design and implement a data analytics platform that covers the major stages of a modern data engineering lifecycle:

* Relational OLTP database
* NoSQL database
* Data warehouse
* SQL analytics and reporting
* Business intelligence dashboards
* ETL processes
* Automated data pipelines
* Big data processing with Apache Spark
* Machine learning model loading and prediction

The official IBM/Coursera capstone describes the project as an end-to-end exercise involving MySQL, MongoDB, PostgreSQL/Db2, Cognos Analytics, ETL pipelines, Apache Airflow, and Apache Spark.

---

# 🏗️ Data Engineering Architecture

The overall project follows this general architecture:

```text
                         E-COMMERCE PLATFORM
                                │
                ┌───────────────┴───────────────┐
                │                               │
                ▼                               ▼
        ┌───────────────┐                ┌───────────────┐
        │     MySQL     │                │    MongoDB    │
        │     OLTP      │                │    NoSQL      │
        │               │                │ Product       │
        │ Sales /       │                │ Catalog       │
        │ Transactions  │                │ Data          │
        └───────┬───────┘                └───────────────┘
                │
                │ ETL
                ▼
        ┌───────────────────┐
        │    PostgreSQL     │
        │   Data Warehouse  │
        │                   │
        │ Staging +         │
        │ Production Data   │
        └─────────┬─────────┘
                  │
          ┌───────┴────────┐
          │                │
          ▼                ▼
 ┌────────────────┐  ┌─────────────────┐
 │ SQL Analytics  │  │ Cognos Analytics│
 │ Reports        │  │ Dashboard       │
 └────────────────┘  └─────────────────┘

                  ETL / Automation
                       │
                       ▼
              ┌─────────────────┐
              │ Apache Airflow  │
              │ DAG Pipelines   │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Apache Spark    │
              │ / PySpark       │
              │ Big Data + ML   │
              └─────────────────┘
```

---

# 🧰 Technologies Used

| Area                      | Technology                     |
| ------------------------- | ------------------------------ |
| Programming               | Python                         |
| Shell                     | Linux / Bash                   |
| OLTP Database             | MySQL                          |
| NoSQL Database            | MongoDB                        |
| Staging Data Warehouse    | PostgreSQL                     |
| Production Data Warehouse | IBM Db2                        |
| Data Visualization        | IBM Cognos Analytics           |
| ETL                       | Python                         |
| Workflow Orchestration    | Apache Airflow                 |
| Big Data Processing       | Apache Spark                   |
| Spark API                 | PySpark                        |
| Machine Learning          | Spark ML                       |
| Version Control           | Git / GitHub                   |
| SQL                       | MySQL / PostgreSQL / Db2       |
| Development Environment   | IBM Skills Network / Cloud IDE |

---

# 📚 Project Modules

## Module 1 — Data Platform Architecture and OLTP Database

### Objective

Design and implement an **OLTP database** for an e-commerce application using MySQL.

### Main technologies

* MySQL
* SQL
* Linux
* Python
* Shell scripting

### Work completed

The OLTP layer was designed to handle transactional e-commerce data.

The database contains transactional information such as sales and inventory-related data.

Typical OLTP operations include:

```sql
SELECT
INSERT
UPDATE
DELETE
```

The database was also used as the source system for later ETL processing.

### Key concepts learned

* OLTP database architecture
* Relational database design
* Tables and relationships
* Primary keys
* SQL queries
* Database administration
* Transactional data processing

---

# Module 2 — Querying Data in NoSQL Databases

## Objective

Use **MongoDB** as a NoSQL database for e-commerce catalog information.

MongoDB is appropriate for product catalog data because documents can represent product information without requiring the same rigid relational structure used by an OLTP database.

### Main technologies

* MongoDB
* NoSQL
* MongoDB queries

### Example operations

```javascript
db.products.find()
```

Filtering documents:

```javascript
db.products.find({
    category: "Laptop"
})
```

Counting documents:

```javascript
db.products.countDocuments()
```

### Key concepts learned

* NoSQL databases
* MongoDB collections
* Documents
* JSON/BSON-style data
* MongoDB queries
* Filtering and aggregation

---

# Module 3 — Build a Data Warehouse

## Objective

Design and populate a **data warehouse** for analytical workloads.

The project uses PostgreSQL as a staging data warehouse and also works with IBM Db2 as the production warehouse environment.

### Main technologies

* PostgreSQL
* IBM Db2
* SQL

### Data warehouse workflow

```text
OLTP / Source Data
       │
       ▼
   PostgreSQL
    Staging
       │
       ▼
 Production
 Data Warehouse
       │
       ▼
   Analytics
```

### PostgreSQL work

The PostgreSQL environment was used to load and query warehouse data.

Unlike MySQL, PostgreSQL does not use:

```sql
USE database;
```

Instead, database selection is performed using:

```text
\c database_name
```

Other useful PostgreSQL commands include:

```text
\l
```

to list databases, and:

```text
\dt
```

to list tables.

### Analytical SQL

The warehouse was used for analytical queries such as:

* Aggregation
* GROUP BY
* CUBE
* ROLLUP
* Business reporting
* Sales analysis

Example:

```sql
SELECT
    product,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY product;
```

---

# Module 4 — Data Analytics

## Objective

Use warehouse data to create business intelligence reports and dashboards.

### Main technology

**IBM Cognos Analytics**

The project included creating visualizations to help analyze business performance.

### Dashboard

The analytics work included a dashboard containing multiple visualizations.

Examples included:

### Panel 1 — Recalls by Car Model

A column chart showing the number of recalls for each car model.

```text
Car Model → Number of Recalls
```

### Panel 2 — Customer Sentiment

A visualization comparing:

* Positive
* Neutral
* Negative

customer reviews.

### Panel 3 — Monthly Sales and Profit

A combination visualization showing:

* Cars sold per month
* Profit per month

This allows sales volume and profitability to be analyzed together.

### Panel 4 — Recalls by Model and System

A heat map showing recalls according to:

* Car model
* Affected system

### Key concepts learned

* Business intelligence
* Data visualization
* KPI reporting
* Dashboard design
* Cognos data modules
* Analytical storytelling

---

# Module 5 — ETL & Data Pipelines

## Objective

Build an ETL process that moves incremental data from a production/source database into a data warehouse.

The module also extends the ETL process using **Apache Airflow** for workflow orchestration. The official course specifically describes extracting daily incremental records, transforming them, loading them into a warehouse, and then automating workflows with Airflow DAGs.

---

## 5.1 Python ETL Pipeline

The Python ETL process consists of three main stages:

```text
Extract → Transform → Load
```

### Extract

The pipeline determines the latest processed `rowid` and retrieves new records.

Example logic:

```python
SELECT MAX(rowid)
FROM production_table;
```

Then new records are retrieved from the source database.

### Transform

The extracted records are prepared for insertion into the destination warehouse.

### Load

The transformed records are inserted into the production data warehouse.

---

## ETL Result

The ETL pipeline successfully processed:

```text
Last row id on production datawarehouse = 0
New rows on staging datawarehouse = 13836
New rows inserted into production datawarehouse = 13836
```

This demonstrated an incremental ETL workflow rather than reloading the entire dataset.

---

# 5.2 Apache Airflow Pipeline

The second part of the module uses **Apache Airflow** to automate a web server log processing pipeline.

### DAG

The DAG is named:

```text
process_web_log
```

### Pipeline

```text
extract_data
      │
      ▼
transform_data
      │
      ▼
load_data
```

The Airflow dependency is:

```python
extract_data >> transform_data >> load_data
```

---

## Task 1 — Extract

The `extract_data` task extracts IP addresses from the web server log.

```bash
awk '{print $1}' accesslog.txt
```

The extracted data is saved as:

```text
extracted_data.txt
```

---

## Task 2 — Transform

The `transform_data` task removes the specified IP address:

```text
198.46.149.143
```

using:

```bash
grep -v '198.46.149.143'
```

The result is saved as:

```text
transformed_data.txt
```

The transformation was verified by checking that the specified IP address no longer appeared in the output.

---

## Task 3 — Load

The final task archives the transformed data:

```bash
tar -cf weblog.tar transformed_data.txt
```

The resulting archive is:

```text
weblog.tar
```

---

## Airflow DAG Structure

```text
                    process_web_log
                          │
                          ▼
                   ┌─────────────┐
                   │ extract_data│
                   └──────┬──────┘
                          │
                          ▼
                  ┌────────────────┐
                  │ transform_data │
                  └───────┬────────┘
                          │
                          ▼
                    ┌───────────┐
                    │ load_data │
                    └───────────┘
```

### Airflow concepts learned

* DAGs
* Tasks
* BashOperator
* Task dependencies
* Scheduling
* DAG triggering
* Task testing
* Monitoring
* Workflow orchestration

---

# Module 6 — Big Data Analytics with Spark

## Objective

Use **Apache Spark / PySpark** to analyze e-commerce web server search data and perform machine learning predictions.

The course describes this module as analyzing web-server search terms and loading a pretrained sales forecasting model to predict a future year's sales.

---

## 6.1 Spark DataFrame

The search-term dataset was loaded from:

```text
searchterms.csv
```

A Spark session was created using:

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Analyze Search Terms") \
    .getOrCreate()
```

The CSV was loaded into a Spark DataFrame:

```python
df = spark.read.csv(
    "searchterms.csv",
    header=True,
    inferSchema=True
)
```

---

## 6.2 Data Exploration

The DataFrame was analyzed using:

```python
df.count()
```

and:

```python
len(df.columns)
```

The first five rows were displayed with:

```python
df.show(5)
```

The schema was inspected with:

```python
df.printSchema()
```

---

## 6.3 Search Term Analysis

The number of searches for:

```text
gaming laptop
```

was calculated using:

```python
df.filter(
    df.searchterm == "gaming laptop"
).count()
```

A temporary SQL view was also created:

```python
df.createOrReplaceTempView("searchterms")
```

The most frequently searched terms were obtained using:

```sql
SELECT
    searchterm,
    COUNT(*) AS frequency
FROM searchterms
GROUP BY searchterm
ORDER BY frequency DESC
LIMIT 5;
```

---

# 6.4 Spark ML Model

A pretrained sales forecasting model was downloaded and extracted.

The model was loaded using Spark ML:

```python
from pyspark.ml.regression import LinearRegressionModel

model = LinearRegressionModel.load("MODEL_DIRECTORY")
```

The project also included practice with saving and loading Spark ML models.

Example:

```python
lrModel.write().overwrite().save(
    "babyweightprediction.model"
)
```

Loading the model:

```python
model = LinearRegressionModel.load(
    "babyweightprediction.model"
)
```

A prediction could then be generated for an infant with a height of 50 cm:

```python
predict(50)
```

---

# 🔄 End-to-End Data Engineering Workflow

The project demonstrates the following lifecycle:

```text
                  SOURCE SYSTEMS
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
       MySQL                    MongoDB
       OLTP                     NoSQL
          │                         │
          └────────────┬────────────┘
                       │
                       ▼
                    ETL
                       │
                       ▼
                 PostgreSQL
                  Staging
                       │
                       ▼
                Data Warehouse
                       │
              ┌────────┴────────┐
              │                 │
              ▼                 ▼
          SQL Reports       Cognos
                              Dashboard
              
              ─────────────────────

                 Web Server Logs
                       │
                       ▼
                 Apache Airflow
                       │
              ┌────────┴────────┐
              ▼                 ▼
          Extract            Transform
              │                 │
              └────────┬────────┘
                       ▼
                     Load
                       │
                       ▼
                  weblog.tar

              ─────────────────────

                  Search Data
                       │
                       ▼
                 Apache Spark
                       │
                       ▼
                 PySpark / SQL
                       │
                       ▼
                Spark ML Model
                       │
                       ▼
                 Sales Forecast
```

---

# 🧠 Key Skills Demonstrated

Through this capstone, I practiced the complete data engineering lifecycle.

### Databases

* MySQL
* PostgreSQL
* IBM Db2
* MongoDB
* Relational database design
* NoSQL data modeling

### Programming

* Python
* SQL
* Bash
* PySpark

### Data Engineering

* ETL
* Data extraction
* Data transformation
* Data loading
* Incremental data processing
* Data warehouse development
* Data pipelines

### Workflow Automation

* Apache Airflow
* DAG creation
* Task dependencies
* Scheduling
* Pipeline monitoring

### Big Data

* Apache Spark
* Spark DataFrames
* Spark SQL
* PySpark
* Spark ML

### Analytics

* SQL analytics
* Aggregation
* Business reporting
* IBM Cognos Analytics
* Dashboard development
* Data visualization

---

# 📂 Suggested Repository Structure

```text
IBM-Data-Engineering-Capstone/
│
├── README.md
│
├── module-1-oltp/
│   ├── sql/
│   ├── screenshots/
│   └── README.md
│
├── module-2-mongodb/
│   ├── queries/
│   ├── screenshots/
│   └── README.md
│
├── module-3-data-warehouse/
│   ├── sql/
│   ├── postgresql/
│   ├── db2/
│   ├── screenshots/
│   └── README.md
│
├── module-4-data-analytics/
│   ├── cognos/
│   ├── screenshots/
│   └── README.md
│
├── module-5-etl-airflow/
│   ├── automation.py
│   ├── process_web_log.py
│   ├── screenshots/
│   └── README.md
│
├── module-6-spark/
│   ├── notebooks/
│   ├── pyspark/
│   ├── screenshots/
│   └── README.md
│
└── screenshots/
```

---

# 📊 Project Outcomes

This capstone provided practical experience with an end-to-end data engineering architecture rather than focusing on only one technology.

The major outcomes were:

* Designed an e-commerce OLTP data platform.
* Queried e-commerce catalog information using MongoDB.
* Built and queried a data warehouse.
* Performed analytical SQL queries.
* Created business intelligence visualizations using Cognos Analytics.
* Developed a Python-based incremental ETL process.
* Automated web-log processing using Apache Airflow.
* Created an Airflow DAG with dependent extraction, transformation, and loading tasks.
* Processed search-term data using Apache Spark.
* Used Spark SQL for analytical queries.
* Practiced saving and loading Spark ML models.
* Used a pretrained forecasting model for sales prediction.

---

# 🎯 What I Learned

The most important lesson from this project was how different data engineering technologies fit together.

A data engineer does not simply write SQL queries or Python scripts. The role involves building reliable systems that move data from operational sources through transformation and storage layers and finally make the data available for analytics and decision-making.

This project helped me understand the relationship between:

```text
Data Sources
     ↓
Databases
     ↓
ETL
     ↓
Data Warehouse
     ↓
Analytics
     ↓
Business Intelligence
     ↓
Big Data / Machine Learning
```

---

# 📜 Course

**IBM Data Engineering Professional Certificate — Data Engineering Capstone Project**

Provider: IBM / Coursera

The course is designed to demonstrate practical skills in relational databases, NoSQL, data warehouses, data pipelines, big data engines, SQL, Python, and analytics.

Course: [IBM Data Engineering Capstone Project — Coursera](https://www.coursera.org/learn/data-enginering-capstone-project?utm_source=chatgpt.com)

---

# 👨‍💻 Author

**Kaung Htet**

Data Engineering / Software Development Learner

Skills demonstrated in this project:

`Python` · `SQL` · `MySQL` · `MongoDB` · `PostgreSQL` · `IBM Db2` · `Cognos Analytics` · `Apache Airflow` · `Apache Spark` · `PySpark` · `ETL` · `Data Warehousing`

---

## ⭐ Project Summary

This capstone demonstrates an end-to-end **Data Engineering pipeline**, from operational databases and NoSQL systems through ETL, data warehousing, business intelligence, workflow orchestration, big data processing, and machine learning-based forecasting.
