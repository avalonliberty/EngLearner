## Why

Currently, the API serves Swagger documentation at `/docs` and there's a separate MkDocs setup that requires building static files. Users want a single port experience where both the auto-generated API docs and the custom MkDocs documentation are accessible via different endpoints on the same server.

## What Changes

- Add `/documentations` endpoint to serve MkDocs static documentation
- Keep `/docs` for FastAPI's auto-generated Swagger UI
- Ensure both documentation types are served from the same server (single port)
- Add build step to generate MkDocs static files before serving

## Capabilities

### New Capabilities
- `mkdocs-endpoint`: Serve MkDocs documentation via `/documentations` endpoint on the same FastAPI server

### Modified Capabilities
- None

## Impact

- `src/englearner/main.py`: Add static file serving for documentation
- `pyproject.toml`: Add build-docs script
- `mkdocs.yml`: Already exists, may need adjustments for embedded serving
