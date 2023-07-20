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