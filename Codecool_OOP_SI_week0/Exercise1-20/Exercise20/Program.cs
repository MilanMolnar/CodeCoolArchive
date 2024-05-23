using System;

namespace Exercise20
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("The program writes the least possible coins in descending order[10, 5, 2, 1].");
            Console.Write("Input an amount: ");
            int amount = Convert.ToInt32(Console.ReadLine());
            int[] arr = new int[4] {10, 5, 2, 1 };
            for (int i = 0; i < 4; i++)
            {
                while (amount >= arr[i])
                {
                    amount = amount - arr[i];
                    Console.WriteLine(arr[i]);
                }
            }
            
        }
    }
    
}
