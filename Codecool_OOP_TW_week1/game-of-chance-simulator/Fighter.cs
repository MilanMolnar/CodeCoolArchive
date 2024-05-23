using System;
using System.Collections.Generic;
using System.Text;

namespace GameOfChanceSimulator
{
    class Fighter
    {
        //csv header Name,Hp,Dmg,Acc,NoS
        public string Name { get; set; }
        int Hp;
        int Damage;
        int Accuracy;
        int NumOfShots;

        public Fighter(Fighter fighter)
        {
            this.Name = fighter.Name;
            this.Hp = fighter.Hp;
            this.Damage = fighter.Damage;
            this.Accuracy = fighter.Accuracy;
            this.NumOfShots = fighter.NumOfShots;
        }
       
        public Fighter(string dataFromCSV)
        {
            string[] fighterData = dataFromCSV.Split(",");
            this.Name = fighterData[0];
            this.Hp = Convert.ToInt32(fighterData[1]);
            this.Damage = Convert.ToInt32(fighterData[1]);
            this.Accuracy = Convert.ToInt32(fighterData[1]);
            this.NumOfShots = Convert.ToInt32(fighterData[1]);
        }
        private void Attack(Fighter fighter1, Fighter fighter2)
        {//Mini game's Attack logic
            Random random = new Random();
            if (random.Next(1, 101) <= fighter1.Accuracy)
            {
                fighter2.Hp = fighter2.Hp - fighter1.Damage;
            }
            return;
        }

        private bool IsDead(Fighter fighter)
        {//Checking hp must be higher than 0.
            if (fighter.Hp <= 0)
            {
                return true;
            }
            return false;
        }

        public string Fight(Fighter fighter1, Fighter fighter2)
        {//Creating deep copies of fighters.
            var fighterA = new Fighter(fighter1);
            var fighterB = new Fighter(fighter2);
            int gameLen;
            //Fighting logic and determaning round length.
            if (fighterA.NumOfShots >= fighterB.NumOfShots)
            {
                gameLen = fighterA.NumOfShots;
            }
            else
            {
                gameLen = fighterB.NumOfShots;
            }
            for (int i = 0; i < gameLen; i++)
            {
                if (fighter1.NumOfShots >= 1)
                {
                    Attack(fighterA, fighterB);
                    fighterA.NumOfShots--;
                    if (IsDead(fighterB))
                    {
                        return fighterA.Name;
                    }
                }
                if (fighterB.NumOfShots >= 1)
                {
                    Attack(fighterB, fighterA);
                    fighterB.NumOfShots--;
                    if (IsDead(fighterA))
                    {
                        return fighterB.Name;
                    }
                }
            }
            if (fighterA.Hp >= fighterB.Hp)
            {
                return fighterA.Name;
            }
            return fighterB.Name;
        }
    }
}
