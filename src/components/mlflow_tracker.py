import mlflow
import mlflow.sklearn
import mlflow.xgboost

from xgboost import XGBRegressor

from src.logger import logger


class MLflowTracker:

    def __init__(self):

        # MLflow Tracking Database
        mlflow.set_tracking_uri("sqlite:///mlflow.db")

        # Experiment Name
        mlflow.set_experiment("Travel Intelligence MLOps")

    def log_complete_model(
        self,
        model_name,
        model,
        metrics,
        params=None
    ):

        logger.info(f"Starting MLflow run for {model_name}")

        with mlflow.start_run(run_name=model_name):

            # ----------------------------
            # Log Parameters
            # ----------------------------
            if params:
                mlflow.log_params(params)

            # ----------------------------
            # Log Metrics
            # ----------------------------
            mlflow.log_metrics(metrics)

            # ----------------------------
            # TEMPORARILY DISABLE MODEL LOGGING
            # ----------------------------
            logger.info("Skipping model artifact logging.")

        logger.info(f"{model_name} logged successfully.")