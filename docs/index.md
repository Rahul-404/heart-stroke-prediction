# Stroke Risk Stratification System

> **Production-grade, end-to-end ML system for clinical stroke risk stratification**

---

## Overview

The **Stroke Risk Stratification System** is a full-stack, production-oriented machine learning project that predicts an individual’s risk of stroke based on demographic, clinical, and lifestyle features. The system is designed to reflect **real-world data science and MLOps practices**, not just offline model training.

This repository demonstrates how a stroke prediction use case can be taken from **problem framing and experimentation** to **reproducible training, model governance, deployment-ready artifacts, and monitoring**.

The project emphasizes:

* Strong **problem framing and success criteria**
* Reproducible **feature engineering and modeling pipelines**
* Experiment tracking and lineage using **MLflow**
* CI/CD-driven infrastructure and deployment workflows
* Cloud-native design aligned with **AWS MLOps patterns**

---

## Problem Statement

Stroke is one of the leading causes of death and long-term disability worldwide. Early identification of high-risk individuals enables preventive interventions and better allocation of healthcare resources.

**Objective**:
Build a machine learning system that stratifies individuals into risk categories (e.g., low / medium / high) based on available patient data, enabling clinicians and healthcare systems to:

* Identify high-risk patients early
* Prioritize preventive care
* Support data-driven clinical decision-making

This project treats stroke prediction as a **risk stratification problem**, not just a binary classification task.

---

## Business & Clinical Context

From a real-world perspective:

* False negatives (missing a high-risk patient) are **costlier** than false positives
* Model outputs must be **interpretable and auditable**
* Data leakage, reproducibility, and monitoring are critical

Therefore, this system is designed with:

* Explicit metric trade-offs
* Versioned data, code, and models
* Clear separation between experimentation and production

---

## Success Criteria

The project defines success across **three dimensions**:

### 1. Model Performance

* Primary metric: **Recall / Sensitivity for high-risk patients**
* Secondary metrics: ROC-AUC, Precision, F1-score
* Performance validated via cross-validation and holdout datasets

### 2. Engineering Quality

* Deterministic, reusable preprocessing and feature engineering pipelines
* Unit and integration tests for transformations and models
* CI pipeline capable of building and testing artifacts

### 3. Production Readiness

* End-to-end experiment tracking (parameters, metrics, artifacts)
* Model registry with versioning and stage transitions
* Deployment-ready inference artifacts
* Monitoring hooks for drift and performance degradation

---

## System Architecture (High Level)

At a high level, the system consists of:

* **Data Sources**

    * Structured patient data (demographics, clinical attributes)

* **Experimentation Layer**

    * Jupyter notebooks for EDA and hypothesis testing
    * MLflow for experiment tracking

* **Training & Pipelines**

    * Modular feature engineering and preprocessing pipelines
    * Model training, evaluation, and selection

* **Model Registry**

    * Versioned models with metadata and lineage

* **Inference Stack**

    * Containerized model serving
    * API-based inference (AWS API Gateway + Lambda + SageMaker Endpoint)

* **Monitoring & Governance**

    * Model performance tracking
    * Data drift and prediction drift detection

---

## What This Project Demonstrates

This is **not** a Kaggle-style notebook-only project.

It demonstrates:

* How real-world ML problems are framed
* How experimentation transitions into production pipelines
* How MLOps tools are integrated coherently
* How decisions are documented and justified

If you are a **recruiter, ML engineer, or data scientist**, this repository is intended to show that the system is:

* Thoughtfully designed
* Technically sound
* Production-aware

---

## Documentation Structure

The documentation is organized as follows:

* **Project Overview** – Problem framing, goals, and success criteria
* **Data Understanding** – Dataset description and limitations
* **Feature Engineering** – Transformations, encoders, and imputations
* **Modeling** – Algorithms, evaluation strategy, and selection
* **Experiment Tracking** – MLflow usage and experiment design
* **MLOps & CI/CD** – Testing, pipelines, and infrastructure
* **Deployment** – Inference architecture and serving strategy
* **Monitoring** – Drift, performance, and governance

Each section focuses on *why* decisions were made, not just *how*.

---

## Intended Audience

This project is designed for:

* Data Scientists transitioning to production ML
* ML Engineers and MLOps practitioners
* Recruiters and hiring managers evaluating real-world ML skills

A basic familiarity with machine learning and cloud concepts is assumed.

---

## Getting Started

If you are new to this project, start with:

1. **Problem Framing & Data Understanding**
2. **Feature Engineering Pipeline**
3. **Experiment Tracking with MLflow**
4. **Training and Model Selection**
5. **Deployment & Monitoring**

Each section builds on the previous one.

---

## Disclaimer

This project is for **educational and demonstrational purposes only**.
It is **not a medical device** and should not be used for real clinical decision-making.

---

## Author

**Rahul Shelke**
End-to-End Data Science & MLOps Practitioner

---

> *The goal of this project is not just to predict stroke risk, but to demonstrate how reliable, auditable, and production-ready machine learning systems are built in the real world.*
