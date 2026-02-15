## ADDED Requirements

### Requirement: MkDocs documentation accessible via /documentations endpoint
The system SHALL serve MkDocs-built static documentation at the `/documentations` endpoint on the same FastAPI server.

#### Scenario: Access /documentations returns index page
- **WHEN** user navigates to GET /documentations
- **THEN** system returns the MkDocs index.html with HTTP 200

#### Scenario: Access /documentations/ returns index page
- **WHEN** user navigates to GET /documentations/
- **THEN** system returns the MkDocs index.html with HTTP 200

#### Scenario: Access nested documentation page
- **WHEN** user navigates to GET /documentations/api
- **THEN** system returns the corresponding api.html page with HTTP 200

#### Scenario: Access static assets (CSS/JS)
- **WHEN** user requests /documentations/styles.css or similar static assets
- **THEN** system returns the static file with appropriate content-type

#### Scenario: Swagger UI still accessible at /docs
- **WHEN** user navigates to GET /docs
- **THEN** FastAPI's Swagger UI page is returned with HTTP 200
- **AND** it is independent of /documentations endpoint
