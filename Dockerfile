FROM python:3.9-slim


WORKDIR /app

COPY app.py /app/app.py
COPY model.joblib /app/model.joblib

RUN pip install scikit-learn numpy flask


CMD ["python", "app.py"]
