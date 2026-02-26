# IITM MLOps Weekly Assignment  
**Roll Number: 23f3004013**

---

# Overview

This repository contains the complete implementation of the IRIS classification pipeline developed as part of the IITM MLOps coursework.

The project demonstrates a production-style MLOps workflow including:

- Cloud-based ML pipeline using Google Cloud Platform (Vertex AI + GCS)
- Reproducible training & inference workflows
- Artifact storage using timestamped directories
- Data and model versioning using DVC
- Remote storage integration with Google Cloud Storage
- Feature Store integration using Feast (Offline + Online store)

---

# Week 1 – Cloud ML Pipeline (Vertex AI + GCS)

## Objective
Build an end-to-end IRIS ML pipeline using GCP services.

## Steps Performed
- Created private GitHub repository
- Created branch `week_01`
- Activated GCP trial
- Enabled required APIs (Vertex AI, Compute Engine, Cloud Storage)
- Created Vertex AI Workbench instance
- Uploaded IRIS dataset to Google Cloud Storage
- Built training pipeline fetching data from GCS
- Stored model artifacts in timestamped folders
- Built inference script fetching latest model from GCS
- Successfully ran training multiple times producing different artifact folders

---

## Week-1 Scripts

### `train.py`
- Downloads dataset from GCS
- Performs train-test split
- Trains RandomForest classifier
- Calculates accuracy
- Stores model + metrics in:
  ```
  gs://bucket-name/artifacts/<timestamp>/
  ```

### `inference.py`
- Identifies latest timestamped model
- Downloads model from GCS
- Runs inference on evaluation samples

### `requirements.txt`
Contains required Python dependencies for cloud pipeline.

---

# Week 2 – Data Version Control (DVC)

## Objective
Make the ML pipeline reproducible using DVC for data & model versioning.

## Steps Performed
- Initialized DVC in branch `week_2`
- Configured GCS bucket as DVC remote
- Tracked dataset using DVC
- Simulated data augmentation (iris_v2.csv)
- Tracked trained model using DVC
- Pushed dataset & model to GCS remote
- Demonstrated switching between dataset versions using:
  ```
  git checkout <commit>
  dvc checkout
  ```
- Verified correct reversion of files

---

## DVC-Tracked Files

Tracked using DVC (NOT stored directly in Git):

- iris.csv
- iris_v2.csv
- model.pkl

Only `.dvc` pointer files are committed.

---

# Week 3 – Feature Store Integration (Feast)

## Objective
Integrate Feast Feature Store into IRIS pipeline.

## Architecture
- Offline Store: File-based Parquet
- Online Store: SQLite
- Entity: iris_id
- Feature View: iris_features

---

## Task 1 – Initialize Feature Repository

- Created `iris_feature_repo`
- Configured SQLite backend
- Committed feature store config

---

## Task 2 – Define Entities & Feature Views

Defined:

- Entity: `iris_id`
- Data Source: `data/iris.parquet`
- Feature View: `iris_features`

Added proper `event_timestamp` using:

```python
pd.date_range(start="2020-01-01", periods=len(df), freq="D")
```

---

## Task 3 – Apply & Materialize

Executed:

```
feast apply
feast materialize 2020-01-01 <today>
```

Features successfully materialized to SQLite online store.

---

## Task 4 – Training Using Offline Store

### `train_with_feast.py`

- Fetches historical features using:
  ```
  store.get_historical_features()
  ```
- Trains RandomForest classifier
- Saves model locally (not committed to Git)

This ensures:
✔ No direct CSV reading for training  
✔ Training strictly via Feature Store  

---

## Task 5 – Real-Time Inference Using Online Store

### `inference_with_feast.py`

- Retrieves features using:
  ```
  store.get_online_features()
  ```
- Loads trained model
- Performs prediction
- Demonstrates production-like inference

---

# Final Repository Structure

```
.
├── train.py
├── inference.py
├── requirements.txt
├── iris.csv.dvc
├── iris_v2.csv.dvc
├── model.pkl.dvc
├── .dvc/
├── iris_feature_repo/
│   ├── feature_repo/
│   │   ├── feature_definitions.py
│   │   ├── train_with_feast.py
│   │   ├── inference_with_feast.py
│   │   ├── data/iris.parquet
│   │   └── feature_store.yaml
└── README.md
```

---

# Not Included in Repository

As per submission guidelines:

- No binary model files (.pkl)
- No raw datasets directly
- No dataset splits
- No video screencast
- No SQLite DB files

---

