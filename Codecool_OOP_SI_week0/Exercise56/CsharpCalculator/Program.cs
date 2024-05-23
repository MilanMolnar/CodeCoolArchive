using System;

namespace CsharpCalculator
{
    class Program
    {
        static void Main(string[] args)
        {
            Calculator calculator = new Calculator();
            Test tester = new Test();
            tester.Tester();
            Console.WriteLine("Use of calculator, input a number than an operator[+, -, *, /] than an other number.");
            double x = Convert.ToDouble(calculator.InputGetter("Input a number: "));
            string op = calculator.InputGetter("Input an operator: ");
            double y = Convert.ToDouble(calculator.InputGetter("Input another number: "));
            calculator.Print(calculator.Calculte(op,x,y));
            

        }
    }
}
