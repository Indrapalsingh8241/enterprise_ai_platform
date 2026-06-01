from fastapi import FastAPI
from fastapi import APIRouter
from backend.routes.data_routes import router as data_router
from backend.routes.upload_routes import router as upload_router
from backend.routes.cleaning_routes import router as cleaning_router
from backend.routes.visualization_routes import router as visualization_router
from backend.routes.prediction_route import router as prediction_router
from backend.routes.chat_route import router as chat_router


app = FastAPI(
    title="Enterprise AI Platform",
    description="AI-powered analytics and forecasting platform",
    version="1.0.0"
)
app.include_router(data_router)
app.include_router(upload_router)
app.include_router(cleaning_router)
app.include_router(visualization_router)
app.include_router(prediction_router)
app.include_router(chat_router)

@app.get("/")
def home():
    return {
        "message": "Enterprise AI Platform Backend Running "
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }