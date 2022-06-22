import airflow

from airflow.models import DAG
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator

dag = DAG(
	dag_id = "Airflow_dag_Spark_Submit",schedule_interval = '* * * * *'

	)
