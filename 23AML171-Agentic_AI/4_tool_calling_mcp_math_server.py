# MCP SERVER FOR EVALUATION OF ARITHMETIC EXPRESSIONS

import ast              # Abstract syntax tree package to be used for safe evaluation of mathematical expressions.
import operator         # Exports a set of functions corresponding to the intrinsic operators of Python such as +, -, ÷ and ×.

from mcp.server.fastmcp import FastMCP      # Provides interfaces to build a light-weight MCP server in Python


# Evaluation is restricted only to arithmetic operators +, -, *, /, ** and parentheses.
ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,     # Unary subtraction (negation) operator to allow for negative numbers in expressions.
}

def eval_math_expression(node: ast.AST) -> float:
    """
    Recursively evaluate an AST node representing a mathematical expression.

    Parameters:
    node (ast.AST): The AST node to evaluate.

    Returns:
    float: The result of the evaluation.
    """
    
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return float(node.value)
    
    if isinstance(node, ast.BinOp) and type(node.op) in ALLOWED_OPERATORS:
        left = eval_math_expression(node.left)
        right = eval_math_expression(node.right)
        return ALLOWED_OPERATORS[type(node.op)](left, right)
    
    if isinstance(node, ast.UnaryOp) and type(node.op) in ALLOWED_OPERATORS:
        operand = eval_math_expression(node.operand)
        return ALLOWED_OPERATORS[type(node.op)](operand)
    
    raise ValueError(f"Unsupported expression: {ast.dump(node)}")

# Initialize an MCP server for math expression evaluation
MATH_MCP = FastMCP(
    name="math-mcp-server",
    host="0.0.0.0",
    port=8001,
    streamable_http_path="/mcp",
    )

@MATH_MCP.tool()
def math(expression: str) -> str:
    """
    Evaluate a basic arithmetic expression safely and return the result.
    
    Parameters:
    expression (str): A string containing the arithmetic expression to evaluate.

    Returns:
    str: The result of the evaluated expression as a string.
    """
    
    allowed_chars = set("0123456789+-*/()^ .")
    if any(ch not in allowed_chars for ch in expression):
        raise ValueError("Unsupported characters in expression.")

    cleaned_expression = expression.replace("^", "**")
    cleaned_expression = cleaned_expression.strip()
    if not cleaned_expression:
        raise ValueError("No arithmetic expression found in input.")
    
    try:
        ast_expression = ast.parse(cleaned_expression, mode="eval").body
        return str(eval_math_expression(ast_expression))
    
    except Exception as e:
        raise ValueError(f"Error parsing expression '{expression}': {e}")


if __name__ == "__main__":
    MATH_MCP.run(transport="streamable-http")     # Runs the MCP server