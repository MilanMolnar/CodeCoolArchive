using System;
using System.Collections.Generic;
using System.Text;
using System.IO;

namespace GameOfChanceSimulator
{
    class HistoricalDataSet
    {
        static Round round = new Round();


        public int Size { get; private set; }
        public string FighterCollection;
        private List<HistoricalDataPoint> _DataPoints = new List<HistoricalDataPoint>();
        public IReadOnlyList<HistoricalDataPoint> DataPoints { get { return _DataPoints.AsReadOnly(); } }
        internal void AddDatapoint(HistoricalDataPoint dataPoint)
        {
            _DataPoints.Add(dataPoint);
        }
        public HistoricalDataSet(ILogger log)
        {
            round.LoadFighters("Fighters.csv");
            GetAllFighters();
            log.Info($"Fighters:  {FighterCollection}\n");
        }

        public void Generate()
        {
            HistoricalDataPoint dataPoint = new HistoricalDataPoint(round.FightResult());
            AddDatapoint(dataPoint);
            this.Size++;

            string history = "history.csv";

            File.AppendAllText(history, dataPoint.DataPoint + "\n");


        }
        public void Load()
        {
            string file = "history.csv";
            if (File.Exists(file))
            {
                string[] historialData = System.IO.File.ReadAllLines(file);
                foreach (var item in historialData)
                {
                    HistoricalDataPoint nextDataPoint = new HistoricalDataPoint(item);
                    AddDatapoint(nextDataPoint);
                    this.Size++;
                }
            }
            else
            {
                var myFile = File.Create(file);
                myFile.Close();
            }

        }
        public void GetAllFighters()
        {
            for (int i = 0; i < round.AllFighters.Length; i++)
            {
                if (i == 0)
                {
                    this.FighterCollection += (round.AllFighters[i].Name);
                }
                else
                {
                    this.FighterCollection += ", " + (round.AllFighters[i].Name);
                }
            }
        }
    }
}
