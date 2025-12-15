from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL

client = Groq(api_key=GROQ_API_KEY)

def answer_question(question: str, context: str):
    prompt = f"""
Use ONLY the PDF content below to answer the question.

PDF CONTENT:
----------------------------------------
{context}
----------------------------------------

User Question:
{question}

RULES:
- If answer is not in the PDF, reply: "Information not found in the PDF."
- Be concise and accurate.
"""

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )

    return response.choices[0].message.content.strip()
