import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter

from api.handlers import user_router

"""API Routes Block"""

app = FastAPI(title="kipia-crm-system")

# create routes
main_api_routes = APIRouter()

# set routes to the app instance
main_api_routes.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(main_api_routes)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    