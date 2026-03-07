# Project Plan and Milestones

## Milestone 1: Data Foundation
- [ ] Validate schema and data quality for NYC trip data.
- [ ] Define target variable and baseline feature set.
- [ ] Document train/validation/test split strategy.

## Milestone 2: Distributed Processing
- [ ] Implement scalable feature transformations in PySpark.
- [ ] Benchmark processing time on representative dataset sizes.
- [ ] Save model-ready dataset to GCS.

## Milestone 3: Model Training (Vertex AI)
- [ ] Parameterize training entry point (`task.py`).
- [ ] Launch training job on GCP and capture logs.
- [ ] Track model metrics (R2, RMSE/MAE as needed).

## Milestone 4: Evaluation and Inference
- [ ] Validate model behavior on held-out test set.
- [ ] Run inference workflow and sanity-check predictions.
- [ ] Compare results with baseline model.

## Milestone 5: Final Delivery
- [ ] Finalize report with architecture and results.
- [ ] Clean repository and documentation.
- [ ] Tag release candidate for submission.
