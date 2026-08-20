from fastapi import FastAPI
from core.database import Base, engine
from modules.auth.router import router as auth_router
from modules.products.router import router as products_router
from modules.categories.router import router as categories_router
from modules.suppliers.router import router as suppliers_router


app = FastAPI(
    title="StockFlow API",
    description="API for inventory and sales management",
    version="1.0.0"
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(auth_router)
app.include_router(products_router)
app.include_router(categories_router)
app.include_router(suppliers_router)

# Root endpoint
@app.get("/")
def root():
    return {
        "message": "StockFlow API Running"
    }

# Health check endpoint
@app.get('/health')
def health():
    return {
        "status": "healthy!"
    }