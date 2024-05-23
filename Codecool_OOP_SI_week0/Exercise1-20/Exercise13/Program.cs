using System;

namespace Exercise12
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Input a number that coorelates with a month: ");
            int month = Convert.ToInt32(Console.ReadLine());
            if (4 > month && month > 0)
            {
                Console.WriteLine("Spring");
            }
            else if (month > 3 && 7 > month)
            {
                Console.WriteLine("Summer");
            }
            else if (month > 6 && 10 > month)
            {
                Console.WriteLine("Fall");
            }
            else if (month > 9 && 13 > month)
            {
                Console.WriteLine("Winter");
            }
        }
    }
}
