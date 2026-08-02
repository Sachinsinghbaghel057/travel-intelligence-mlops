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

        logger.info("=" * 60)
        logger.info(f"Starting MLflow Run : {model_name}")
        logger.info("=" * 60)

        with mlflow.start_run(run_name=model_name):

            # ---------------------------------------
            # Parameters
            # ---------------------------------------
            if params:
                mlflow.log_params(params)
                logger.info("Parameters logged.")

            # ---------------------------------------
            # Metrics
            # ---------------------------------------
            mlflow.log_metrics(metrics)
            logger.info("Metrics logged.")

            # ---------------------------------------
            # Model Artifact
            # ---------------------------------------
            #
            # Disabled for Jenkins because the Docker
            # container has limited RAM.
            #
            # Enable this after increasing Docker memory.
            #
            # if isinstance(model, XGBRegressor):
            #
            #     mlflow.xgboost.log_model(
            #         xgb_model=model,
            #         name="model"
            #     )
            #
            # else:
            #
            #     mlflow.sklearn.log_model(
            #         sk_model=model,
            #         name="model"
            #     )

            logger.info("Model artifact logging skipped.")

        logger.info("=" * 60)
        logger.info("MLflow Run Completed Successfully")
        logger.info("=" * 60)