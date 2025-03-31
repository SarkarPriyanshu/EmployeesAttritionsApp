# Employee Attrition Prediction App

## Description

This application is designed to predict employee attrition based on various factors such as job satisfaction, work-life balance, compensation, and more. By analyzing historical employee data, the app provides insights into potential turnover, helping HR departments take proactive steps to improve employee retention. The app uses machine learning models to identify patterns in employee behavior and generate predictions about which employees are likely to leave the company.

## Table of Contents

1. [How to Setup](#how-to-setup)
    - 1.1 [Create Virtual Environment](#create-virtual-environment)
    - 1.2 [Install Dependencies](#install-dependencies)
    - 1.3 [Activate Virtual Environment](#activate-virtual-environment)
2. [Project Architecture](#project-architecture)
    - 2.1 [Data Ingestion](#data-ingestion)
    - 2.2 [Data Validation](#data-validation)
    - 2.3 [Data Transformation](#data-transformation)
    - 2.4 [Model Experimentation](#model-experimentation)
    - 2.5 [Hyperparameter Tuning](#hyperparameter-tuning)
    - 2.6 [Selecting Best Model](#selecting-best-model)

---

## 1. How to Setup

### 1.1 Create Virtual Environment

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

