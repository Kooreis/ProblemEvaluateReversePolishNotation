Here is a Java console application that evaluates an arithmetic expression in Reverse Polish Notation:

```java
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        String[] tokens = new String[] { "2", "1", "+", "3", "*" };
        System.out.println(evalRPN(tokens));
    }

    public static int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for (String token : tokens) {
            if (!"+-*/".contains(token)) {
                stack.push(Integer.valueOf(token));
                continue;
            }

            int number2 = stack.pop();
            int number1 = stack.pop();
            switch (token) {
                case "+":
                    stack.push(number1 + number2);
                    break;
                case "-":
                    stack.push(number1 - number2);
                    break;
                case "*":
                    stack.push(number1 * number2);
                    break;
                case "/":
                    stack.push(number1 / number2);
                    break;
            }
        }
        return stack.pop();
    }
}
```

This program evaluates the Reverse Polish Notation expression "2 1 + 3 *", which equals 9. The `evalRPN` method uses a stack to keep track of the numbers in the expression. When it encounters an operator, it pops the top two numbers from the stack, performs the operation, and pushes the result back onto the stack. At the end of the expression, the final result is the only number left on the stack.