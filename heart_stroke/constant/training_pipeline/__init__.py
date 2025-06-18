import os

from heart_stroke.constant.s3_bucket import TRAINING_BUCKET_NAME

TARGET_COLUMN = "stroke"
PIPELINE_NAME: str = "heart_stroke"
ARTIFACT_DIR: str = "artifact"

# common file name

FILE_NAME: str = "heart_stroke.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
PREPROCESSING_OBJECT_FILE_NAME: str = "preprocessing.pkl"
MODEL_FILE_NAME = "model.pkl"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

"""Data Ingestion realted constants"""
DATA_INGESTION_COLLECTION_NAME: str = "heart_stroke"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2

"""Data Validation related constants"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"