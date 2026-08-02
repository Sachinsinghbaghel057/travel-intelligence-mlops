from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="travel_intelligence_training_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["travel", "mlops"],
) as dag:

    train_model = BashOperator(
        task_id="train_model",
        bash_command="""
        echo "Starting Travel Intelligence MLOps Pipeline"
        cd /opt/airflow/project
        python -m src.pipeline.main_pipeline
        """
    )

    train_model