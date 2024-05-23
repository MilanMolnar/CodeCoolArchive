using System;

namespace Exercise16
{
    class Program
    {
        static void Main(string[] args)
        {
            string correctPass = "qwertz1";
            for (int i = 0; i < 3; i++)
            {
                Console.WriteLine("try: " + (Convert.ToInt16(i) + 1));
                Console.Write("Please input your password: ");
                string pass = Console.ReadLine();
                if (pass == correctPass)
                {
                    Console.WriteLine("The password is correct! ");
                    break;
                }
                else
                {
                    Console.WriteLine("The password was incorrect you have: " + (2 - Convert.ToInt16(i)) + " tries left!");
                }
            }
        }
    }
}
