using System;
using System.Collections.Generic;

namespace exercise3
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] triSides = new int[3];
            Console.Write("Please input the triangle's 3 sides: ");
            for (int i = 0; i < 3; i++)
            {
                int temp = Convert.ToInt32(Console.ReadLine());
                triSides[i] = temp;
            }

            if ((triSides[0] + triSides[1]) > triSides[2] && (triSides[0] + triSides[2]) > triSides[1] && (triSides[1] + triSides[2]) > triSides[0])
            {
                Console.WriteLine("Valid triangle.");
            }
            else
            {
                Console.WriteLine("Invalid inputs.");
            }
        }
    }
}
