from fastapi import FastAPI
from apiis.router_get_post import router as user_router
from models.table_data import Table
from base import engine

# Initialize FastAPI app
app = FastAPI()

# Create database tables
Table.metadata.create_all(bind=engine)

# Register routes
app.include_router(user_router)

# Middleware (optional)
@app.middleware("http")
async def add_custom_header(request, call_next):
    response = await call_next(request)
    response.headers["X-Custom-Header"] = "CustomValue"
    return response
