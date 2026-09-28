from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta


# ============================================================
# Task 1 - Define the DAG arguments
# ============================================================

default_args = {
    'owner': 'Kaung Htet',
    'start_date': datetime(2023, 1, 1),
    'email': ['kaunghtet@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}


# ============================================================
# Task 2 - Define the DAG
# ============================================================

dag = DAG(
    'process_web_log',
    default_args=default_args,
    description='Process web server log file',
    schedule_interval='@daily',
    catchup=False
)


# ============================================================
# Task 3 - Extract data
# ============================================================

extract_data = BashOperator(
    task_id='extract_data',
    bash_command="""
    awk '{print $1}' /home/project/airflow/dags/capstone/accesslog.txt \
    > /home/project/airflow/dags/capstone/extracted_data.txt
    """,
    dag=dag
)


# ============================================================
# Task 4 - Transform data
# ============================================================

transform_data = BashOperator(
    task_id='transform_data',
    bash_command="""
    grep -v '198.46.149.143' \
    /home/project/airflow/dags/capstone/extracted_data.txt \
    > /home/project/airflow/dags/capstone/transformed_data.txt
    """,
    dag=dag
)


# ============================================================
# Task 5 - Load data
# ============================================================

load_data = BashOperator(
    task_id='load_data',
    bash_command="""
    tar -cf /home/project/airflow/dags/capstone/weblog.tar \
    -C /home/project/airflow/dags/capstone transformed_data.txt
    """,
    dag=dag
)


# ============================================================
# Task 6 - Define the task pipeline
# ============================================================

extract_data >> transform_data >> load_data

