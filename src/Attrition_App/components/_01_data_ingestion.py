import os
import shutil
from Attrition_App import logger
from Attrition_App.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,ingestion_config:DataIngestionConfig):
        self.ingestion_config = ingestion_config

    # This function deletes the local data file if it exists and logs the result.
    def clean_up(self):
        """
        Cleans up the local data file by deleting it if it exists.

        This method checks if the file specified by 'self.ingestion_config.local_data_file_path' exists. 
        If it does, it deletes the file and logs a message indicating the file has been deleted.
        If the file doesn't exist, it logs a different message indicating the file is not present.
        """
        if os.path.exists(self.ingestion_config.local_data_file_path):
            os.remove(self.ingestion_config.local_data_file_path)  
            logger.info(f"File Attrition.csv has been deleted.")
        logger.info(f"File Attrition.csv does not exist.")

    # This function checks if the local data file exists, and if not, copies the file from the source URL to the local directory.
    def download_file(self):
        """
        Downloads a file from the specified source URL and saves it to the local directory.

        The function checks if the file already exists at the local path specified by 
        'self.ingestion_config.local_data_file_path'. If the file doesn't exist, it copies 
        the file from 'self.ingestion_config.source_url' to 'self.ingestion_config.root_dir' 
        and logs a success message. If the file already exists, it logs a warning message.

        Args:
            None

        Returns:
            None
        """
        if not os.path.exists(self.ingestion_config.local_data_file_path):
            shutil.copy(self.ingestion_config.source_url, self.ingestion_config.root_dir)
            logger.info('Status: Successful, Info: File have been copied from source.')
        else:    
            logger.warning('Status: Already Present, Info: Unable to copy copied file from source.')

    def initialize_data_ingestion(self):
        self.clean_up()
        self.download_file()
        