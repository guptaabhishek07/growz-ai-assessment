import pandas as pd

def process_result(result):
    # 1. If result is a scalar
    if isinstance(result, (int, float, str)):
        return {"type": "text", "value": str(result)}

    # 2. If result is a pandas Series
    if isinstance(result, pd.Series):
        return {"type": "list", "value": result.tolist()}

    # 3. If result is a dataframe
    if isinstance(result, pd.DataFrame):
        return {
            "type": "table",
            "value": result.to_dict(orient="records")
        }

    # 4. If empty
    if result is None or len(result) == 0:
        return {"type": "empty", "value": "No matching results found"}

    return {"type": "unknown", "value": str(result)}
