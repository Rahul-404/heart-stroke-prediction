# 🩺 Heart Stroke Prediction using Machine Learning

## 📌 Overview

This project focuses on building a predictive model to estimate the risk of stroke in individuals based on demographic and medical features. Early prediction of stroke risks can help healthcare providers take preventive measures and prioritize patient care.

---

## 📂 Dataset

- **Source:** [Kaggle Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
- **Rows:** 5,110
- **Target Variable:** `stroke` (1 = Stroke, 0 = No Stroke)

### **Features:**

| Feature             | Description                               |
| ------------------- | ----------------------------------------- |
| gender              | Male / Female / Other                     |
| age                 | Age of the patient                        |
| hypertension        | 0: No, 1: Yes                             |
| heart\_disease      | 0: No, 1: Yes                             |
| ever\_married       | Marital status                            |
| work\_type          | Type of employment                        |
| Residence\_type     | Urban / Rural                             |
| avg\_glucose\_level | Average glucose level in blood            |
| bmi                 | Body Mass Index                           |
| smoking\_status     | Smoking status                            |
| stroke              | Target variable (0: No stroke, 1: Stroke) |

---

## ⚙️ Project Workflow

1️⃣ **Data Preprocessing**

- Missing value imputation (`bmi`)
- Encoding categorical variables
- Feature scaling
- Outlier detection & treatment

2️⃣ **Exploratory Data Analysis (EDA)**

- Distribution plots of key features
- Correlation analysis
- Class imbalance visualization

3️⃣ **Handling Class Imbalance**

- Used **SMOTE (Synthetic Minority Oversampling Technique)** to balance the dataset.

4️⃣ **Model Building**

- **Algorithms used:**

  - Logistic Regression
  - Random Forest
  - XGBoost
  - Support Vector Classifier (SVC)
- **Hyperparameter Tuning:** GridSearchCV / RandomizedSearchCV

5️⃣ **Model Evaluation**

- Metrics used: Precision, Recall, F1-Score, ROC-AUC
- **Priority on Recall & ROC-AUC** to reduce false negatives (critical for healthcare)

6️⃣ **Model Explainability**

- Feature importance from tree-based models
- SHAP value visualization for interpretability

---

## 📊 Results

| Model         | ROC-AUC | Recall | F1-Score |
| ------------- | ------- | ------ | -------- |
| Random Forest | 0.92    | 0.86   | 0.78     |
| XGBoost       | 0.93    | 0.88   | 0.80     |

- Top predictors of stroke: **age**, **avg\_glucose\_level**, **hypertension**, **heart\_disease**

---

## 🛠 Tech Stack

- **Languages & Libraries:** Python, Pandas, NumPy, Scikit-learn, XGBoost, imbalanced-learn
- **Visualization:** Matplotlib, Seaborn, Plotly
- **Data Validation:** Evidently
- **RESTful API:** FastAPI
- **Model Interpretability:** SHAP

---

## 🚀 How to Run

```bash
git clone https://github.com/your-username/heart-stroke-prediction.git
cd heart-stroke-prediction
pip install -r requirements_dev.txt
python demo.py
python python app.py
```

---

## 🚀 Deployment Plan

The model will be deployed as a **REST API** using **FastAPI**, hosted on **AWS EC2**, with the following architecture:

### ⚙️ **Deployment Stack**

- **FastAPI** → REST API serving stroke predictions
- **AWS S3** → Store model artifacts (e.g., trained `.pkl` files)
- **AWS ECR (Elastic Container Registry)** → Docker image registry
- **AWS EC2** → Hosting the Dockerized FastAPI service
- **Github Actions CI/CD** → Automate build, test, and deployment pipelines
- **Docker** → Containerization of the application

### ✅ **CI/CD Workflow**

1. **Push code to GitHub** → Trigger github actions Pipeline
2. **Github Actions**:

   - Build Docker image
   - Push image to **AWS ECR**
   - Deploy/update container on **AWS EC2**
3. **FastAPI** running on EC2 → Exposes `/predict` endpoint for stroke prediction
4. Model artifacts loaded from **AWS S3** during container startup


![Deployment-Architecture]()

---

## 📧 Contact

For questions or collaboration:
**Your Name** – [rahulshelke3399@gmail.com](mailto:rahulshelke3399@gmail.com)
[LinkedIn](https://www.linkedin.com/in/rahulshelke981) | [GitHub](https://github.com/R  ahul-404)
