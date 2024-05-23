using System;

namespace Exercise8
{
    class Program
    {
        static void Main(string[] args)
        {
            int a = 10;
            int b = 11;
            int c = 16;
            Console.WriteLine("If couboid's 'a' edge is 10, 'b' is 11 and 'c' is 16.");
            Console.WriteLine("The couboid's volume is: " + a * b * c);
            Console.WriteLine("The couboid's space diagonal is: " + Math.Sqrt(Math.Pow(a, 2) + Math.Pow(b, 2) + Math.Pow(c, 2)));
            Console.WriteLine("The couboid's surface is :" + 2 * (a * b + a * c + b *c));
            Console.WriteLine("The couboid's 'A' side diagonal is: " + Math.Sqrt(Math.Pow(a, 2) + Math.Pow(b, 2)));
            Console.WriteLine("The couboid's 'B' side diagonal is: " + Math.Sqrt(Math.Pow(a, 2) + Math.Pow(c, 2)));
            Console.WriteLine("The couboid's 'C' side diagonal is: " + Math.Sqrt(Math.Pow(b, 2) + Math.Pow(c, 2)));
        }
    }
}
