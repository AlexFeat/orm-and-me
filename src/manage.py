import typer
import uvicorn

from app.settings import get_settings

app = typer.Typer()
settings = get_settings()


@app.command("runserver")
def _run(reload: bool = True):
    uvicorn.run(
        f"{settings.DIR_CODE}.main:app",
        host=settings.HOST,
        port=settings.PORT,
        workers=settings.UVICORN_WORKERS_COUNT,
        log_level=settings.UVICORN_LOG_LEVEL,
        reload=settings.UVICORN_RELOAD,
        access_log=True,
    )


@app.command()
def default():
    pass


if __name__ == "__main__":
    _run()
    app()