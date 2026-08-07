# Enterprise AI Business Intelligence Platform

An end-to-end AI-powered Business Intelligence platform that automates data analytics, machine learning, business insight generation, and conversational AI from raw business datasets.

---

# Business Problem

Organizations often struggle to transform raw business data into meaningful insights because the analytics workflow is fragmented across multiple tools. Data cleaning, exploratory analysis, machine learning, visualization, and reporting typically require different platforms and significant manual effort.

This project addresses that challenge by providing a unified AI-powered Business Intelligence platform that automates the complete analytics workflow—from dataset upload to AI-generated business recommendations and interactive business question answering.

---

# Overview

Enterprise AI Business Intelligence Platform enables users to upload business datasets and automatically perform:

- Data Validation & Cleaning
- Exploratory Data Analysis (EDA)
- Machine Learning Predictions
- Business Insight Generation
- AI-powered Business Recommendations
- Conversational Business Intelligence using RAG

The platform combines **Business Intelligence, Data Analytics, Machine Learning, and Generative AI** into a single workflow, enabling faster and more informed business decision-making.

---

# Key Highlights

- End-to-End Business Intelligence Platform
- Automated Data Validation & Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning Pipeline
- Profit Prediction using XGBoost
- Interactive Business Dashboards
- AI-powered Business Recommendation Engine
- RAG-based Business Chatbot
- FastAPI Backend
- Streamlit Frontend
- Dockerized Deployment

---

# Business Value

The platform helps organizations:

- Reduce manual effort in business analytics
- Automatically clean and validate datasets
- Identify key business drivers using Machine Learning
- Generate AI-assisted business recommendations
- Improve decision-making through interactive dashboards
- Enable non-technical users to interact with business data using natural language

---

# Features

## Data Upload & Processing

- Upload CSV datasets
- Automatic data loading
- Dataset validation
- Missing value detection
- Duplicate record detection
- Dataset preview
- Summary statistics

---

## Automated Exploratory Data Analysis (EDA)

- Data profiling
- Distribution analysis
- Correlation heatmaps
- Feature visualization
- Business trend analysis

---

## Machine Learning Module

- Automated Feature Engineering
- Profit Prediction Model
- Model Training
- Model Evaluation
- R² Score
- Feature Importance Analysis
- Business Performance Prediction

---

## AI Business Insights

- Automated Business Recommendations
- Performance Analysis
- Feature Impact Interpretation
- Decision Support Insights

---

## RAG-Based Business Chatbot

- Retrieval-Augmented Generation (RAG)
- LangChain
- ChromaDB Vector Database
- Hugging Face Embeddings
- Groq LLM
- Context-aware Business Question Answering

---

# System Architecture

```text
                  CSV Business Dataset
                           │
                           ▼
              Data Validation & Cleaning
                           │
                           ▼
         Exploratory Data Analysis (EDA)
                           │
                           ▼
              Feature Engineering
                           │
                           ▼
          Machine Learning Models
                           │
                           ▼
      Business Insights & Predictions
                           │
                           ▼
             ChromaDB Knowledge Base
                           │
                           ▼
         AI Business Intelligence Chatbot
```

---

# Tech Stack

## Frontend

- Streamlit

## Backend

- FastAPI

## Machine Learning

- Scikit-Learn
- XGBoost
- Pandas
- NumPy

## Data Visualization

- Matplotlib
- Plotly

## AI & RAG

- LangChain
- ChromaDB
- Hugging Face Embeddings
- Groq LLM

## Deployment

- Docker
- Docker Compose

---

# Project Structure

```text
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
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Indrapalsingh8241/enterprise_ai_platform.git

cd enterprise_ai_platform
```

---

## Create Virtual Environment

```bash
python -m venv myvenv
```

### Windows

```bash
myvenv\Scripts\activate
```

### Linux / macOS

```bash
source myvenv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=your_api_key
```

---

# Run Backend

```bash
cd backend

uvicorn main:app --reload
```

Backend

```
http://127.0.0.1:8000
```

---

# Run Frontend

```bash
cd frontend

streamlit run app.py
```

Frontend

```
http://localhost:8501
```

---

# API Endpoints

| Method | Endpoint | Description |
|----------|------------|----------------------------|
| POST | /upload | Upload dataset |
| POST | /clean | Data cleaning |
| POST | /visualizations | Generate charts |
| POST | /predict | Profit prediction |
| POST | /chat | AI Business Assistant |

---

# Sample Workflow

1. Upload a business dataset.
2. Validate and clean the data.
3. Perform automated exploratory data analysis.
4. Generate visualizations.
5. Train Machine Learning models.
6. Evaluate model performance.
7. Generate business insights.
8. Ask questions through the AI Business Assistant.
9. Receive context-aware business recommendations.

---

# Future Enhancements

- AutoML Integration
- Automated Target Column Detection
- Multi-dataset Analysis
- PDF Report Generation
- Explainable AI (SHAP)
- Advanced Business Forecasting
- Cloud Deployment (AWS/Azure)
- User Authentication
- Real-time Analytics Dashboard
- Scheduled Model Retraining

---

# Screenshots

> Add screenshots here for:

- Dashboard
- Data Cleaning
- EDA
- Prediction
- Business Insights
- AI Chatbot

---

# Author

**Indrapal Singh**

AI • Machine Learning • Data Analytics • Business Intelligence • FastAPI • Streamlit • Generative AI

GitHub:
https://github.com/Indrapalsingh8241

LinkedIn:
https://www.linkedin.com/in/indrapal-singh-thakur-148a73332
