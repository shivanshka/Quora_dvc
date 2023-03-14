
from Quora_App.config.configuration import Configuration
from Quora_App.components import DataValidation
from Quora_App.logger import logging
from Quora_App.exception import ApplicationException
from Quora_App.entity import DataIngestionConfig, DataTransformationConfig
import sys

STAGE_NAME = "Data Validation stage"

def main():
    try:
        config = Configuration()
        data_ingestion_config = config.get_data_ingestion_config()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config=data_validation_config,
                                         data_ingestion_config=data_ingestion_config)
        data_validation.initiate_data_validation(train=True)
    except Exception as e:
        raise ApplicationException(e, sys) from e

if __name__ =='__main__':
    try:
        logging.info(f"\n\n>>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logging.info(f"\n\n>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==============x")
    except Exception as e:
        raise ApplicationException(e, sys) from e