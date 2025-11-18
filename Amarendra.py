
def simple_calculator(expression_str):
    """
    Performs a simple calculation (+, -, *, /) based on a string input 
    like "5 + 3". It requires exactly two numbers and one operator.
    """
    
   
    print(f"Input Expression: **{expression_str}**")
    
    
    elements = expression_str.split()
    
    
    if len(elements) != 3:
        return "**Error:** Invalid format. Please use 'number operator number' (e.g., '5 + 3')."
    
    
    num1_str, operator, num2_str = elements[0], elements[1], elements[2]
    
    
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        return "**Error:** Invalid number input."

    
    valid_operators = ('+', '-', '*', '/')
    
    if operator not in valid_operators:
        return f"**Error:** Invalid operator. Use one of {valid_operators}."

    
    result = None
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
       
        if num2 == 0:
            return "**Error:** Cannot divide by zero."
        result = num1 / num2
    
    return result



print("\n--- Example 1 (Addition) ---")

input_add = "15.5 + 4.5" 
output_add = simple_calculator(input_add)
print(f"Result: {output_add}")

print("\n--- Example 2 (Multiplication) ---")

input_mul = "7 * 6" 
output_mul = simple_calculator(input_mul)
print(f"Result: {output_mul}")

print("\n--- Example 3 (Error Handling - Invalid Operator) ---")

input_invalid = "10 ^ 2" 
output_invalid = simple_calculator(input_invalid)
print(f"Result: {output_invalid}")
