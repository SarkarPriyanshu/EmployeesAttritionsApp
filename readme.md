# Employee Attrition Prediction App

## Description

This application is designed to predict employee attrition based on various factors such as job satisfaction, work-life balance, compensation, and more. By analyzing historical employee data, the app provides insights into potential turnover, helping HR departments take proactive steps to improve employee retention. The app uses machine learning models to identify patterns in employee behavior and generate predictions about which employees are likely to leave the company.

## Table of Contents

1. [Project Description](#how-to-setup)
2. [How to Setup](#how-to-setup)
    - 2.1 [Create Virtual Environment](#create-virtual-environment)
    - 2.2 [Install Dependencies](#install-dependencies)
    - 2.3 [Activate Virtual Environment](#activate-virtual-environment)
3. [Project Architecture](#project-architecture)
    - 3.1 [Data Ingestion](#data-ingestion)
    - 3.2 [Data Validation](#data-validation)
    - 3.3 [Data Transformation](#data-transformation)
    - 3.4 [Model Experimentation](#model-experimentation)
    - 3.5 [Hyperparameter Tuning](#hyperparameter-tuning)
    - 3.6 [Selecting Best Model](#selecting-best-model)

---
## 1. Project Description
This application is designed to predict employee attrition based on various factors such as job satisfaction, work-life balance, compensation, and more. By analyzing historical employee data, the app provides insights into potential turnover, helping HR departments take proactive steps to improve employee retention.

## 2. How to Setup

### 2.1 Create Virtual Environment

Before setting up the project, create a Python virtual environment. Run the following command:

#### Windows:
```bash
python -m venv venv
```


### Explanation of Commands:
1. **Creating Virtual Environment**: 
   - On Windows, `python -m venv venv` creates a virtual environment named `venv`.
   - On macOS/Linux, `python3 -m venv venv` creates the same.
   
2. **Activating the Virtual Environment**: 
   - On Windows: `.\venv\Scripts\activate` to activate the virtual environment.
   - On macOS/Linux: `source venv/bin/activate` to activate the virtual environment.

3. **Installing Dependencies**: 
   - Use `pip install -r requirements.txt` to install all dependencies from the `requirements.txt` file.

This ensures that you have all the necessary libraries installed in an isolated environment.

## 3. Project Architecture
![Project architecture](https://github.com/SarkarPriyanshu/EmployeesAttritionsApp/blob/main/images/project_archetechture.drawio.png)

### 3.1 Data Ingestion
![Data Ingestion](https://github.com/SarkarPriyanshu/EmployeesAttritionsApp/blob/main/images/data_ingestion.drawio.png)

### 3.2 Data Validation
![Data Validation](https://github.com/SarkarPriyanshu/EmployeesAttritionsApp/blob/main/images/Data_validation.drawio.png)

The second image is the **Evidently Report**, which helps us identify the **target drift problem**.

![Data Validation evidently](https://github.com/SarkarPriyanshu/EmployeesAttritionsApp/blob/main/images/data_validation_evidently_report_dash.png)

### 3.3 Data Transformation
![Data Transformation](https://github.com/SarkarPriyanshu/EmployeesAttritionsApp/blob/main/images/DataTransformation.drawio.png)


### 3.3 Model Selection
![Data Transformation](https://github.com/SarkarPriyanshu/EmployeesAttritionsApp/blob/main/images/Model_Selection.drawio%20(1).png)

The image below is the **Mlflow Report**, which helps us compare the **differnt models performance** in a centralized server so whole team can understand which model performing better and why.

![Data Transformation](https://github.com/SarkarPriyanshu/EmployeesAttritionsApp/blob/main/images/mlflow_dashboard.png)

The image below is the **Mlflow**, not only help us to **differnt models performance** but also help in understanding which **hyper parameter** is performing good.

![Data Transformation](https://github.com/SarkarPriyanshu/EmployeesAttritionsApp/blob/main/images/mlflow_single_model_parameter_compare.png)

The image below is the **Mlflow**, help us to compare **differnt models performance metrics**

![Data Transformation](https://github.com/SarkarPriyanshu/EmployeesAttritionsApp/blob/main/images/mlflow_comapre_metric_of_multiple_models.png)

## Thank You

Thank you for exploring this project! If you have any questions, feel free to reach out.
