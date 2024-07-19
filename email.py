from airflow import DAG
from airflow.operators.email_operator import EmailOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2024, 7, 19),
}

dag = DAG(
    'send_email_dag',
    default_args=default_args,
    description='A simple DAG to send an email',
    schedule_interval=timedelta(days=1),
    catchup=False,
)

send_email = EmailOperator(
    task_id='send_email',
    to='artem_badanov@inbox.ru',
    subject='Test Email from Airflow',
    html_content='<h3>Hello Artem!</h3><p>This is a test email sent from Apache Airflow.</p>',
    dag=dag,
)

send_email
