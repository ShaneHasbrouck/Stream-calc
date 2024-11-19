import streamlit as st

# Function to perform basic arithmetic operations
def calculate(operation, num1, num2):
    if operation == 'Addition':
        return num1 + num2
    elif operation == 'Subtraction':
        return num1 - num2
    elif operation == 'Multiplication':
        return num1 * num2
    elif operation == 'Division':
        return num1 / num2

# Streamlit app
st.title("Interactive Calculator")

# Input numbers
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Select operation
operation = st.selectbox("Select operation", ['Addition', 'Subtraction', 'Multiplication', 'Division'])

# Calculate result
if st.button("Calculate"):
    result = calculate(operation, num1, num2)
    st.write(f"The result of {operation.lower()} is: {result}")
