using System;
using System.Collections.Generic;
using System.Text;

namespace GameOfChanceSimulator
{
    /*
     HistoricalDataPoint encapsulates all state the describes the input and output for a round of game.
     E.g. in a horse race simulator it could store the names of the horses
     that participated in a race and the order that they've finished after the race.
     Note: a HistoricalDataPoint instance should be mappable to a line in history.csv and vica versa.
    */

    class HistoricalDataPoint
    {
        public string DataPoint { get; set; }
        public string fighter1;
        public string fighter2;
        public string winner { get; set; } 

        public HistoricalDataPoint(string[] fightResult)
        {
            this.DataPoint = $"{fightResult[0]},{fightResult[1]},{fightResult[2]}";
            this.fighter1 = fightResult[0];
            this.fighter2 = fightResult[1];
            this.winner = fightResult[2];
        }
        public HistoricalDataPoint(string datapoint)
        {
            this.DataPoint = datapoint;
            string[] fightResult = datapoint.Split(",");
            this.fighter1 = fightResult[0];
            this.fighter2 = fightResult[1];
            this.winner = fightResult[2];
        }
    }
}
