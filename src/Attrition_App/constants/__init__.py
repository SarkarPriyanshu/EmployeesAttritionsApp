from pathlib import Path
import os

# Data Injestion Constants
CONFIG_FILE_PATH =  Path('config\config.yaml')

# Data Validation Constants
TRAIN_DATASET_NAME = 'train.csv'
TEST_DATASET_NAME = 'test.csv'

TOTAL_NO_OF_COLUMNS = 35
TARGET_COLUMN = 'Attrition'
SCHEMA_FILE_PATH = Path('config\schema.yaml')

# Data Transformation Constants
TRANSFORMED_X_TRAIN_DATA_NAME = 'X_train_trfm.csv'
TRANSFORMED_Y_TRAIN_DATA_NAME = 'Y_train_trfm.csv'

# Data Modeling Constants
MODEL_FILE_PATH = Path('config\model.yaml')
MODEL_SELECTION_TRAIN_X = 'X_train_trfm.csv'
MODEL_SELECTION_TRAIN_Y = 'Y_train_trfm.csv'
MODEL_SELECTION_TOP_SELECTS = 3
MODEL_SELECTION_FOLDS = 5
MODEL_SELECTION_MODELS_LIST = ['lr','dt','rf','gbc']
MODEL_SELECTION_TARGET = 'target'
MODEL_SELECTION_BEST_MODEL = 'model.pkl'



