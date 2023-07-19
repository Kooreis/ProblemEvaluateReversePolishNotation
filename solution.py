Here is a Python console application that evaluates an arithmetic expression in Reverse Polish Notation:

```python
def evaluate(expression):
    stack = []
    for token in expression.split(' '):
        if token in ['+', '-', '*', '/']:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            else:
                result = operand1 / operand2
            stack.append(result)
        else:
            stack.append(int(token))
    return stack.pop()

def main():
    expression = input("Enter the Reverse Polish Notation expression: ")
    result = evaluate(expression)
    print("The result is: ", result)

if __name__ == "__main__":
    main()
```

This console application first asks the user to input a Reverse Polish Notation expression. It then evaluates the expression and prints the result. The `evaluate` function uses a stack to keep track of the operands and applies the operators as they appear in the expression.