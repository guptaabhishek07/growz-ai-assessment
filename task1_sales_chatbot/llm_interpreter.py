from groq import Groq
from config import SYSTEM_PROMPT, GROQ_MODEL, GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def generate_pandas_code(query: str, columns: list):
    # We KNOW your dataset only has these two columns:
    # ["Header Name", "Explanation"]
    prompt = f"""
You are an expert assistant. The dataframe ALWAYS has exactly these two columns:

1. Header Name  (text)
2. Explanation   (text)

Your job:
Generate VALID pandas code that returns relevant rows from df.

Rules:
- ALWAYS filter using df['Header Name'] only
- NEVER use df['Explanation'] for filtering
- NEVER use sum(), mean(), groupby(), or any math functions (data is NOT numeric)
- ALWAYS return a filtered dataframe, NOT a number
- ALWAYS use df[...] format without assigning variables
- Use .str.contains("...", case=False) for matching
- If user asks for "show dataset", return simply: df
- If user asks for columns, return: df.columns
- Do NOT hallucinate new column names
- Return ONLY executable pandas code

User query:
{query}
"""


    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )

    code = response.choices[0].message.content
    return code.strip()
