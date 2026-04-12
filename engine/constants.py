# engine/constants.py

# The "Legal Big Five": Standardized entity labels for Sprint 1
# Every module (OCR & NER) must map their output to these keys.
SUPPORTED_ENTITIES = [
    "PARTIES",      # Names of people, companies, or organizations
    "REFERENCE_ID", # Case numbers, contract IDs, or bill references
    "DATES",        # Filing dates, deadlines, or effective dates
    "JURISDICTION", # Courts, states, or specific legal authorities
    "MONETARY_VAL"  # Fines, settlements, interest rates, or contract values
]

# Classification domains to help the engine apply specific logic filters
SUPPORTED_DOMAINS = [
    "CIVIL", 
    "CRIMINAL", 
    "CORPORATE", 
    "FAMILY"
]

# Project Metadata for API reporting
ENGINE_VERSION = "0.1.0-alpha"
TIER_TARGET = 4  # Aiming for 91-99% accuracy