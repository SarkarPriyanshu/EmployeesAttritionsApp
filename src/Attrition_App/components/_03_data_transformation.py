import pandas as pd

from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import (
                            MinMaxScaler,
                            OneHotEncoder,
                            LabelEncoder
                            )

from Attrition_App import logger
from Attrition_App.constants import *
from Attrition_App.utils.main_utils import read_yaml
from Attrition_App.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self,transformation_config:DataTransformationConfig):
        self.transformation_config = transformation_config
        self.schema = read_yaml(SCHEMA_FILE_PATH)
        self.data = None

    # This method loads data from a CSV file for transformation and handles potential loading errors.
    def load_data(self):
        """
        Loads data from a CSV file for transformation.

        The method attempts to load the data from the file specified by 'transformation_data_path'. 
        If successful, it stores the data in 'self.data' and logs a success message. 
        If loading the data fails, it logs a warning message.

        Args:
            None

        Returns:
            None
        """
        file_path = Path(self.transformation_config.transformation_data_path)
        try:
            self.data = pd.read_csv(file_path)
        except Exception as e:
            logger.warning('failed to load data for transformation.')
        else:
            logger.info('load data for transformation sucessfully.')   

    # This method transforms the data by selecting significant features, scaling and encoding them,
    # and then handles the resampling of the data. Finally, it saves the transformed data to specified paths.
    def transform_data(self):
        """
        Transforms the dataset by selecting significant features, scaling, encoding, and resampling.

        The method first selects the significant features and target feature from the dataset.
        Then, it applies MinMax scaling to numerical features, OneHot encoding to categorical features,
        and SMOTE resampling to balance the dataset. The transformed data is saved as CSV files to the 
        specified directory.

        Args:
            None

        Returns:
            None
        """
        significant_features = self.schema.significant_features
        target_feature = self.schema.target_feature

        self.data = self.data[significant_features]

        X_train = self.data.drop(target_feature,axis=1)
        y_train = LabelEncoder().fit_transform(self.data[target_feature])

        ColumnTransformerStep = ColumnTransformer([
            ('MinMaxScaler',MinMaxScaler(),self.schema.sacle_features),
            ('OneHotEncoder',OneHotEncoder(),self.schema.ohe_features)
        ])

        try:
            pipe = Pipeline([('cl',ColumnTransformerStep),('smt',SMOTE())])
            X_train,y_train = pipe.fit_resample(X_train,y_train)
        except Exception as e:
            logger.warning('data transformation failed.')
        else:
            logger.warning('data transformation succesful.')    

        X_train_path = Path.joinpath(Path(self.transformation_config.data_transform_dir),
                                     Path(TRANSFORMED_X_TRAIN_DATA_NAME))
        
        y_train_path = Path.joinpath(Path(self.transformation_config.data_transform_dir),
                                     Path(TRANSFORMED_Y_TRAIN_DATA_NAME))

        try:
            pd.DataFrame(X_train).to_csv(X_train_path)
            pd.DataFrame(y_train.reshape(-1,1)).to_csv(y_train_path)
        except Exception as e:
            logger.warning('failed to save transformed data into transformed artifact directory.')
        else:
            logger.info('transformed data saved into transformed artifact directory succesfully.')    


    def initialize_data_transformation(self):
        self.load_data()
        self.transform_data()


