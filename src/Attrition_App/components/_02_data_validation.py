import pandas as pd
import evidently
from evidently.report import Report
from evidently import ColumnMapping
from evidently.metrics import ColumnDriftMetric, DatasetMissingValuesMetric

from Attrition_App.constants import *
from sklearn.model_selection import train_test_split
from pathlib import Path
from Attrition_App import logger
from Attrition_App.utils.main_utils import read_yaml
from Attrition_App.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self,validation_config:DataValidationConfig):
        self.validation_config = validation_config
        self.columns = None
        self.schemas = read_yaml(SCHEMA_FILE_PATH)

    # This function loads a dataset, splits it into training and test sets, 
    # and saves them into the specified directory if they don't already exist.
    def load_dataset(self):
        """
        Loads the dataset, splits it into training and test sets, and saves them to the specified directory.

        The method reads the dataset from the 'referral_data_path' specified in the 'validation_config',
        splits it into training and test sets using an 80-20 split, and saves them as CSV files to the 
        'data_split_dir' if they don't already exist. It logs information about the dataset loading 
        and the splitting process.

        Args:
            None

        Returns:
            None
        """
        dataset_path = Path(self.validation_config.referral_data_path)
        logger.info('Found data into artifact directory')
        data = pd.read_csv(dataset_path)  
        self.columns = data.columns.to_list()

        train_set,test_set = train_test_split(data,test_size=0.2)

        train_path = Path.joinpath(Path(self.validation_config.data_split_dir),Path(TRAIN_DATASET_NAME))
        test_path = Path.joinpath(Path(self.validation_config.data_split_dir),Path(TEST_DATASET_NAME))

        if not train_path.exists() and not test_path.exists():
            logger.info('Saved new train and test split into data_split directory.')    
            train_set.to_csv(train_path)
            test_set.to_csv(test_path)
        else:
            logger.info('train and test set already exist in data_split directory.')

    # This function checks if all the required columns, including numerical and categorical features, 
    # exist in the dataset and logs errors if any columns are missing.
    def check_all_columns_exist(self):
        """
        Checks if all required columns (total, numerical, and categorical) exist in the dataset.

        The method verifies that the number of columns matches the expected total (defined by 'TOTAL_NO_OF_COLUMNS').
        It also checks if each numerical and categorical column (as defined in 'schemas') is present in the dataset.
        If any columns are missing, it logs an error message for each missing column and updates the corresponding status.

        Args:
            None

        Returns:
            bool: True if all required columns exist, False if any column is missing.
        """
        all_columns_satus = True
        numerical_columns_status = True
        categorical_columns_status = True

        if len(self.columns) != TOTAL_NO_OF_COLUMNS:
            logger.error(f'Total columns expected was {TOTAL_NO_OF_COLUMNS}, but get {len(self.columns)}!')
            all_columns_satus = False
        
        for column in self.schemas.numerical_feature:
            if column not in self.columns:
                logger.error(f'Column {column} not present in data!')
                numerical_columns_status = False

        for column in self.schemas.categorical_feature:
            if column not in self.columns:
                logger.error(f'Column {column} not present in data!')
                categorical_columns_status = False

        return all([all_columns_satus,numerical_columns_status,categorical_columns_status])

    
    # This method checks if there is any data drift by comparing the target feature in the reference dataset 
    # and the new dataset, and generates a report on the results.
    def check_target_drift(self):
        """
        Checks for data drift in the target feature by comparing the reference dataset and the new dataset.

        The method creates a data drift report using the 'ColumnDriftMetric' for the target feature and 
        'DatasetMissingValuesMetric' to analyze any missing values. It loads the reference data and the new 
        data, runs the report, and saves the report as an HTML file. If data drift is detected, the method 
        returns a boolean indicating the drift status.

        Args:
            None

        Returns:
            bool: True if drift is detected, False otherwise.
        """
        
        column_mapping = ColumnMapping(
            numerical_features = self.schemas.numerical_feature,
            categorical_features = self.schemas.numerical_feature,
            target = self.schemas.target_feature
        )
    
        report = Report(metrics = [
                        ColumnDriftMetric(column_name = self.schemas.target_feature),
                        DatasetMissingValuesMetric()
                ])
        
        ref_data = pd.read_csv(self.validation_config.referral_data_path)
        new_data = pd.read_csv(self.validation_config.new_data_path)

        if 'Unnamed: 0' in new_data.columns.to_list():
            new_data.drop('Unnamed: 0',axis=1,inplace=True)

        report.run(reference_data=ref_data,current_data=new_data,column_mapping=column_mapping)

        report_dir_name = Path(self.validation_config.validation_report_file_name)
        report.save_html(str(report_dir_name))
        logger.info('Data drift report updated.')
        drift_detected_status = report.as_dict()['metrics'][0]['result']['drift_detected'] 
        return drift_detected_status

    def initialize_data_validation(self):
        self.load_dataset()
        logger.info('Feature validation started.')
        columns_validation_status = self.check_all_columns_exist()
        if columns_validation_status:
            logger.info('Feature validation completed successfully.')
        else:
            logger.info('Feature validation failed.')    

        check_target_drift = self.check_target_drift()
        if check_target_drift:
            logger.info('Target drift detected.')
        else:
            logger.info('Target drift not detected.')

