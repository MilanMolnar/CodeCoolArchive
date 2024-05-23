using System;

namespace Exercise13
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Please input the company's income: ");
            int inc = Convert.ToInt16(Console.ReadLine());
            Console.Write("Please input the company's costs: ");
            int cost = Convert.ToInt16(Console.ReadLine());
            if (inc > cost)
            {
                Console.WriteLine("The company was Profitable");
                Console.Write("The profit was: ");
                Console.WriteLine(inc - cost);
            }
            else if (inc == cost)
            {
                Console.WriteLine("The year was null");
            }
            else
            {
                Console.Write("The company closed the year with a loss of: ");
                Console.WriteLine(cost - inc);
            }
        }
    }
}
