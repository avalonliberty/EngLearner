from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .api.routes import router as vocabulary_router

app = FastAPI(
    title="EngLearner API",
    description="Vocabulary learning with Fibonacci-based spaced repetition",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(vocabulary_router)

static_docs_path = Path(__file__).parent.parent.parent / "static_docs"


@app.get("/")
def root():
    return {"message": "EngLearner API", "version": "1.0.0"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/documentations", include_in_schema=False)
@app.get("/documentations/", include_in_schema=False)
async def documentations_index():
    """Serve MkDocs documentation index."""
    if not static_docs_path.exists():
        return {"error": "Documentation not built. Run 'uv run build-docs' first."}
    return FileResponse(str(static_docs_path / "index.html"))


if static_docs_path.exists():
    app.mount(
        "/documentations",
        StaticFiles(directory=str(static_docs_path), html=True),
        name="documentations",
    )
