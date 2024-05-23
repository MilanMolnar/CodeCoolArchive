using System;
using System.Collections.Generic;
using System.Text;

namespace CsharpCalculator
{
    class Calculator
    {
        public string InputGetter(string prompt)
        {
            Console.Write(prompt);
            string input = Console.ReadLine();
            return input;
        }

        public double Calculte(string op, double x, double y)
        {
            if (op == "+")
            {
                return x + y;
            }
            else if (op == "-")
            {
                return x - y;
            }
            else if (op == "*")
            {
                return x * y;
            }
            else if (op == "/")
            {
                return x / y;
            }
            else
            {
                Console.WriteLine("Invalid operator...");
                throw new Exception("Key Error");
            }
        }

        public void Print(double result)
        {
                Console.WriteLine("The result is: " + result);
        }


    }
}
