import mlflow
import mlflow.sklearn
import mlflow.xgboost

from xgboost import XGBRegressor

from src.logger import logger


class MLflowTracker:

    def __init__(self):

        mlflow.set_tracking_uri("sqlite:///mlflow.db")
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

            if params:
                mlflow.log_params(params)

            mlflow.log_metrics(metrics)

            if isinstance(model, XGBRegressor):

                logger.info("Logging XGBoost model...")

                mlflow.xgboost.log_model(
                    xgb_model=model,
                    artifact_path="model"
                )

            else:

                logger.info("Logging Scikit-Learn model...")

                mlflow.sklearn.log_model(
                    sk_model=model,
                    artifact_path="model"
                )

        logger.info(f"{model_name} logged successfully.")