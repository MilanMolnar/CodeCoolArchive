using System;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] listOfInputs = new int[3];
            Console.WriteLine("Please input 3 numbers to sort in descending order: ");
            for (int i = 0; i < 3; i++)
            {
                int temp = Convert.ToInt32(Console.ReadLine());
                listOfInputs[i] = temp;
            }
            Array.Sort(listOfInputs);
            Array.Reverse(listOfInputs);
            Console.WriteLine("The list of inputs in descending order are as follows: ");
            Array.ForEach(listOfInputs, Console.WriteLine);
        }
    }
}
