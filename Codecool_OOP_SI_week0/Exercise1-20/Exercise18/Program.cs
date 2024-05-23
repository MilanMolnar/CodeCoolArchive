using System;

namespace Exercise18
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] meanTemps = new int[12];
            for (int i = 0; i < 12; i++)
            {
                Console.Write("Input the mean temperature of the " + (Convert.ToInt32(i) + 1) + ". month: ");
                meanTemps[i] = Convert.ToInt32(Console.ReadLine());
            }
            int sum = 0;
            for (int i = 0; i < meanTemps.Length; i++)
            {
                sum += meanTemps[i];
            }
            Console.WriteLine("This year's mean temprature is: " + (sum / 12));
        }
    }
}
