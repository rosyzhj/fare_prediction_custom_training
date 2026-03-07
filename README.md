# fare_prediction_custom_training

## Overview
This course final project builds a scalable machine learning pipeline to predict NYC taxi fares using historical NYC taxi trip data. The system leverages PySpark for distributed data processing and model training and runs on Google Cloud Platform (GCP) infrastructure to efficiently handle large-scale trip datasets.

## Objectives
- Predict taxi trip fares based on trip characteristics and engineered features.
- Build a scalable training pipeline using PySpark.
- Run training and inference workflows in a GCP environment.

## Current Repository Structure
- `data_preparation.ipynb`: Data cleaning and feature preparation notebook.
- `VertexAI_model_train/task.py`: Vertex AI training entry point script.
- `VertexAI_model_train/start_training_job.ipynb`: Notebook for launching training jobs.
- `VertexAI_model_train/model_inferences.ipynb`: Notebook for model inference and evaluation.
- `report.pdf`: Final report/documentation artifact.

## Suggested Workflow
1. Prepare features in `data_preparation.ipynb`.
2. Export a model-ready training dataset to cloud storage.
3. Launch training via `VertexAI_model_train/task.py` and Vertex AI.
4. Evaluate with held-out data and validate inference outputs.
5. Track progress in Git and `PROJECT_PLAN.md`.

## Environment Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run Training Script (Example)
```bash
python VertexAI_model_train/task.py --data-path gs://YOUR_BUCKET/path/to/train.csv
```

## Notes
- Do not commit credentials or cloud keys.
- Keep large raw datasets in cloud/object storage, not in Git.
- Keep experiment outputs under ignored artifact directories.
