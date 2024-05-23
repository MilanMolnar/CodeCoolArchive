using System;
using System.Collections.Generic;
using System.Text;
using System.Text.RegularExpressions;
using ConsoleTables;
using cmd;

namespace api
{
    class DataManager
    {
        //Megkeresi a felhasználó indexét a memóriába betöltött listából a felhasználó álltal megadott ID alapján
        public  int GetIndexByID()
        {
            ConsoleLogger cl = new ConsoleLogger();
            List<ValuedCustomer> valuedCustomers = FIleHandler.valuedCustomers;
            //A felhasználó által megadott ID
            string enteredID = "";

            while (true)
            {
                var customerIndex = 0;
                cl.Input("User ID: ");
                enteredID = Console.ReadLine();

                foreach (var id in valuedCustomers)
                {
                    if (id.CustomerID == enteredID)
                    {
                        return customerIndex;
                    }
                    else
                    {
                        customerIndex++;
                    }
                }

                throw new NotValidIDException();
            }
        }

        //A FileHandler-ben megirt logikát használva hozzáadja az uj vásárlót a listához
        public  void GetAddUserInput()
        {
            ConsoleLogger cl = new ConsoleLogger();
            string name = "";
            string address = "";
            string phone = "";
            string email = "";
            string onlist = "";
            string temp;

            for (int i = 0; i < 5; i++)
            {
                if (i == 0)
                {
                    cl.Input("Customer's Name: ");
                    name = Console.ReadLine();
                }
                else if (i == 1)
                {
                    cl.Input("Customer's Address: ");
                    address = Console.ReadLine();
                }
                else if (i == 2)
                {
                    cl.Input("Customer's Phone number: ");
                    temp = Console.ReadLine();
                    while (!Regex.Match(temp, @"([0-9])").Success)
                    {
                        cl.Error("Invalid telephone number format!");
                        cl.Input("Customer's Phone number: ");
                        temp = Console.ReadLine();
                    }
                    phone = temp; 
                }
                else if (i == 3)
                {
                    cl.Input("Customer's Email address: ");
                    temp = Console.ReadLine();
                    bool IsValidEmail(string email)
                    {
                        try
                        {
                            var addr = new System.Net.Mail.MailAddress(email);
                            return addr.Address == email;
                        }
                        catch
                        {
                            return false;
                        }
                    }
                    while (!IsValidEmail(temp))
                    {
                        cl.Error("Invalid e-mail format!");
                        cl.Input("Customer's Email address: ");
                        temp = Console.ReadLine();
                    }
                    email = temp;

                }
                else if (i == 4)
                {
                    while (true)
                    {
                        cl.Input("If customer wants to be on our email list (true/false): ");
                        onlist = Console.ReadLine();
                        if (onlist == "true" || onlist == "false")
                        {
                            Convert.ToBoolean(onlist);
                            break;
                        }
                        else
                        {
                            cl.Error("Wrong input!");

                        }
                    }      
                }
            }
            FIleHandler.AddCustomer(name, address, phone, email, onlist);
        }

        //Hozzá adja a felhasználó álltal kiválasztott vásárlóhoz jelenlegi költségeihez az elköltött mennyiséget.   
        public  void IncreaseCurrentSpendingByID()
        {
            ConsoleLogger cl = new ConsoleLogger();
            int userIndex;
            while (true)
            {
                try
                {
                    userIndex = GetIndexByID();
                }
                catch (NotValidIDException)
                {
                    cl.Error("Invalid ID.");
                    continue;
                }
                break;
            }
            
            
            cl.Input($"How much did {FIleHandler.valuedCustomers[userIndex].CustomerName} spent: ");
            int currSpending;
            while (true)
            {
                if (int.TryParse(Console.ReadLine(), out currSpending))
                {
                    break;
                }
                else
                {
                    cl.Error("Please use whole numbers to specify the spent amount.");
                    continue;
                }
            } 
            FIleHandler.valuedCustomers[userIndex].CurrentSpending += currSpending;
            cl.Info($"Current Spendings: {FIleHandler.valuedCustomers[userIndex].CurrentSpending}");
            cl.Info($"{FIleHandler.valuedCustomers[userIndex].GetDiscountLevel()}");
            cl.Info($"Saved amount: {FIleHandler.valuedCustomers[userIndex].GetDiscount()}");
        }

        //Lenullázza az összes felhasználó jelenlegi költségét
        public  void ResetCurrentSpendings()
        {
            //Reseting every customers current spending and adding it to the total spending
            foreach (var customer in FIleHandler.valuedCustomers)
            {
                customer.UpdateSpendings();
                customer.CurrentSpending = 0;
            }
            FIleHandler.UpdateFileByFile();
        }

        //Kirajzolja a táblázatot amiben minden vásárló iformációja formázva megtalálható
        public  void DrawAllCustomer()
        {
            var table = new ConsoleTable("NAME", "ADDRESS", "PHONE NUMBER", "ID", "EMAIL", "TOTALSPENT", "ONEAMILLIST");
            foreach (var customer in FIleHandler.valuedCustomers)
            {
                table.AddRow(customer.CustomerName, customer.Address, customer.PhoneNumber, customer.CustomerID, customer.Email,
                    customer.SpentAmount, customer.IsOnEmailList);
            }
            table.Write();
        }

        //Lereseteli a kosárban lévő termékek árát és hozzá adja az össz elköltéshez.
        public  void EmptyCartByCustomer()
        {
            ConsoleLogger cl = new ConsoleLogger();
            int index;
            while (true)
            {
                try
                {
                    index = GetIndexByID();
                }
                catch (NotValidIDException)
                {
                    cl.Error("Invalid ID.");
                    continue;
                }
                break;
            }
            cl.Info($"You spent: {FIleHandler.valuedCustomers[index].CurrentSpending - FIleHandler.valuedCustomers[index].GetDiscount()}," +
                $" your dicount level have been adjusted accordingly");
            FIleHandler.valuedCustomers[index].UpdateSpendings();
            FIleHandler.valuedCustomers[index].CurrentSpending = 0;
            FIleHandler.UpdateFileByFile();
            cl.Info($"Your cart is now empty, thank you for your purchase {FIleHandler.valuedCustomers[index].CustomerName}");
        }
    }
}
