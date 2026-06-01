FROM python:3.10

WORKDIR /app

COPY frontend/requirements.txt .

RUN pip install -r requirements.txt

COPY frontend .

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]