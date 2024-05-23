namespace VideoExpertSystem
{
    class Program
    {
        static void Main(string[] args)
        {
            bool GoodInput = true;
            while (GoodInput)
            {
                try
                {
                    var es = new ESProvider(new FactParser(), new RuleParser());
                    GoodInput = false;
                }
                catch
                {
                    System.Console.WriteLine("Bad input boy!");
                }
            }
        }
    }
}
