import os
from datetime import datetime

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y/%m/%d-%H:%M:%S')}"

ROOT_DIR= os.getcwd()

CONFIG_DIR= "config"
CONFIG_FILE_NAME= "config.yaml"
CONFIG_FILE_PATH= os.path.join(ROOT_DIR, CONFIG_DIR, CONFIG_FILE_NAME)

SCHEMA_FILE_NAME= "schema.yaml"
SCHEMA_FILE_PATH= os.path.join(ROOT_DIR, CONFIG_DIR, SCHEMA_FILE_NAME)

TRAINED_MODELS_YAML_FILE_NAME= "models.yaml"
TRAINED_MODELS_YAML_FILE_PATH= os.path.join(ROOT_DIR, CONFIG_DIR, TRAINED_MODELS_YAML_FILE_NAME)

#CURRENT_TIME_STAMP= get_current_time_stamp()

#Training Pipeline related variables
TRAINING_PIPELINE_CONFIG_KEY= 'training_pipeline_config'
TRAINING_PIPELINE_NAME_KEY= 'pipeline_name'
TRAINING_PIPELINE_ARTIFACT_DIR_KEY= 'artifacts'

#Data Ingestion related variables
DATA_INGESTION_CONFIG_KEY= 'data_ingestion_config'
DATA_INGESTION_ARTIFACT_DIR_KEY= 'data_ingestion'
DATA_INGESTION_DOWNLOAD_URL_KEY= 'download_url'
DATA_INGESTION_RAW_DATA_DIR_KEY= 'raw_data_dir'
DATA_INGESTION_ZIPPED_DIR_KEY= 'zipped_download_dir'
DATA_INGESTION_INGESTED_DIR_KEY= 'ingested_dir'

#Data Validation related variables
DATA_VALIDATION_CONFIG_KEY= 'data_validation_config'
DATA_VALIDATION_ARTIFACT_DIR_KEY= 'data_validation'
DATA_VALIDATION_SCHEMA_DIR_KEY= 'schema_dir'
DATA_VALIDATION_SCHEMA_FILE_NAME_KEY= 'schema_file_name'

#Data Transformation related variables
DATA_TRANSFORMATION_CONFIG_KEY= 'data_transformation_config'
DATA_TRANSFORMATION_ARTIFACT_DIR_KEY= 'data_transformation'
DATA_TRANSFORMATION_DIR_NAME_KEY= 'transformed_dir'
DATA_TRANSFORMATION_TRAIN_DIR_KEY= 'transformed_train_dir'
DATA_TRANSFORMATION_TEST_DIR_KEY= 'transformed_test_dir'
DATA_TRANSFORMATION_PREPROCESSING_DIR_KEY= 'preprocessed_dir'
DATA_TRANSFORMATION_FEAT_ENG_OBJ_FILE_NAME_KEY= 'feature_eng_object_file_name'
DATA_TRANSFORMATION_PREPROCESSED_OBJ_FILE_NAME_KEY= 'preprocessed_object_file_name'

#Model Training related variables
MODEL_TRAINER_CONFIG_KEY= 'model_trainer_config'
MODEL_TRAINER_ARTIFACT_DIR_KEY= 'model_trainer'
MODEL_TRAINER_DIR_NAME_KEY= 'trained_model_dir'
MODEL_TRAINER_FILE_NAME_KEY= 'model_file_name'
MODEL_TRAINER_BASE_ACCURACY_KEY= 'base_accuracy'

