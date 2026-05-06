### A) Environment Setup

* Python version
* Poetry install
* Install dependencies

Example:

```
poetry install
```

---

### B) Run Training

```
make train
```

or

```
poetry run python src/train.py
```

---

### C) Run API

```
docker-compose up
```

or

```
uvicorn app.main:app --reload
```

---

### D) View MLflow UI

```
mlflow ui
```

---
