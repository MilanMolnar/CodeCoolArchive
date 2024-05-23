using System;
using System.Collections.Generic;
using System.Text;

namespace GameOfChanceSimulator
{
    class ConsoleLogger : ILogger
    {

        public ConsoleLogger()
        {

        }
        public void Info(string message)
        {
            //Formating console logger
            Console.ForegroundColor = ConsoleColor.Blue;
            Console.Write("INFO: ");
            Console.ResetColor();
            Console.Write(DateTime.Now.ToString("yyyy-mm-ddThh:mm:ss: "));
            Console.Write(message);
            
        }
        public void Error(string message)
        {
            //Formating console logger
            Console.ForegroundColor = ConsoleColor.Red;
            Console.Write("Error: ");
            Console.ResetColor();
            Console.Write(DateTime.Now.ToString("yyyy-mm-ddThh:mm:ss: "));
            Console.Write(message);
        }
    }
}
