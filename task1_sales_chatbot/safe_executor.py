import ast

ALLOWED_NAMES = {
    "df": None
}

class SafeExecutor(ast.NodeVisitor):
    def visit_Attribute(self, node):
        return self.generic_visit(node)

    def visit_Call(self, node):
        return self.generic_visit(node)

    def visit_Name(self, node):
        if node.id not in ALLOWED_NAMES:
            raise ValueError(f"Unauthorized name used: {node.id}")

def safe_execute(code: str, df):
    allowed_globals = {"df": df}

    try:
        result = eval(code, allowed_globals, {})
        return result

    except Exception as e:
        raise Exception(f"Execution failed: {str(e)}\nGenerated code: {code}")

