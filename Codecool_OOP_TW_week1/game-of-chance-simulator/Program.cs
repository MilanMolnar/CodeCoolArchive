using System;
using System.IO;
using System.Collections.Generic;

namespace GameOfChanceSimulator

{
    class Program
    {
        static ConsoleLogger conslog = new ConsoleLogger();
        static HistoricalDataSet dataSet = new HistoricalDataSet(conslog);
        static void Main(string[] args)
        {
            if (args.Length == 0 || Convert.ToInt32(args[0]) == 0)
            {
                GenerateHistoricalDataSet(0);
            }
            else
            {
                GenerateHistoricalDataSet(Convert.ToInt32(args[0]));
            }
        }
        static HistoricalDataSet GenerateHistoricalDataSet(int argNum)
        {
            if (argNum == 0)
            {
                dataSet.Load();
                conslog.Info("Using previously generated data." + "\n");
                for (int i = 0; i < dataSet.DataPoints.Count; i++)
                {
                    conslog.Info($"{dataSet.DataPoints[i].fighter1} vs {dataSet.DataPoints[i].fighter2}, winner: {dataSet.DataPoints[i].winner}" + "\n");
                }

                var dataEvaulator = new DataEvaluator(dataSet, conslog);
                try //Handling no file exception.
                {
                    var newResult = dataEvaulator.Run();
                    dataEvaulator.Log.Info($"Number of simulations: {newResult.NumberOfSimulations} .\n");
                    dataEvaulator.Log.Info($"The best bet would be {newResult.BestChoice} with the winrate of {newResult.BestChoiceChance * 100:f2}%. \n");
                }
                catch (Exception)
                {

                    dataEvaulator.Log.Error("There is no file called history.csv, please generate a few rounds first!");
                }
                return dataSet;
            }
            else
            {
                dataSet.Load();
                for (int i = 0; i < argNum; i++)
                {
                    dataSet.Generate();
                }

                for (int i = 0; i < dataSet.DataPoints.Count; i++)
                {
                    if (i < dataSet.DataPoints.Count - argNum)
                    {
                        conslog.Info($"{dataSet.DataPoints[i].fighter1} vs {dataSet.DataPoints[i].fighter2}, winner: {dataSet.DataPoints[i].winner}" + "\n");
                    }
                    else
                    {
                        conslog.Info("Generating 1 round of data." + "\n");
                        conslog.Info($"{dataSet.DataPoints[i].fighter1} vs {dataSet.DataPoints[i].fighter2}, winner: {dataSet.DataPoints[i].winner}" + "\n");
                    }

                }

                var dataEvaulator = new DataEvaluator(dataSet, conslog);
                var newResult = dataEvaulator.Run();
                dataEvaulator.Log.Info($"Number of simulations: {newResult.NumberOfSimulations} .\n");
                dataEvaulator.Log.Info($"The best bet would be {newResult.BestChoice} with the winrate of {newResult.BestChoiceChance * 100:f2}%. \n");
                return dataSet;
            }


        }
    }
}
