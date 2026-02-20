# IITM MLOps Weekly Assignment

## Overview
This repository contains the implementation of the IRIS classification pipeline developed as part of the IITM MLOps coursework.

The project demonstrates:
- Cloud-based ML pipeline using Google Cloud Platform (Vertex AI + GCS)
- Reproducible training and inference workflow
- Artifact storage in timestamped folders
- Data and model versioning using DVC
- Remote storage of datasets and models in Google Cloud Storage

---

# Week 1 – Cloud ML Pipeline

## Objective
Build an end-to-end ML pipeline for the IRIS dataset using GCP services.

## Steps Performed
- Created private GitHub repository and week_01 branch
- Activated GCP trial and enabled required APIs
- Created Vertex AI Workbench instance
- Uploaded dataset to Google Cloud Storage
- Built training pipeline fetching data from GCS
- Stored model artifacts in timestamped folders in GCS
- Built inference script that fetches latest model from GCS
- Successfully ran training twice and verified outputs

## Week-1 Files

### train.py
Downloads dataset from GCS, trains RandomForest classifier,  
stores model + metrics in timestamped artifact folders.

### inference.py
Fetches latest trained model from GCS and performs predictions.

### requirements.txt
Lists dependencies required to run the pipeline.

---

# Week 2 – Data Version Control (DVC)

## Objective
Extend the pipeline with reproducible dataset and model versioning using DVC.

## Steps Performed
- Initialized DVC inside repository
- Configured Google Cloud Storage as DVC remote backend
- Tracked dataset using DVC
- Simulated data augmentation to create new dataset version
- Tracked trained model files using DVC
- Pushed datasets and models to remote storage
- Demonstrated switching between versions using Git history + DVC checkout
- Verified local files revert correctly when switching versions

---

## DVC-Tracked Files

The following files are tracked using DVC (not stored directly in Git):

- iris.csv (original dataset)
- iris_v2.csv (augmented dataset version)
- model.pkl (trained model)

Corresponding `.dvc` files store metadata and references to remote storage.

---

# Repository Structure
.
├── train.py
├── inference.py
├── requirements.txt
├── README.md
├── iris.csv.dvc
├── iris_v2.csv.dvc
├── model.pkl.dvc
└── .dvc/


---

# Storage Structure

## Google Cloud Storage (Pipeline Artifacts)

data/iris.csv
artifacts/<timestamp>/model.pkl
artifacts/<timestamp>/metrics.txt


# Key Learnings

- Setting up reproducible ML pipelines on cloud infrastructure
- Using Vertex AI Workbench for development
- Managing datasets and models using DVC
- Integrating Git + DVC + GCS for full MLOps workflow
- Ensuring reproducibility through version control

---
