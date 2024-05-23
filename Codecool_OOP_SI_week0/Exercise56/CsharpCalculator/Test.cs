using System;
using System.Collections.Generic;
using System.Text;

namespace CsharpCalculator
{
    class Test
    {
        public void Tester()
        {
            Calculator calculator = new Calculator();
            double res1 = calculator.Calculte("+", 2, 2);
            double res2 = calculator.Calculte("*", 2, 4);
            double res3 = calculator.Calculte("-", 3, 2);
            double res4 = calculator.Calculte("/", 4, 4);

            if (res1 == 4 && res2 == 8 && res3 == 1 && res4 == 1)
            {
                Console.WriteLine("Test 4/4 Pass...");
            }
            else
            {
                Console.WriteLine("Opps something went wrong...");
            }
        }
    }
}
