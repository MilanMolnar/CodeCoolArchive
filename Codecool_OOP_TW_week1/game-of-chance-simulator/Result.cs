using System;
using System.Collections.Generic;
using System.Text;

namespace GameOfChanceSimulator
{
    class Result
    {//Creating result objects template
        public int NumberOfSimulations { get; private set; }
        public string BestChoice { get; private set; }
        public float BestChoiceChance { get; private set; }

        public Result(int num, string name, float percent)
        {
            NumberOfSimulations = num;
            BestChoice = name;
            BestChoiceChance = percent;
        }
    }
}
