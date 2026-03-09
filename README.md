# NYC Taxi Fare Prediction (PySpark + Vertex AI Custom Training)

A scalable machine learning project that predicts NYC taxi fares from historical trip data using PySpark and GCP Vertex AI Custom Training.

## Why This Project
This project demonstrates end-to-end ML workflow skills on large transportation data:
- Distributed data processing with PySpark
- Feature engineering for tabular regression
- Cloud-based model training with GCP Vertex AI Custom Training
- Reproducible analysis in notebooks

## Tech Stack
- Python
- PySpark
- XGBoost
- Scikit-learn
- Google Cloud Platform (GCS + Vertex AI Custom Training)

## Repository Structure
- `data_preparation.ipynb`: data cleaning and feature engineering
- `VertexAI_model_train/task.py`: training entrypoint for custom training
- `VertexAI_model_train/start_training_job.ipynb`: launch training jobs
- `VertexAI_model_train/model_inferences.ipynb`: inference and evaluation checks
- `report.pdf`: final project report

## How It Works
1. Prepare and transform trip data.
2. Build model-ready features.
3. Train the fare prediction model using GCP Vertex AI Custom Training.
4. Evaluate predictions on hold-out data.

## Run Locally (Core Script)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python VertexAI_model_train/task.py --data-path gs://YOUR_BUCKET/path/to/train.csv
```

## Portfolio Notes
Yes, this repo can be used as a portfolio project. To make it stronger:
- Add one short section with final metrics (R2, RMSE/MAE)
- Add one architecture diagram screenshot
- Add 2-3 bullet points on scale (dataset size, runtime, cluster setup)
