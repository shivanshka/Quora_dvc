
from Quora_App.config.configuration import Configuration
from Quora_App.components import ModelTrainer, DataTransformation
from Quora_App.logger import logging
from Quora_App.exception import ApplicationException
from Quora_App.entity import  DataTransformationArtifact
import sys

STAGE_NAME = "Model Training stage"

def main():
    try:
        config = Configuration()
        model_trainer_config = config.get_model_trainer_config()
        data_ingestion_config = config.get_data_ingestion_config()
        data_transformation_config = config.get_data_transformation_config()

        data_transformation = DataTransformation(data_transformation_config=data_transformation_config,
                                             data_ingestion_artifact=data_ingestion_config)
        data_transformation_artifact= data_transformation.initiate_data_transformation()
        
        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config, 
                                     data_transformation_artifact=data_transformation_artifact)
        model_trainer.initiate_model_training()
    except Exception as e:
        raise ApplicationException(e, sys) from e

if __name__ =='__main__':
    try:
        logging.info(f"\n\n>>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logging.info(f"\n\n>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==============x")
    except Exception as e:
        raise ApplicationException(e, sys) from e