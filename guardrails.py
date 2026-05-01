import re
from datetime import datetime

blocked_keywords = [
    "ignore", "tell me", "joke", "what is", "explain"
]

def input_guardrail(user_input):
    
    # Rule-based check
    for word in blocked_keywords:
        if word in user_input.lower():
            log_block(user_input, "keyword_block")
            return {"blocked": True, "reason": "Malicious keyword"}

    # Structure check
    pattern = r"sepal_length:.*sepal_width:.*petal_length:.*petal_width:"
    
    if not re.search(pattern, user_input.lower()):
        log_block(user_input, "format_block")
        return {"blocked": True, "reason": "Invalid format"}

    return {"blocked": False}

def log_block(input_text, rule):
    with open("guardrail_logs.txt", "a") as f:
        f.write(f"{datetime.now()} | {rule} | {input_text}\n")


valid_outputs = ["setosa", "versicolor", "virginica"]

def output_guardrail(response):

    # Format violation
    if response.lower() not in valid_outputs:
        log_block(response, "output_violation")
        return "Invalid response blocked"

    # Leakage detection
    if "instruction" in response.lower():
        log_block(response, "leakage_detected")
        return "Sensitive content blocked"

    return response