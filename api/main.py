from fastapi import FastAPI, UploadFile, HTTPException, Depends
from api.schemas import RefineryResponse, ProcessedEntity
from engine.constants import ENGINE_VERSION, SUPPORTED_DOMAINS

app = FastAPI(
    title="Legal Tech Refinery API",
    description="Enterprise-grade data refinery for unstructured legal docs.",
    version=ENGINE_VERSION
)

@app.get("/")
async def root():
    return {"status": "online", "engine": "Refinery-Core", "v": ENGINE_VERSION}

@app.post("/upload", response_model=RefineryResponse)
async def upload_document(file: UploadFile, domain: str):
    # 1. Validation Logic
    if domain.upper() not in SUPPORTED_DOMAINS:
        raise HTTPException(status_code=400, detail=f"Unsupported domain. Choose from: {SUPPORTED_DOMAINS}")

    # 2. Mocking the 'In-Between' Process
    # This represents what Falconx and Fatima will eventually provide
    mock_entities = [
        ProcessedEntity(label="PARTIES", text="State of California vs. Global Corp", confidence=0.98),
        ProcessedEntity(label="DATES", text="2026-04-12", confidence=0.95)
    ]

    # 3. Final Response (Matches our Schema Contract)
    return RefineryResponse(
        file_id="ref-9921",
        filename=file.filename,
        domain=domain.upper(),
        entities=mock_entities,
        status="Success",
        engine_version=ENGINE_VERSION
    )