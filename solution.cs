static void Main(string[] args)
{
Console.WriteLine("Enter Reverse Polish Notation expression (separated by space):");
string input = Console.ReadLine();
Console.WriteLine("Result: " + EvaluateRPN(input));
}