using System;

namespace SiWeek6
{
    class Program
    {
        static void Main(string[] args)
        {
            int radius;
            Console.Write("Please input the radius: ");
            radius = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("The circle's area is: " + 3.14 * Math.Pow(radius, 2));
            Console.WriteLine("The circle's circumference is: " + 2 * radius * 3.14);
            Console.WriteLine("The sphere's surface is: " + 4 * (Math.Pow(radius, 2) * 3.14));
            Console.WriteLine("The sphere's volume is: " + (4 * (Math.Pow(radius, 3) * 3.14) / 3));
        }
    }
}
