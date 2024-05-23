using System;
using System.Collections.Generic;
using System.Text;

namespace cmd
{
    //ConsoleLogger formázza a kiírt üzeneteket
    class ConsoleLogger : ILogger
    {
        public ConsoleLogger() { }
        public void Info(string message)
        {
            Console.ForegroundColor = ConsoleColor.Blue;
            Console.Write("INFO: ");
            Console.ResetColor();
            Console.Write(DateTime.Now.ToString("yyyy-mm-ddThh:mm:ss: "));
            Console.WriteLine(message);
        }
        public void Error(string message)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.Write("Error: ");
            Console.ResetColor();
            Console.Write(DateTime.Now.ToString("yyyy-mm-ddThh:mm:ss: "));
            Console.WriteLine(message);
        }
        public void Input(string message)
        {
            Console.ForegroundColor = ConsoleColor.Green;
            Console.Write("Input ");
            Console.ResetColor();
            Console.Write(message);
        }
        public void Clear()
        {
            Console.Clear();
        }
    }
}
