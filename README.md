# IITM MLOps Weekly Assignment
**Roll Number:** 23f3004013

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
- Continuous Integration (CI) using GitHub Actions

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

## Week-1 Scripts

### `train.py`
- Downloads dataset from GCS
- Performs train-test split
- Trains RandomForest classifier
- Calculates accuracy

Stores model + metrics in:

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
- Simulated data augmentation (`iris_v2.csv`)
- Tracked trained model using DVC
- Pushed dataset & model to GCS remote

Demonstrated switching between dataset versions using:

```
git checkout <commit>
dvc checkout
```

Verified correct reversion of files.

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

- Offline Store → File-based Parquet
- Online Store → SQLite
- Entity → `iris_id`
- Feature View → `iris_features`

---

## Task 1 – Initialize Feature Repository

Created `iris_feature_repo`

Configured SQLite backend.

Committed feature store configuration files.

---

## Task 2 – Define Entities & Feature Views

Defined:

Entity:
```
iris_id
```

Data Source:
```
data/iris.parquet
```

Feature View:
```
iris_features
```

Feast requires an `event_timestamp` column.

Since IRIS is a static dataset, timestamps were generated using:

```python
pd.date_range(start="2020-01-01", periods=len(df), freq="D")
```

This allows proper historical feature retrieval.

---

## Task 3 – Apply & Materialize

Executed:

```
feast apply
feast materialize 2020-01-01 <today>
```

This step:

- Registers entities
- Registers feature views
- Loads feature values into the SQLite online store

Materialization ensures features are available for real-time inference.

---

## Task 4 – Training Using Offline Store

Script: `train_with_feast.py`

Steps performed:

- Initialize `FeatureStore`
- Create entity dataframe with `iris_id` and `event_timestamp`
- Fetch historical features using:

```
store.get_historical_features()
```

- Convert results to dataframe
- Train RandomForest classifier

Training strictly uses the **Feature Store** instead of raw CSV.

---

## Task 5 – Real-Time Inference Using Online Store

Script: `inference_with_feast.py`

Steps:

- Load trained model
- Provide entity rows (example `iris_id`)
- Fetch features using:

```
store.get_online_features()
```

- Retrieve feature values from SQLite online store
- Run `model.predict()`

This simulates **production inference using an online feature store**.

---

# Week 4 – Continuous Integration (CI) with GitHub Actions

## Objective
Introduce automated testing and CI pipelines to validate the ML workflow.

The goal is to ensure that every code change is automatically tested before merging into the main branch.

---

## Task 1 – Data Validation Tests

Implemented data validation tests using **pytest**.

Tests verify:

- Dataset loads correctly
- Expected columns exist
- No missing values
- Feature values fall within valid ranges

Example test file:

```
tests/test_data.py
```

These checks prevent corrupted or malformed datasets from breaking the ML pipeline.

---

## Task 2 – Model Evaluation Tests

Implemented model validation tests to ensure model performance remains acceptable.

Steps performed:

- Load trained model using `joblib`
- Load evaluation dataset
- Run predictions
- Compute accuracy
- Ensure accuracy meets minimum threshold

Example file:

```
tests/test_model.py
```

This prevents degraded models from being merged into the repository.

---

## Task 3 – GitHub Actions CI Pipeline

Created a CI workflow:

```
.github/workflows/ci.yml
```

Pipeline steps:

1. Checkout repository
2. Setup Python environment
3. Install dependencies
4. Authenticate with Google Cloud
5. Pull data and models from DVC
6. Run automated tests
7. Display test report

---

## Task 4 – DVC Integration in CI

Since datasets and models are versioned using DVC with a GCS remote, the CI pipeline retrieves them automatically.

```
dvc pull
```

This ensures tests always run on the correct versioned data and model artifacts.

Authentication is handled using a **GCP service account key stored in GitHub Secrets**.

---

## Task 5 – Automated Test Execution

The CI pipeline runs:

```
pytest tests/
```

Example CI output:

```
tests/test_data.py ....
tests/test_model.py ..

6 passed
```

This confirms the ML pipeline functions correctly.

---

## Task 6 – Pull Request CI Validation

Workflow:

1. Create branch `week_4`
2. Push changes to GitHub
3. Open Pull Request to merge into `main`
4. GitHub Actions automatically runs CI tests
5. Only after successful tests is the PR merged

This introduces **quality control into the ML pipeline**.

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
├── tests/
│   ├── test_data.py
│   └── test_model.py
├── .github/
│   └── workflows/
│       └── ci.yml
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

- No binary model files (`.pkl`)
- No raw datasets directly
- No dataset splits
- No video screencast
- No SQLite DB files