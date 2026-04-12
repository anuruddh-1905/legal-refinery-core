from pydantic import BaseModel, Field
from typing import List, Optional
from engine.constants import SUPPORTED_ENTITIES, SUPPORTED_DOMAINS

class ProcessedEntity(BaseModel):
    # This ensures the 'label' is one of our "Legal Big Five"
    label: str = Field(..., description=f"Must be one of: {SUPPORTED_ENTITIES}")
    text: str
    confidence: float = Field(..., ge=0, le=1) # Must be between 0.0 and 1.0

class RefineryResponse(BaseModel):
    file_id: str
    filename: str
    # Ensures the domain is one of our 4 supported types
    domain: str = Field(..., description=f"Must be one of: {SUPPORTED_DOMAINS}")
    entities: List[ProcessedEntity]
    status: str = "Success"
    engine_version: str = "0.1.0-alpha"