from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator
from datetime import datetime, timedelta 

dag_owner = ''
google_cloud_conn_id = 'google-cloud-default'

default_args = {'owner': dag_owner,
        'depends_on_past': False,
        'retries': 2,
        'retry_delay': timedelta(minutes=5)
        }

with DAG(dag_id='test',
        default_args=default_args,
        description='',
        start_date=datetime(2023, 1, 1),
        schedule_interval='@daily',
        catchup=False,
        tags=['']
):

    start = EmptyOperator(task_id='start')

#this is just to ensure it actually works
#another

    test_query = BigQueryExecuteQueryOperator (
        task_id='test_query',
        sql = 'SELECT first_name FROM `i-love-basketball.fpl.elements` LIMIT 1',
        destination_dataset_table=None,
        write_disposition='WRITE_EMPTY',
        gcp_conn_id=google_cloud_conn_id,
        use_legacy_sql=False,
        )


    end = EmptyOperator(task_id='end')

start  >> test_query >> end