# MLOps Weekly Assignments

One Iris classification project taken through the full MLOps course: cloud training, versioning, feature store, CI, tracking, deployment, security and LLM safety.

## Why this exists
Weekly graded assignments for the MLOps course in the IIT Madras BS in Data Science (roll number 23f3004013). Each week has its own branch (`week_01` to `week_11`); `master` holds the combined result.

## What it does
| Topic | Files |
|:--|:--|
| Cloud training on Vertex AI, artifacts in GCS | `train.py`, `inference.py` |
| Data and model versioning with DVC (GCS remote) | `iris.csv.dvc`, `iris_v2.csv.dvc`, `prepare_v1.py`, `prepare_v2.py` |
| Feature store with Feast (Parquet offline, SQLite online) | `iris_feature_repo/` |
| CI with data and model tests | `tests/`, `.github/workflows/ci.yml` |
| Experiment tracking with MLflow | `mlartifacts/`, `metrics.txt` |
| Docker image and Kubernetes deployment with autoscaling | `app.py`, `Dockerfile`, `deployment.yaml`, `service.yaml`, `hpa.yaml`, `post.lua` |
| Explainability, fairness and drift | `shap_analysis.py`, `fairness.py`, `drift_detection.py` |
| Data poisoning (MLSecOps) | `poison_data.py`, `train_poisoned.py`, `secure_pipeline.py` |
| LLM evaluation, prompt injection, prompt leakage, guardrails | `evaluate_llm.py`, `prompt_injection.py`, `prompt_leakage.py`, `guardrails.py` |

## Project structure
```
23f3004013_MLOPS_WEEKLY_ASSIGNMENT/
├── .github/workflows/  CI tests and Docker build
├── iris_feature_repo/  Feast entities and feature views
├── tests/              Data and model tests
├── mlartifacts/        MLflow run artifacts
├── app.py              FastAPI prediction service
├── train.py            Training on GCS data
├── inference.py        Inference with latest model
├── *.py                Weekly task scripts (see table)
├── *.yaml              Kubernetes manifests
├── Dockerfile          Container image
└── requirements.txt    Python dependencies
```

## Getting started
Requirements: Python 3.10+, DVC; a GCP project for the cloud and Kubernetes parts.
```bash
git clone https://github.com/abhijha8287/23f3004013_MLOPS_WEEKLY_ASSIGNMENT.git
cd 23f3004013_MLOPS_WEEKLY_ASSIGNMENT
pip install -r requirements.txt
dvc pull                     # needs access to the GCS remote
python train.py              # uses the GCS bucket set in the script
uvicorn app:app --port 8000  # expects final_model.pkl
```

To see one week on its own:
```bash
git checkout week_3
```

## Tests
```bash
pytest tests/
```

## Tech stack
Python, scikit-learn, DVC, Feast, MLflow, FastAPI, Docker, Kubernetes, Google Cloud (Vertex AI, GCS), GitHub Actions, SHAP, Fairlearn

## Notes
Course work; scored 100/100. GCP bucket names are hard-coded in the scripts. Change them before running in another project.
