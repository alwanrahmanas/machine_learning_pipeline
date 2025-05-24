# 📊 Machine Learning Pipeline with Python & PySpark

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![PySpark](https://img.shields.io/badge/pyspark-3.5.1-orange.svg)](https://spark.apache.org/docs/latest/api/python/)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](#)

## 📑 Deskripsi

Proyek ini merupakan implementasi **data pipeline dan machine learning pipeline** menggunakan Python dan PySpark. Pipeline dirancang untuk mengelola data marketing bank, dimulai dari ekstraksi data, staging, transformasi, hingga pemodelan machine learning.

---

## 📦 Arsitektur Pipeline

Spreadsheet → Staging DB (PostgreSQL) → Warehouse DB (PostgreSQL) → Machine Learning (PySpark + Sklearn)

1. **ETL Pipeline**
   - Ekstraksi data dari spreadsheet
   - Load ke **staging database**
   - Transformasi data
   - Load ke **warehouse database**

2. **ML Pipeline**
   - Ekstraksi data dari **warehouse**
   - Preprocessing data
   - **Train-test split** (👉 dilakukan sebelum outlier removal untuk mencegah *data leakage*)
   - Outlier removal hanya di **training set**
   - Training model Decision Tree
   - Evaluasi performa di **test set original**

---

## 🛠️ Tools & Library

- Python 3.11
- PySpark 3.5.1
- PostgreSQL (Dockerized)
- Pandas, Numpy, Scikit-learn
- dotenv
- Logging
- Docker & Docker Compose

---

## Struktur Project
```
machine_learning_pipeline/
├── src/
│   ├── staging/
│   ├── warehouse/
│   ├── modeling/
│   ├── utils/
├── log/
├── .env
├── docker-compose.yml
├── pipeline.py
└── README.md

```
