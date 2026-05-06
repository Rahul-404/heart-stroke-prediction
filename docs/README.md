# Stroke Risk Stratification System — Production-Grade ML

## Executive Summary

An end‑to‑end, production‑grade machine learning system for **stroke risk stratification**, designed to mirror **Big Tech ML standards**. The project demonstrates rigorous problem framing, reproducible experimentation, robust feature engineering, model governance, CI/CD, cloud‑native deployment, and post‑deployment monitoring. While trained on a public dataset, the system is architected to be **enterprise‑ready**, auditable, and extensible to real clinical settings.

---

## Why This Project Matters

* **Business‑first framing**: Moves beyond Kaggle metrics to risk stratification, thresholding, and decision trade‑offs.
* **Production realism**: Treats data, models, and infra as long‑lived assets with versioning, testing, and monitoring.
* **Hiring signal**: Demonstrates how I would build, ship, and operate ML systems in a real organization.

---

## What’s Implemented (End to End)

### 1. Problem & Success Criteria

* Clearly defined prediction task aligned to downstream decisions (risk bands vs raw probabilities)
* Explicit offline metrics (ROC‑AUC, PR‑AUC, calibration) and online success proxies

### 2. Data & Feature Engineering

* Schema‑first data contracts with validation
* Production‑safe preprocessing using **custom scikit‑learn transformers**
* Leakage‑aware feature engineering and imputations
* Fully serialized feature pipeline reused across training and inference

### 3. Experimentation & Model Management

* **MLflow‑based experiment tracking** (params, metrics, artifacts, pipelines)
* Reproducible runs with environment capture
* Model selection driven by metrics + calibration, not leaderboard scores
* Versioned models promoted via a **model registry**

### 4. Evaluation & Model Card

* Segment‑level analysis (fairness & robustness signals)
* Threshold analysis tied to business cost
* Model Card documenting intended use, limitations, and risks

### 5. System Architecture

* Cloud‑native design (AWS‑aligned):

  * Training via managed pipelines
  * Containerized inference
  * API‑driven prediction surface
* Infrastructure defined via **Terraform** (no manual setup)

![Architecture](docs/assets/diagrams/architecture.svg)

### 6. Quality, CI/CD & Monitoring

* Unit, integration, and pipeline tests
* Smoke tests on synthetic data
* Data drift & prediction monitoring
* Clear rollback and retraining triggers

### 7. Governance & Risk Management

* Explicit non‑medical disclaimer and scope control
* Bias, misuse, and data drift risks documented
* Roadmap for clinical validation and compliance hardening

---

## Tech Stack

* **ML**: Python, scikit‑learn, MLflow
* **Data Validation**: Schema & quality checks
* **Infra**: AWS, Terraform, Docker
* **CI/CD**: GitHub Actions
* **Docs**: MkDocs (architecture‑level documentation, not notebooks)

---

## What This Is *Not*

* ❌ A Kaggle notebook
* ❌ A single‑script demo
* ❌ A claim of clinical readiness

This is a **systems‑level ML project** that shows how I approach real‑world ML engineering problems under production constraints.

---

## How a Big Tech Team Could Use This

* As a reference architecture for tabular ML systems
* As a starting point for regulated ML pipelines
* As evidence of ML engineering depth beyond model training

---

## Author

**Rahul Shelke**
Machine Learning / MLOps Engineer
Focus: production ML systems, reliability, and governance

---

> This repository is intentionally documentation‑heavy. The goal is not just to build a model, but to show how to **design, ship, and operate ML responsibly at scale**.


### MkDocs pages

| Page              | Visual                |
| ----------------- | --------------------- |
| `architecture.md` | Full infra diagram    |
| `experiments.md`  | Experiment flow       |
| `evaluation.md`   | ROC + calibration     |
| `monitoring.md`   | Drift detection loop  |
| `api_spec.md`     | Request/response flow |
