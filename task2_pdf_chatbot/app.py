from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from pdf_reader import extract_pdf
from data_store import data_store
from llm_answer import answer_question

app = FastAPI(title="PDF Q&A Chatbot API")

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF and extract its text + tables.
    """
    file_path = f"uploaded_{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    text, tables = extract_pdf(file_path)

    data_store.text = text
    data_store.tables = tables

    return {
        "message": "PDF processed successfully.",
        "text_length": len(text),
        "tables_found": len(tables)
    }


@app.post("/ask")
async def ask_question(payload: dict):
    """
    Ask a question based on uploaded PDF content.
    """
    question = payload.get("question", "")

    if not data_store.text:
        return JSONResponse(
            status_code=400,
            content={"error": "No PDF uploaded yet. Upload a PDF using /upload."}
        )

    answer = answer_question(question, data_store.text)

    return {
        "question": question,
        "answer": answer
    }
