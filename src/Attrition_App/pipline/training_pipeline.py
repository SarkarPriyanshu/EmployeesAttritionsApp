from Attrition_App import logger
from Attrition_App.components._01_data_ingestion import DataIngestion
from Attrition_App.components._02_data_validation import DataValidation
from Attrition_App.components._03_data_transformation import DataTransformation
from Attrition_App.components._04_model_selection import ModelSelection
from Attrition_App.configuration.configuration import ConfigurationManager


class TraningPipeline:
    STAGE_NAME = 'Data Ingestion'
    def __init__(self):
        pass

    def data_ingestion(self):
        logger.info(f'\n>>>>> Stage: Data Ingestion started <<<<<<\n' )
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(ingestion_config=data_ingestion_config)
        data_ingestion.initialize_data_ingestion()
        logger.info(f'\n>>>>> Stage: Ingestion completed <<<<<<\n' )

    def data_validation(self):
        logger.info(f'\n>>>>> Stage: Data Validation started <<<<<<\n' )
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(validation_config=data_validation_config)
        data_validation.initialize_data_validation()
        logger.info(f'\n>>>>> Stage: Data Validation completed <<<<<<\n' )

    def data_transformation(self):
        logger.info(f'\n>>>>> Stage: Data transformation started <<<<<<\n' )
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(transformation_config=data_transformation_config)
        data_transformation.initialize_data_transformation()
        logger.info(f'\n>>>>> Stage: Data transformation completed <<<<<<\n' )    

    def model_selection(self):
        logger.info(f'\n>>>>> Stage: Model Selection started <<<<<<\n' )
        config = ConfigurationManager()
        model_selection_config = config.get_model_selection_config()
        model_selection = ModelSelection(model_selection_config=model_selection_config)
        model_selection.initialize_model_selection()
        logger.info(f'\n>>>>> Stage: Model Selection completed <<<<<<\n' )    

    def main(self):
        self.data_ingestion()
        self.data_validation() 
        self.data_transformation()
        self.model_selection()   
        