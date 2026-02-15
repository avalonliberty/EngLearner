## Context

The API currently serves Swagger UI at `/docs`. The project also has MkDocs for custom documentation, but it requires running on a separate port. Users want both documentation types accessible via different endpoints on the same server.

## Goals / Non-Goals

**Goals:**
- Serve MkDocs static documentation at `/documentations` endpoint
- Keep FastAPI's Swagger UI at `/docs` (no changes)
- Single server, single port experience for all documentation

**Non-Goals:**
- Modify existing API endpoints
- Change documentation content
- Add authentication to documentation endpoints

## Decisions

### Decision 1: Static File Serving

Using FastAPI's `StaticFiles` to serve MkDocs-built static files:
- Built-in FastAPI support
- No additional dependencies
- Simple to implement

```
/documentations     → MkDocs static files (HTML, CSS, JS)
/docs              → FastAPI Swagger UI (auto-generated)
```

### Decision 2: Build Process

Adding MkDocs build to the startup process:
- Pre-build static files before server starts
- Use `python-multipart` or subprocess to build
- Store built files in `static_docs/` directory

### Decision 3: HTML5 Mode for MkDocs

Configuring MkDocs for SPA-style routing:
- Enable `strict_mode` to avoid 404 on refresh
- Serve `index.html` for all non-file paths
- This ensures deep links work correctly

## Risks / Trade-offs

- **[Risk] Build dependency** → Server won't start if mkdocs build fails; show clear error message
- **[Risk] Large static files** → Static docs can be large; consider gzip in production
- **[Risk] Port conflict** → `/documentations` and `/docs` could conflict; use different mount points
