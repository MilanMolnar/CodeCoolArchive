using System;

namespace Exercise15
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Do you speak Hungary/French/Russia/Spanish if you do please chose one and write it down, and if not just press enter.");
            Console.Write("Your input: ");
            string language = Console.ReadLine();
            string hearth = "\u2665";
            if (language == "Hungary")
            {
                Console.WriteLine("Köszönöm!");
            }
            else if (language == "French")
            {
                Console.WriteLine("Merci!");
            }
            else if (language == "Russia")
            {
                Console.WriteLine("Cпасибо!");
            }
            else if (language == "Spanish")
            {
                Console.WriteLine("Gracias!");
            }
            else if (language == "")
            {
                Console.WriteLine(hearth);
            }
        }
    }
}
