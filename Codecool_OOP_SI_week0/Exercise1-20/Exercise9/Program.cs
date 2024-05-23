using System;

namespace Exercise9
{
    class Program
    {
        static void Main(string[] args)
        {
            int A_sum = 0;
            int B_sum = 0;

            int[] A_cuboid = { 10, 11, 14 };
            int[] B_cuboid = { 12, 16, 12 };
            Array.ForEach(A_cuboid, delegate (int i) { A_sum += i; });
            Array.ForEach(B_cuboid, delegate (int i) { B_sum += i; });
            if (B_sum > A_sum)
            {
                Console.WriteLine("The sum of A_cuboid's edges are lesser.");
                Console.WriteLine("Its voulume: " + A_cuboid[0] * A_cuboid[1] * A_cuboid[2]);
                Console.WriteLine("Its surface area: " + 2 * ((A_cuboid[0] * A_cuboid[1]) + (A_cuboid[0] * A_cuboid[2]) + (A_cuboid[1] * A_cuboid[2])));
            }
            else
            {
                Console.WriteLine("The sum of B_cuboid's edges are lesser.");
                Console.WriteLine("Its voulume: " + B_cuboid[0] * B_cuboid[1] * B_cuboid[2]);
                Console.WriteLine("Its surface area: " + 2 * ((B_cuboid[0] * B_cuboid[1]) + (B_cuboid[0] * B_cuboid[2]) + (B_cuboid[1] * B_cuboid[2])));
            }

        }
    }
}
