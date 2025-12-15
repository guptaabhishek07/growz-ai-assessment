import os
from dotenv import load_dotenv

load_dotenv()

# Groq Model (fast + accurate for code generation)
GROQ_MODEL = "meta-llama/llama-4-maverick-17b-128e-instruct"
# Alternatives:
# GROQ_MODEL = "mixtral-8x7b-32768"
# GROQ_MODEL = "llama3-8b-8192"

# Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

SYSTEM_PROMPT = """
You are a data analysis assistant. Your job is to convert natural language questions
into Python pandas code to query a dataframe named df.

Rules:
1. Only output Python code, no explanations.
2. Do not assign variables; only return expressions (like df[...] or df.groupby(...)).
3. Use pandas filtering, grouping, sum(), mean(), etc.
4. Columns available will be provided dynamically.
5. If asked to plot, generate Python code that returns a dataframe for plotting, not the chart.
6. NEVER use print(), only return a pandas expression as output.
"""
