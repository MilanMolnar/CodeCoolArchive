using System;

namespace Exercise19
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Do you want a coffe [y/n]: ");
            string choice = Console.ReadLine();
            bool sugar = false;
            bool glass = false;
            bool cream = false;
            if (choice == "y" || choice == "Y")
            {
                Console.Write("if you want extra sugar input: '1'");
                string sugarInput = Console.ReadLine();
                if (sugarInput == "1")
                {
                    sugar = true;
                }
                Console.Write("if you dont want a disposable cup input: '1'");
                string cupInput = Console.ReadLine();
                if (cupInput == "1")
                {
                    glass = true;
                }
                Console.Write("if you dont want a extra cream input: '1'");
                string creamInput = Console.ReadLine();
                if (creamInput == "1")
                {
                    cream = true;
                }
                int cost = 80;
                if (cream == true)
                {
                    cost += 50;
                }
                if (glass == true)
                {
                    cost -= 10;
                }
                if (sugar == true)
                {
                    cost += 20;
                }

                Console.WriteLine("The coffe cost's: " + cost);
            }
        }
    }
}
