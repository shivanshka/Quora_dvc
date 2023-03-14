
from Quora_App.config.configuration import Configuration
from Quora_App.components import DataIngestion
from Quora_App.logger import logging
from Quora_App.exception import ApplicationException
import sys

STAGE_NAME = "Data Ingestion stage"

def main():
    try:
        config = Configuration()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        raise ApplicationException(e, sys) from e

if __name__ =='__main__':
    try:
        logging.info(f"\n\n>>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logging.info(f"\n\n>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==============x")
    except Exception as e:
        raise ApplicationException(e, sys) from e