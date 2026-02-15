from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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


if static_docs_path.exists():
    app.mount(
        "/documentations",
        StaticFiles(directory=str(static_docs_path), html=True),
        name="documentations",
    )
