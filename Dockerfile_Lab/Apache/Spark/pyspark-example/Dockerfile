FROM bitnami/spark:latest

COPY requirements.txt .
RUN pip3 install -r requirements.txt

CMD ["python", "main.py" ]

COPY main.py .
