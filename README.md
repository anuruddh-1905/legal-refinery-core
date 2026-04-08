# Legal Tech Data Refinery

## 🎯 Project Vision
To build a high-precision data pipeline for the US legal market, achieving 91-99% accuracy in converting unstructured documents into AI-ready JSONL format.

## 🛠️ Tech Stack (Local-First)
- **Engine**: Python 3.13, Tesseract OCR, spaCy (Transformers), Unstructured.io
- **API**: FastAPI + Uvicorn
- **Database**: Local PostgreSQL
- **Storage**: Local filesystem (`/data/raw`) - **NO AWS usage for now.**

## 📂 Project Structure
- `/engine`: Core processing logic (OCR, NER, PII Masking).
- `/api`: FastAPI endpoints.
- `/data/raw`: Input PDFs (Git-ignored).
- `/data/refined`: Final JSONL outputs.

## 🚀 Getting Started
1. Install Tesseract OCR on your OS.
2. Run `pip install -r requirements.txt`.
3. Create a local `.env` file for your DB credentials.

## 🤝 Coordination Rules
1. **Branching**: `feature/your-task-name`. Never push to `main`.