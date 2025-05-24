# 📊 Machine Learning Pipeline with Python & PySpark


[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![PySpark](https://img.shields.io/badge/pyspark-3.5.1-orange.svg)](https://spark.apache.org/docs/latest/api/python/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue.svg)](https://www.postgresql.org/)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](#)

---

## 📖 Overview

This project is a **Machine Learning Data Pipeline** built using Python, PySpark, Docker, and PostgreSQL.  
It follows a modular ETL (Extract, Transform, Load) and Machine Learning workflow that simulates real-world data processing scenarios.

The pipeline extracts data from Google Spreadsheets, stages it in a PostgreSQL database, transforms it, and loads it into a data warehouse. Finally, a machine learning model is trained, evaluated, and logged.

---

## 📦 Pipeline Architecture

**Spreadsheet → Staging DB (PostgreSQL) → Warehouse DB (PostgreSQL) → Machine Learning (PySpark + Sklearn)**  

### 📌 ETL Pipeline:
- Extract data from spreadsheet  
- Load to **staging database**
- Data transformation
- Load to **warehouse database**

### 📌 ML Pipeline:
- Extract data from **warehouse**
- Data preprocessing
- **Train-test split** 👉 performed **before outlier removal** to avoid *data leakage*
- Outlier removal only on **training set**
- Train a Decision Tree model
- Evaluate performance on the **original test set**

---

## 🛠️ Tools & Libraries

- Python 3.11  
- PySpark 3.5.1  
- PostgreSQL (Dockerized)  
- Pandas, Numpy, Scikit-learn  
- dotenv  
- Logging  
- Docker & Docker Compose  

---

## Project Structure
```
machine_learning_pipeline/
├── log/                         # Log file directory
│   └── info_process.log
├── marketing_staging/           # Staging database init scripts
│   └── init.sql
├── marketing_warehouse/         # Warehouse database init scripts
│   └── init.sql
├── src/                         # Source code modules
│   ├── staging/
│   ├── warehouse/
│   ├── modeling/
│   └── utils/
├── .flake8                      # Flake8 linting config
├── .gitignore                   # Git ignore rules
├── README.md                    # Project documentation
├── docker-compose.yml           # Docker Compose config
├── live_class_week_8.ipynb      # Jupyter notebook for live session
├── pipeline.py                  # Main pipeline script
├── requirements.txt             # Python dependencies
└── tempCodeRunnerFile.py        # Temp file (can be ignored)


```
