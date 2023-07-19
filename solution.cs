```C#
using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Enter Reverse Polish Notation expression (separated by space):");
        string input = Console.ReadLine();
        Console.WriteLine("Result: " + EvaluateRPN(input));
    }

    static int EvaluateRPN(string expression)
    {
        string[] tokens = expression.Split(' ');
        Stack<int> stack = new Stack<int>();

        foreach (string token in tokens)
        {
            if (int.TryParse(token, out int number))
            {
                stack.Push(number);
            }
            else
            {
                int operand2 = stack.Pop();
                int operand1 = stack.Pop();

                switch (token)
                {
                    case "+":
                        stack.Push(operand1 + operand2);
                        break;
                    case "-":
                        stack.Push(operand1 - operand2);
                        break;
                    case "*":
                        stack.Push(operand1 * operand2);
                        break;
                    case "/":
                        stack.Push(operand1 / operand2);
                        break;
                    default:
                        throw new ArgumentException("Invalid operator");
                }
            }
        }

        return stack.Pop();
    }
}
```