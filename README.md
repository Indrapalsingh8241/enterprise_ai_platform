# Enterprise AI Business Intelligence Platform

## Overview

Enterprise AI Business Intelligence Platform is an end-to-end analytics application that enables users to upload raw business datasets, perform automated analysis, generate machine learning insights, and interact with an AI-powered chatbot.

The platform combines Data Analytics, Machine Learning, Business Intelligence, and Generative AI into a single workflow.

---

## Features

### Data Upload & Processing

* Upload CSV datasets
* Automatic data loading and validation
* Dataset preview and summary statistics
* Missing value detection
* Duplicate record detection

### Automated Exploratory Data Analysis (EDA)

* Data profiling
* Distribution analysis
* Correlation heatmaps
* Feature visualization
* Business trend analysis

### Machine Learning Module

* Profit prediction model
* Automated feature engineering
* Model training and evaluation
* R² Score calculation
* Feature importance analysis
* Business performance prediction

### AI Business Insights

* Automated business recommendations
* Feature impact interpretation
* Performance analysis
* Decision-support insights

### RAG-Based Business Chatbot

* Retrieval-Augmented Generation (RAG)
* ChromaDB vector database
* Hugging Face embeddings
* Groq LLM integration
* Context-aware business question answering

---

## System Architecture

User Uploads Dataset
↓
Data Validation & Cleaning
↓
Exploratory Data Analysis
↓
Machine Learning Analysis
↓
Business Insight Generation
↓
ChromaDB Knowledge Base
↓
AI Business Chatbot

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* FastAPI

### Machine Learning

* Scikit-Learn
* XGBoost
* Pandas
* NumPy

### Visualization

* Matplotlib
* Plotly

### AI & RAG

* LangChain
* ChromaDB
* Hugging Face Embeddings
* Groq LLM

### Deployment

* Docker
* Docker Compose

---

## Project Structure

enterprise_ai_platform/

├── backend/

│   ├── routes/

│   ├── services/

│   ├── models/

│

├── frontend/

│

├── RAG/

│   ├── embeddings.py

│   ├── ingest.py

│   ├── retriever.py

│   └── chroma_db/

│

├── datasets/

├── ml_models/

├── visualizations/

├── docker/

├── notebooks/

└── README.md

---

## Installation

### Clone Repository

git clone <repository-url>

cd enterprise_ai_platform

### Create Virtual Environment

python -m venv myvenv

source myvenv/bin/activate

### Install Dependencies

pip install -r requirements.txt

---

## Environment Variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key

---

## Run Backend

cd backend

uvicorn main:app --reload

Backend URL:

http://127.0.0.1:8000

---

## Run Frontend

cd frontend

streamlit run app.py

Frontend URL:

http://localhost:8501

---

## API Endpoints

### Upload Dataset

POST /upload

### Data Cleaning

POST /clean

### Generate Visualizations

POST /visualizations

### Predict Profit

POST /predict

### AI Business Chat

POST /chat

---

## Sample Workflow

1. Upload business dataset.
2. Perform automated data analysis.
3. Generate visualizations and insights.
4. Train machine learning models.
5. View model performance metrics.
6. Analyze feature importance.
7. Interact with AI Business Assistant.
8. Receive actionable business recommendations.

---

## Future Enhancements

* AutoML integration
* Automated target column detection
* Multi-dataset analysis
* PDF report generation
* Advanced business forecasting
* Cloud deployment
* User authentication
* Real-time analytics dashboard

---

## Author

Indrapal Singh

AI | Machine Learning | Data Analytics | FastAPI | Streamlit | Generative AI
# enterprise_ai_platform
# enterprise_ai_platform
# enterprise_ai_platform
