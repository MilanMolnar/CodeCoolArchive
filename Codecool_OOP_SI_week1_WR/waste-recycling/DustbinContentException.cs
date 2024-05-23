using System;

namespace WasteRecycling
{
    public class DustbinContentException : Exception
    {
        public DustbinContentException(string message) : base(message)
        {
            Console.WriteLine(message);
        }
    }
}
