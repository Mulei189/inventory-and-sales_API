from fastapi import FastAPI

from core.database import Base, engine
from modules.auth.router import router as auth_router

app = FastAPI(
    title="StockFlow API",
    description="API for inventory and sales management",
    version="1.0.0"
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(auth_router)

@app.get("/")
def root():
    return {
        "message": "StockFlow API Running"
    }
@app.get('/health')
def health():
    return {
        "status": "healthy!"
    }