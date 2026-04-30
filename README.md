# Student-Performance-Prediction-System
Machine Learning system to predict student performance and risk
# 🎓 Student Performance Prediction System

## 📌 Overview
This project predicts student performance (pass/fail & risk level) using Machine Learning.

## 🚀 Features
- Predict student performance
- Risk classification (Low / Medium / High)
- Feature importance analysis
- SHAP explainability
- FastAPI backend

## 🧠 Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- SHAP
- FastAPI
- Matplotlib

## 📊 Model
- Random Forest Classifier
- Accuracy-based evaluation
- Probability-based risk scoring

## 🔥 API Endpoints
- `/predict` → Predict student performance

## 📈 Outputs
- Feature importance graph
- SHAP explainability graph
- Risk prediction API

## 🖼️ Screenshots


### 🔹 Feature Importance
![Feature Importance](images/feature_importance_graph.png)

### 🔹 SHAP Feature
![SHAP](images/shap_feature_impact.png)


## ▶️ Run Project

```bash
pip install -r requirements.txt
python3 src/train.py
uvicorn serving.app:app --reload
