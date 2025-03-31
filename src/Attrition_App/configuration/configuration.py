from Attrition_App.constants import *
from Attrition_App.utils.main_utils import read_yaml, create_directories
from Attrition_App.entity.config_entity import (DataIngestionConfig,
                                                DataValidationConfig,
                                                DataTransformationConfig,
                                                ModelSelectionConfig) 

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    # This method retrieves the data ingestion configuration, creates the necessary directory,
    # and returns the configuration object.
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Retrieves and prepares the data ingestion configuration.

        This method:
        - Accesses the data ingestion configuration from the general config.
        - Ensures the necessary root directory for data ingestion is created.
        - Returns the `DataIngestionConfig` object containing the relevant paths for data ingestion.

        Args:
            None

        Returns:
            DataIngestionConfig: A configuration object containing paths for data ingestion.
        """
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file_path = config.local_data_file_path,
        )

        return data_ingestion_config
    
    # This method retrieves the data validation configuration, creates necessary directories,
    # and returns the configuration object.
    def get_data_validation_config(self) -> DataValidationConfig:
        """
        Retrieves and prepares the data validation configuration.

        This method:
        - Accesses the data validation configuration from the general config.
        - Ensures the necessary directories (for data validation and data splits) are created.
        - Returns the `DataValidationConfig` object containing the relevant paths for data validation.

        Args:
            None

        Returns:
            DataValidationConfig: A configuration object containing paths for data validation and splits.
        """
        config = self.config.data_validation
        create_directories([config.data_split_dir])
        create_directories([config.data_validation_dir])
        
        data_validation_config = DataValidationConfig(
            referral_data_path = config.referral_data_path,
            new_data_path = config.new_data_path,
            data_split_dir = config.data_split_dir,
            data_validation_dir = config.data_validation_dir,
            validation_report_file_name = config.validation_report_file_name
        )

        return data_validation_config
    
    # This method retrieves the data transformation configuration, creates necessary directories,
    # and returns the configuration object.
    def get_data_transformation_config(self)-> DataTransformationConfig:
        """
        Retrieves and prepares the data transformation configuration.

        This method:
        - Accesses the data transformation configuration from the general config.
        - Ensures the necessary directories (for storing transformed data) are created.
        - Returns the `DataTransformationConfig` object containing the relevant paths for data transformation.

        Args:
            None

        Returns:
            DataTransformationConfig: A configuration object containing paths for data transformation.
        """
        config = self.config.data_transformation
        create_directories([config.data_transform_dir])

        data_transformation_config = DataTransformationConfig(
            data_transform_dir = config.data_transform_dir,
            transformation_data_path = config.transformation_data_path
        )

        return data_transformation_config
    
    # This method retrieves the model selection configuration, creates necessary directories,
    # and returns the configuration object.
    def get_model_selection_config(self) -> ModelSelectionConfig:
        """
        Retrieves and prepares the model selection configuration.

        This method:
        - Accesses the model selection configuration from the general config.
        - Ensures the necessary directories (for storing models and artifacts) are created.
        - Returns the `ModelSelectionConfig` object containing the relevant paths for model selection.

        Args:
            None

        Returns:
            ModelSelectionConfig: A configuration object containing paths for model storage and transformation.
        """
        config = self.config.model_selection
        create_directories([config.best_models_artifact_dir])

        model_selection_config = ModelSelectionConfig(
            best_models_artifact_dir = config.best_models_artifact_dir,
            best_models_dir = config.best_models_dir,
            data_transform_dir = config.data_transform_dir
        )
        
        return model_selection_config