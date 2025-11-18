# Function to perform the calculation
def simple_calculator(expression_str):
    """
    Performs a simple calculation (+, -, *, /) based on a string input 
    like "5 + 3". It requires exactly two numbers and one operator.
    """
    
    # --- 1. Use a String for Input ---
    # The 'expression_str' is the string input (e.g., "10 * 5")
    print(f"Input Expression: **{expression_str}**")
    
    # --- 2. Use a List for Parsing ---
    # Split the string by spaces to get a list of elements
    # Example: "10 * 5" -> ['10', '*', '5']
    elements = expression_str.split()
    
    # Basic input validation: Check if we have three elements (num, op, num)
    if len(elements) != 3:
        return "**Error:** Invalid format. Please use 'number operator number' (e.g., '5 + 3')."
    
    # Assign elements from the list
    num1_str, operator, num2_str = elements[0], elements[1], elements[2]
    
    # Convert number strings to float for calculation
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        return "**Error:** Invalid number input."

    # --- 3. Use a Tuple for Storing Valid Operations ---
    # A tuple is used here because the set of valid operators is constant.
    valid_operators = ('+', '-', '*', '/')
    
    if operator not in valid_operators:
        return f"**Error:** Invalid operator. Use one of {valid_operators}."

    # Perform the calculation
    result = None
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        # Handle division by zero
        if num2 == 0:
            return "**Error:** Cannot divide by zero."
        result = num1 / num2
    
    return result

# --- Examples ---

print("\n--- Example 1 (Addition) ---")
# String input
input_add = "15.5 + 4.5" 
output_add = simple_calculator(input_add)
print(f"Result: {output_add}")

print("\n--- Example 2 (Multiplication) ---")
# String input
input_mul = "7 * 6" 
output_mul = simple_calculator(input_mul)
print(f"Result: {output_mul}")

print("\n--- Example 3 (Error Handling - Invalid Operator) ---")
# String input
input_invalid = "10 ^ 2" 
output_invalid = simple_calculator(input_invalid)
print(f"Result: {output_invalid}")
