from fastapi import FastAPI
from app.config.database import Base, engine
from app.controller.user_controller import router as user_router

# Create database tables if not exist
Base.metadata.create_all(bind=engine)

# Initialize FastAPI application
app = FastAPI(title="Python CRUD with MySQL")

# Register user routes
app.include_router(user_router)
