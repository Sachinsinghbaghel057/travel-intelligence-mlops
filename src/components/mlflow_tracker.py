import mlflow
import mlflow.sklearn
import mlflow.xgboost

from xgboost import XGBRegressor

from src.logger import logger


class MLflowTracker:

    def __init__(self):

        # SQLite Tracking Database
        mlflow.set_tracking_uri("sqlite:///mlflow.db")

        # Create / Use Experiment
        mlflow.set_experiment("Travel Intelligence MLOps")

    def log_complete_model(
        self,
        model_name,
        model,
        metrics,
        params=None
    ):

        with mlflow.start_run(run_name=model_name):

            # -------------------------------
            # Parameters
            # -------------------------------

            if params:
                mlflow.log_params(params)

            # -------------------------------
            # Metrics
            # -------------------------------

            mlflow.log_metrics(metrics)

            # -------------------------------
            # Log Model
            # -------------------------------

            if isinstance(model, XGBRegressor):

                logger.info("Logging XGBoost model...")

                mlflow.xgboost.log_model(
                    xgb_model=model,
                    name="model"
                )

            else:

                logger.info("Logging Scikit-Learn model...")

                mlflow.sklearn.log_model(
                    sk_model=model,
                    name="model"
                )

            logger.info(f"{model_name} logged successfully to MLflow.")