from guardrails import input_guardrail, output_guardrail

def model_call(user_input):
    # Yahan manually paste karoge (playground se)
    return input("Paste model response: ")

def secure_predict(user_input):
    
    check = input_guardrail(user_input)
    
    if check["blocked"]:
        return check
    
    response = model_call(user_input)
    
    safe_output = output_guardrail(response)
    
    return safe_output


# Test
user_input = input("Enter input: ")
print(secure_predict(user_input))
