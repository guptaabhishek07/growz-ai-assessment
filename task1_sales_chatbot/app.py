from fastapi import FastAPI
from pydantic import BaseModel
from data_loader import load_sales_data
from llm_interpreter import generate_pandas_code
from safe_executor import safe_execute
from query_router import process_result
from dotenv import load_dotenv
load_dotenv()
from fastapi.responses import FileResponse
from visualization import create_chart


df = load_sales_data()

app = FastAPI(title="Sales Data Chatbot API")

class UserQuery(BaseModel):
    query: str

@app.post("/ask")
def ask_question(payload: UserQuery):
    query = payload.query

    code = generate_pandas_code(query, df.columns.tolist())

    try:
        result = safe_execute(code, df)
    except Exception as e:
        return {"error": str(e), "generated_code": code}

    response = process_result(result)

    return {
        "query": query,
        "generated_code": code,
        "response": response
    }
@app.get("/columns")
def get_columns():
    return {"columns": df.columns.tolist()}

@app.get("/sample")
def get_sample():
    return df.head().to_dict(orient="records")

@app.get("/chart")
def make_chart(x: str, y: str, chart_type: str = "bar"):
    filename = create_chart(df, x, y, chart_type)
    return FileResponse(f"charts/{filename}")

