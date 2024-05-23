using System;
using System.Collections.Generic;
using System.Text;

namespace cmd
{
    interface ILogger
    {
        void Info(string message);
        void Error(string message);
        void Input(string message);
        void Clear();
    }
}

