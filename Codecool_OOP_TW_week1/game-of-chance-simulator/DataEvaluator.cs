using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;

namespace GameOfChanceSimulator
{
    class DataEvaluator
    {
        public HistoricalDataSet Data { get; }
        public ILogger Log { get; }

        public DataEvaluator(HistoricalDataSet data, ILogger log)
        {
            this.Data = data;
            this.Log = log;
        }

        public Result Run()
        {//Determening best choice and returnin type result obj.
            var numOfSimulation = Data.DataPoints.Count;
            var dictOfWinners = new Dictionary<string, int>();

            for (int i = 0; i < numOfSimulation; i++)
            {
                var winners = Data.DataPoints[i].winner;
                if (!dictOfWinners.ContainsKey(winners))
                {
                    dictOfWinners[winners] = 1;
                }
                else
                {
                    dictOfWinners[winners]++;
                }
            }
            string bestChoice = dictOfWinners.Aggregate((l, r) => l.Value > r.Value ? l : r).Key;
            float bestChoiceChance = (float)dictOfWinners[bestChoice] / (float)numOfSimulation;

            Result result = new Result(numOfSimulation, bestChoice, bestChoiceChance);
            return result;
        }
    }
}
