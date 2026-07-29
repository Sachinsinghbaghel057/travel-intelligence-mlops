from src.pipeline.data_pipeline import DataPipeline
from src.pipeline.training_pipeline import TrainingPipeline


if __name__ == "__main__":

    print("=" * 60)
    print("Travel Intelligence MLOps")
    print("=" * 60)

    # Run Data Pipeline
    data_pipeline = DataPipeline()
    data_pipeline.run_pipeline()

    # Run Training Pipeline
    training_pipeline = TrainingPipeline()
    training_pipeline.run_pipeline()

    print("=" * 60)
    print("Pipeline Completed Successfully")
    print("=" * 60)