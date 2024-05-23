using System;

namespace Exercise7
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Input two numbers: ");
            double a = Convert.ToDouble(Console.ReadLine());
            double b = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("The number pair's arithmetic mean is: " + (a + b) / 2);
        }
    }
}
