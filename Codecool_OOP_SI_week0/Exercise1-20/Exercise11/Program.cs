using System;

namespace Exercise11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Input a number that you want to test: ");
            int num = Convert.ToInt16(Console.ReadLine());
            if (num - 9 * (num / 9) == 0)
            {
                Console.WriteLine("Divisible by 9.");
            }
            else
            {
                Console.WriteLine("Not divisable by 9.");
            }
            //test
            if (num % 9 == 0)
            {
                Console.WriteLine("Test result: Divisable by 9.");
            }
            else
            {
                Console.WriteLine("Test result: Not divisible by 9.");
            }
        }
    }
}
