from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.settings import get_settings
from app.routers.stuff import router as stuff_router
from app.utils import get_logger

logger = get_logger(__name__)

settings = get_settings()

def app_settings():
    settings = get_settings()
    app_settings = dict(docs_url=None, openapi_url=None, redoc_url=None)
    if settings.SHOW_DOCS:
        app_settings = dict(
            docs_url="/docs/",
            openapi_url="/openapi.json",
        )
    return app_settings


app = FastAPI(**app_settings())


@app.on_event("startup")
async def startup_event():
    logger.info("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down...")


app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=".*",
    allow_credentials=True,
    allow_methods="*",
    allow_headers="*",
)
app.include_router(stuff_router)


@app.get("/")
def root():
    return "(o_O)"

