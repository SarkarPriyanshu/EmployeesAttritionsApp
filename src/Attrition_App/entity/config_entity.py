# This entity holds yaml file return types
from dataclasses import dataclass
from pathlib import Path

# DataIngestionConfig class holds the configuration for the data ingestion process.
# The class is frozen to make it immutable after instantiation.
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path  # The root directory where data will be stored after ingestion
    source_url: Path  # The URL from where data will be sourced
    local_data_file_path: Path  # Local path to store the ingested data file

# DataValidationConfig class holds the configuration for the data validation process.
# The class is frozen to make it immutable after instantiation.
@dataclass(frozen=True)
class DataValidationConfig:
    referral_data_path: Path  # Path to the referral data used for validation
    new_data_path: Path  # Path to the new data to be validated
    data_split_dir: Path  # Directory to store data splits
    data_validation_dir: Path  # Directory to store validation results/reports
    validation_report_file_name: Path  # The file name for storing the validation report

# DataTransformationConfig class holds the configuration for the data transformation process.
# The class is frozen to make it immutable after instantiation.
@dataclass(frozen=True)
class DataTransformationConfig:
    data_transform_dir: Path  # Directory to store transformed data
    transformation_data_path: Path  # Path to the raw data to be transformed

# ModelSelectionConfig class holds the configuration for model selection process.
# The class is frozen to make it immutable after instantiation.
@dataclass(frozen=True)    
class ModelSelectionConfig:
    best_models_artifact_dir: Path  # Directory to store artifacts of the best models
    best_models_dir: Path  # Directory to store the best performing models
    data_transform_dir: Path  # Directory where the transformed data is stored for model selection

