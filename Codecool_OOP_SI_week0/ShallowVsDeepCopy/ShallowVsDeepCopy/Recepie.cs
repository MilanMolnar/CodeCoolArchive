using System;
using System.Collections.Generic;
using System.Text;

namespace ShallowVsDeepCopy
{
    class Recipe : ICloneable
    {
        public int Id;
        public string Name;
        public string[] Ingridients;
        
        public Recipe(string name, string[] recipies)
        {
            Random randInt = new Random();
            this.Id = randInt.Next(100,9999);
            this.Name = name;
            this.Ingridients = recipies;

            Console.WriteLine($"{name} is created.");
        }

        public override string ToString()
        {
            string resString = ": ";
            for (int i = 0; i < Ingridients.Length; i++)
            {
                if (i != Ingridients.Length - 1)
                {
                    resString += $"{Ingridients[i]}, ";
                }
                else if (i == Ingridients.Length - 1)
                {
                    resString += $"{Ingridients[i]}";
                }
            }
            return resString;
        }

        public object Clone() //Deep copy
        {
            string[] copiedIngridients = new string[Ingridients.Length];
            for (int i = 0; i < Ingridients.Length; i++)
	    {
                copiedIngridients[i] = Ingridients[i];
	    }
            return new Recipe( this.Name, copiedIngridients);
        }
        public object SClone() //Shallow copy
        {
            return this.MemberwiseClone();
        }
    }
}
