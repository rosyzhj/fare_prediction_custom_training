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
- `data/links/yellow_2024_2025_links.txt`: extracted TLC parquet links used for ingestion
- `scripts/extract_tlc_yellow_links.py`: scrape and filter yellow taxi parquet links from TLC website
- `scripts/upload_links_to_gcs.sh`: batch copy listed parquet files into GCS
- `VertexAI_model_train/task.py`: training entrypoint for custom training
- `VertexAI_model_train/start_training_job.ipynb`: launch training jobs
- `VertexAI_model_train/model_inferences.ipynb`: inference and evaluation checks
- `report.pdf`: final project report

## How It Works
1. Extract yellow taxi parquet file links from the TLC trip data page.
2. Load raw parquet files into GCS for scalable processing.
3. Prepare and transform trip data.
4. Build model-ready features.
5. Train the fare prediction model using GCP Vertex AI Custom Training.
6. Evaluate predictions on hold-out data.

## Data Acquisition
```bash
# 1) Scrape TLC links for yellow taxi parquet files (2024-2025 by default)
python scripts/extract_tlc_yellow_links.py \
  --start-year 2024 \
  --end-year 2025 \
  --output data/links/yellow_2024_2025_links.txt

# 2) Upload all files from the link list into your GCS prefix
bash scripts/upload_links_to_gcs.sh \
  data/links/yellow_2024_2025_links.txt \
  gs://YOUR_BUCKET/taxi-data/yellow
```
