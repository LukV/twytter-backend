"""Main"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import posts, tags
from app.core.database import Base, engine

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Adjust if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the posts routes
app.include_router(posts.router)
app.include_router(tags.router)
