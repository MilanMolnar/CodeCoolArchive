using System;
using System.Collections.Generic;
using System.Text;
using cmd;


namespace api
{
    class Program
    {
        private static int index = 0;

        private static void Main(string[] args)
        {
            ConsoleLogger cl = new ConsoleLogger();
            DataManager dm = new DataManager();

            //Menü elemeinek listája
            List<string> menuItems = new List<string>() 
               {"ADD CUSTOMER",
                "REMOVE CUSTOMER",
                "DISPLAY CUSTOMER INFORMATION",
                "DISPLAY ALL CUSTOMERS",
                "SAVE TO XML",
                "ADD TO CART",
                "EMPTY CART WITH CUSTOMER WITH CUSTOMER",
                "EXIT"};

            //A kurzor eltüntetése a menü kiiratásnál
            Console.CursorVisible = false;

            //Menü ciklus
            while (true)
            {
                string selectedMenuItem = drawMenu(menuItems);
                if (selectedMenuItem == "ADD CUSTOMER")
                {
                    Console.CursorVisible = true;
                    FIleHandler.GetData();
                    dm.GetAddUserInput();
                    cl.Input("Press any button to continue...");
                    Console.ReadLine();
                    cl.Clear();
                    Console.CursorVisible = false;
                }
                else if (selectedMenuItem == "REMOVE CUSTOMER")
                {
                    Console.CursorVisible = true;
                    FIleHandler.GetData();
                    FIleHandler.RemoveCustomerByID(dm.GetIndexByID());
                    cl.Input("Press any button to continue...");
                    Console.ReadLine();
                    cl.Clear();
                    Console.CursorVisible = false;
                }
                else if (selectedMenuItem == "SAVE TO XML")
                {
                    FIleHandler.GetData();
                    FIleHandler.SaveToXML();
                    cl.Input("Press any button to continue...");
                    Console.ReadLine();
                    cl.Clear();
                }
                else if (selectedMenuItem == "EMPTY CART WITH CUSTOMER WITH CUSTOMER")
                {
                    FIleHandler.GetData();
                    dm.EmptyCartByCustomer();
                    cl.Input("Press any button to continue...");
                    Console.ReadLine();
                    cl.Clear();
                }
                else if (selectedMenuItem == "DISPLAY CUSTOMER INFORMATION")
                {
                    Console.CursorVisible = true;
                    FIleHandler.GetData();
                    int userIndex;
                    while (true)
                    {
                        try
                        {
                            userIndex = dm.GetIndexByID();
                        }
                        catch (NotValidIDException)
                        {
                            cl.Error("Invalid ID.");
                            continue;
                        }
                        break;
                    }
                    Console.WriteLine(FIleHandler.valuedCustomers[userIndex].ToString());
                    cl.Input("Press any button to continue...");
                    Console.ReadLine();
                    cl.Clear();
                    Console.CursorVisible = false;
                }
                else if (selectedMenuItem == "DISPLAY ALL CUSTOMERS")
                {
                    FIleHandler.GetData();
                    dm.DrawAllCustomer();
                    cl.Input("Press any button to continue...");
                    Console.ReadLine();
                    cl.Clear();
                }
                else if (selectedMenuItem == "ADD TO CART")
                {
                    Console.CursorVisible = true;
                    FIleHandler.GetData();
                    dm.IncreaseCurrentSpendingByID();
                    cl.Input("Press any button to continue...");
                    FIleHandler.UpdateFileByFile();
                    Console.ReadLine();
                    cl.Clear();
                    Console.CursorVisible = false;
                }
                else if (selectedMenuItem == "EXIT")
                {
                    FIleHandler.GetData();
                    dm.ResetCurrentSpendings();
                    Environment.Exit(0);
                }
            }
        }
        //Menü kirajzolásáért felelős függvény
        private static string drawMenu(List<string> items)
        {
            Console.WriteLine("\n\n\n\n");
            for (int i = 0; i < items.Count; i++)
            {
                if (i == index)
                {
                    Console.Write(" ");
                    Console.BackgroundColor = ConsoleColor.Gray;
                    Console.ForegroundColor = ConsoleColor.Black;
                    Console.Write(">");//"\u261E"
                    Console.BackgroundColor = ConsoleColor.Black;
                    Console.ForegroundColor = ConsoleColor.Gray;

                    Console.Write("      ");
                    Console.BackgroundColor = ConsoleColor.Gray;
                    Console.ForegroundColor = ConsoleColor.Black;
                    Console.WriteLine(items[i]);
                }
                else
                {
                    Console.WriteLine($"      {items[i]}");
                }
                Console.ResetColor();
            }

            ConsoleKeyInfo ckey = Console.ReadKey();

            if (ckey.Key == ConsoleKey.DownArrow)
            {
                if (index == items.Count - 1)
                {
                    index = 0; //Az elejére ugrik
                }
                else { index++; }
            }
            else if (ckey.Key == ConsoleKey.UpArrow)
            {
                if (index <= 0)
                {
                    index = items.Count - 1;  //A végére ugrik
                }
                else { index--; }
            }
            else if (ckey.Key == ConsoleKey.Enter)
            {
                return items[index];
            }
            else
            {
                return "";
            }

            Console.Clear();
            return "";
        }
    }
}
