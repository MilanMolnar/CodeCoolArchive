using System;

namespace ShallowVsDeepCopy
{
    class Program
    {
        static void Main(string[] args)
        {
            Recipe husleves = new Recipe("husleves",  new string[] { "hus", "leves" });
            Recipe krumplisTeszta = new Recipe("krumplisteszta", new string[] { "krumpli", "teszta" });
            Recipe garnelsaRizotto = new Recipe("garnelsa rizotto", new string[] { "garnela", "rizs" });
            Recipe salata = new Recipe("salata", new string[] { "salata", "dressing" });
            Recipe sajtTorta = new Recipe("sajttorta", new string[] { "mascarpone", "kex" });


            Recipe huslevesClone = (Recipe)husleves.Clone();
            huslevesClone.Name = "Husosabb leves";
            huslevesClone.Ingridients[1] = "rengeteg husika";

            Recipe salataClone = (Recipe)salata.Clone();
            salataClone.Id = 6969;

            Recipe sajtTortaClone = (Recipe)sajtTorta.Clone();
            sajtTortaClone.Name = "Royal sajttorta";
            sajtTortaClone.Ingridients[0] = "keksajt";
            Console.WriteLine();
            Console.WriteLine("ID: " + husleves.Id + " " + husleves.Name + ", ingridients: " + husleves);
            Console.WriteLine("ID: " + krumplisTeszta.Id + " " + krumplisTeszta.Name + ", ingridients: " + krumplisTeszta);
            Console.WriteLine("ID: " + garnelsaRizotto.Id + " " + garnelsaRizotto.Name + ", ingridients: " + garnelsaRizotto);
            Console.WriteLine("ID: " + salata.Id + " " + salata.Name + ", ingridients: " + salata);
            Console.WriteLine("ID: " + sajtTorta.Id + " " + sajtTorta.Name + ", ingridients: " + sajtTorta);

            Console.WriteLine("==================After cloning================");
            Console.WriteLine("ID: " + huslevesClone.Id + " " + huslevesClone.Name + ", ingridients: " + huslevesClone);
            Console.WriteLine("ID: " + salataClone.Id + " " + salataClone.Name + ", ingridients: " + salataClone);
            Console.WriteLine("ID: " + sajtTortaClone.Id + " " + sajtTortaClone.Name + ", ingridients: " + sajtTortaClone);
            Console.ReadLine();


        }
    }
}
