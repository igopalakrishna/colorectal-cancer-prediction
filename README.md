# Colorectal Cancer Survival Prediction (Full-Stack MLOps)

An end-to-end MLOps pipeline to predict 5-year survival outcomes for colorectal cancer patients using clinical data. Designed for hospitals, clinics, and researchers, the project integrates model training, deployment, and tracking using modern MLOps tools.

## Project Overview

- **Goal:** Predict survival chances (Yes/No) for patients with colorectal cancer.
- **Dataset:** ~167,497 clinical records with 28 features (Kaggle-sourced).
- **Model:** Gradient Boosting Classifier (Scikit-learn)
- **Pipeline Orchestration:** Kubeflow Pipelines + Minikube + Docker
- **Deployment:** Flask Web UI for clinical input and prediction
- **Tracking:** MLflow + DAGsHub for online experiment tracking

## Tech Stack

| Layer         | Tools Used |
|--------------|------------|
| Language      | Python 3.9 |
| ML Framework  | Scikit-learn, GradientBoostingClassifier |
| MLOps Tools   | MLflow, DAGsHub, Docker, Kubeflow Pipelines, Minikube |
| Frontend UI   | Flask, HTML/CSS |
| Versioning    | Git + GitHub |
| Deployment    | Docker Hub + Localhost (via Minikube) |

## Key Features

- Modular codebase with class-based components for reusability
- Chi-Squared feature selection reducing dimensionality by 82% (5 out of 28)
- Training Metrics: Accuracy = 59.9%, ROC-AUC ≈ 0.50 (synthetic data)
- MLflow Integration: Local + Remote (DAGsHub) tracking of metrics & artifacts
- Kubeflow Pipelines for containerized orchestration of data processing + training
- Interactive Flask UI for clinicians to input features and receive predictions

## Use Cases

1. **Patient Monitoring:** Track survival changes over time based on clinical updates
2. **Treatment Planning:** Adjust interventions for high-risk patients
3. **Resource Allocation:** Prioritize patients with lower survival predictions

## Results

| Metric        | Value     |
|---------------|-----------|
| Accuracy      | 59.95%    |
| Precision     | 53.62%    |
| Recall        | 59.95%    |
| F1 Score      | 45.36%    |
| ROC-AUC       | 0.4996    |
| Top Features  | Healthcare_Costs, Tumor_Size_mm, Treatment_Type, Diabetes, Mortality_Rate_per_100K |

## Directory Structure

```
colorectal-cancer-prediction/
├── artifacts/             # Raw and processed data, model artifacts
├── kubeflow_pipeline/     # KFP pipeline YAML + Python compiler
├── notebook/              # Jupyter notebooks for initial EDA and model testing
├── src/                   # Modular Python scripts for preprocessing & training
├── static/                # CSS for Flask frontend
├── templates/             # HTML templates for UI
├── app.py                 # Flask application
├── Dockerfile             # Docker configuration
├── kfpipeline.yaml        # Compiled Kubeflow pipeline
├── requirements.txt       # Dependencies
└── setup.py               # Project installer
```

## MLflow on DAGsHub

DAGsHub enables remote MLflow tracking. View metrics, parameters, and artifacts:

**Run Dashboard:** [https://dagshub.com/igopalakrishna/colorectal-cancer-prediction.mlflow](https://dagshub.com/igopalakrishna/colorectal-cancer-prediction.mlflow)

## Setup & Run Locally

### 1. Clone & Install
```bash
git clone https://github.com/igopalakrishna/colorectal-cancer-prediction.git
cd colorectal-cancer-prediction
pip install -e .
```

### 2. Run Preprocessing Pipeline
```bash
python src/data_processing.py
```

### 3. Train & Track Model
```bash
python src/model_training.py
```

### 4. Launch Flask Web App
```bash
python app.py
# Visit http://127.0.0.1:5000
```

## Kubeflow Pipelines (Optional)

### Build & Push Docker Image
```bash
docker build -t yourdockerhubusername/mymlopsapp .
docker push yourdockerhubusername/mymlopsapp
```

### Compile KFP YAML
```bash
python kubeflow_pipeline/kf_pipeline.py
```

### Open Kubeflow Dashboard
```bash
kubectl port-forward svc/ml-pipeline-ui -n kubeflow 8080:80
# Visit: http://localhost:8080
```

## Future Improvements

- Integrate FastAPI for scalable backend
- Use real-world clinical data for better generalization
- Hyperparameter tuning using Optuna or Ray Tune
- CI/CD with GitHub Actions + GCP/AWS deployment

