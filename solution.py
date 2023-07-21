def main():
    expression = input("Enter the Reverse Polish Notation expression: ")
    result = evaluate(expression)
    print("The result is: ", result)