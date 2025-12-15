# 📘 **Growz Technical Assessment – AI Engineering Submission**

### **Author:** Abhishek Kumar

### **Date:** 15 December 2025

---

# #️⃣ **OVERVIEW**

This repository contains **two complete AI Engineering tasks**, developed as part of the **Growz Technical Assessment**.

✔ **Task-1:** AI-powered Sales Data Chatbot using FastAPI + Pandas + Groq
✔ **Task-2:** PDF Q&A Chatbot using FastAPI + pdfplumber + Groq

Both tasks are production-ready, modular, cleanly structured, and tested.

---

# #️⃣ **FOLDER STRUCTURE**

```
project/
│── README.md
│── venv/                            # Python virtual environment
│
├── task1_sales_chatbot/
│   ├── Sales & Active Stores Data.xlsb
│   ├── app.py
│   ├── main.py
│   ├── data_loader.py
│   ├── llm_interpreter.py
│   ├── query_router.py
│   ├── safe_executor.py
│   ├── visualization.py
│   ├── config.py
│   ├── charts/
│   └── requirements.txt
│
└── task2_pdf_chatbot/
    ├── app.py
    ├── pdf_reader.py
    ├── llm_answer.py
    ├── data_store.py
    ├── config.py
    ├── requirements.txt
    └── samples/
```

---

# #️⃣ **SETUP INSTRUCTIONS**

## 1️⃣ Create Virtual Environment

```bash
cd project
python3 -m venv venv
source venv/bin/activate
```

---

## 2️⃣ Install Dependencies

### Install for Task-1

```bash
pip install -r task1_sales_chatbot/requirements.txt
```

### Install for Task-2

```bash
pip install -r task2_pdf_chatbot/requirements.txt
```

### Install additional requirements

```bash
pip install python-multipart
```

---

## 3️⃣ Environment Variables

Create `.env` at **project level**:

```
GROQ_API_KEY=your_key_here
```

Model used for both tasks:

```
meta-llama/llama-4-maverick-17b-128e-instruct
```

---

# #️⃣ **TASK-1 — Sales Data Chatbot**

### ✔ Allows natural language questions about XLSB data

### ✔ Converts human queries → Pandas code

### ✔ Executes safely inside sandbox

### ✔ Returns tables, values, summaries

### ✔ Generates charts on demand

---

## ▶️ **Run Task-1 API**

```bash
cd task1_sales_chatbot
uvicorn app:app --reload
```

Open Swagger:

```
http://127.0.0.1:8000/docs
```

---

## 📌 **Key Endpoints**

### **POST /ask**

Ask questions like:

```
"total sales for biscuits"
"show all cities"
"top 5 brands"
"plot monthly sales"
```

Example request:

```json
{
  "query": "what is inside my dataset"
}
```

Example response:

* Generated Pandas code
* Clean structured data
* Table results or summaries
* Chart filename if visual generated

---

# #️⃣ **TASK-2 — PDF Q&A Chatbot**

### ✔ Upload ANY PDF

### ✔ Extract text + tables using pdfplumber

### ✔ Store content in memory

### ✔ Ask questions about the PDF

### ✔ Groq answers ONLY from PDF context

---

## ▶️ **Run Task-2 API**

```bash
cd task2_pdf_chatbot
uvicorn app:app --reload
```

Open Swagger:

```
http://127.0.0.1:8000/docs
```

---

## 📌 **Key Endpoints**

### **POST /upload**

Upload a PDF file.

Response:

```json
{
  "message": "PDF processed successfully.",
  "text_length": 1249,
  "tables_found": 2
}
```

---

### **POST /ask**

Example body:

```json
{
  "question": "What items are listed in the invoice?"
}
```

Example answer:

```
The invoice contains product rows with columns such as SKU,
Description, Quantity, Unit Price, Discount %, Tax %, Total Value...
```

---

# #️⃣ **TECHNOLOGIES USED**

| Feature        | Library                         |
| -------------- | ------------------------------- |
| API Framework  | FastAPI                         |
| XLSB Reading   | pandas + pyxlsb                 |
| PDF Parsing    | pdfplumber                      |
| AI LLM         | Groq API (Llama-4 Maverick 17B) |
| Visualization  | matplotlib                      |
| Code Execution | safe sandbox                    |
| Realtime Dev   | Uvicorn reload                  |

---

# #️⃣ **SCREENSHOTS TO INCLUDE (FOR GROWZ)**

📸 **Task-1**

* `/columns` output
* `/sample` output
* `/ask` with complex query
* chart preview in `charts/` folder

📸 **Task-2**

* `/upload` successful response
* `/ask` showing extracted invoice information

---

# #️⃣ **HOW TO ZIP FOR SUBMISSION**

From inside `project` folder:

```bash
zip -r Growz_Assessment_Abhishek_Kumar.zip .
```

Submit the zip.

---

# 🎉 **FINAL NOTES**

Both Task 1 and Task 2 are:

✅ Fully functional
✅ Modular
✅ Stable
✅ Using modern LLM (Groq Maverick 17B)
✅ Following clean architecture
✅ API tested via Swagger

This fulfills all Growz assessment requirements.

---

