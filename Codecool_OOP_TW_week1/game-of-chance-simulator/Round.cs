using System;
using System.Collections.Generic;
using System.Text;
using System.IO;

namespace GameOfChanceSimulator
{
    class Round
    {
        public Fighter[] AllFighters { get; private set; }

        public Round()
        {

        }
        public void LoadFighters(string file)
        {
            string[] historialData = System.IO.File.ReadAllLines(file);
            List<Fighter> allFighters = new List<Fighter>();

            foreach (var fighter in historialData)
            {
                var newFighter = new Fighter(fighter);
                allFighters.Add(newFighter);
            }
            this.AllFighters = allFighters.ToArray();

            //Replace the triple loop method with the code above
            /*using (var reader = new StreamReader(file))
            
            {
                List<string> listA = new List<string>();
                List<string[]> listB = new List<string[]>();
                while (!reader.EndOfStream)
                {
                    var line = reader.ReadLine();
                    listA.Add(line);
                }
                Fighter[] allFighters = new Fighter[listA.Count];
                foreach (var item in listA)
                {
                    var values = item.Split(',');
                    listB.Add(values);
                }

                for (int i = 0; i < listB.Count; i++)
                {
                    allFighters[i] = new Fighter(listB[i][0], Int32.Parse(listB[i][1]), Int32.Parse(listB[i][2]), Int32.Parse(listB[i][3]), Int32.Parse(listB[i][4]));
                }
                this.AllFighters = allFighters;
            }*/
        }

        public string[] FightResult()
        {
            Random randomFighter = new Random();
            int fighterA = randomFighter.Next(0, AllFighters.Length);
            int fighterB = randomFighter.Next(0, AllFighters.Length);

            while (fighterA == fighterB)
            {
                fighterB = randomFighter.Next(0, AllFighters.Length);
            }
            string winner = AllFighters[0].Fight(AllFighters[fighterA], AllFighters[fighterB]);
            string[] resultArray = new string[] { AllFighters[fighterA].Name, AllFighters[fighterB].Name, winner };
            return resultArray;
        }
    }
}
