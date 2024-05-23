using System;
using System.Collections.Generic;
using System.Text;
using System.IO;
using System.Linq;
using System.Xml.Linq;
using cmd;


namespace api
{
    public static class FIleHandler
    {
        //Lista az értékes vásárlókról
        public static List<ValuedCustomer> valuedCustomers = new List<ValuedCustomer>();
        //Kiolvassa az információkat a CustomerInfo fájlból
        public static void GetData()
        {
            using (var sr = new StreamReader(Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments), "CustomerInfo.txt")))
            {
                int index = 0;
                valuedCustomers = new List<ValuedCustomer>();
                while (!sr.EndOfStream)
                {
                    //Beolvassa a sorokat egy Listába
                    var line = sr.ReadLine().Split(':');
                    var name = line[0];
                    var address = line[1];
                    var phone = line[2];
                    var id = line[3];
                    var email = line[4];
                    var spendAmount = Convert.ToInt32(line[5]);
                    var onEmailList = Convert.ToBoolean(line[6]);
                    var currentSpending = Convert.ToInt32(line[7]);
                    valuedCustomers.Add(new ValuedCustomer(name, address, phone, id, email, spendAmount, onEmailList, currentSpending));
                    index++;

                }
            }
        }

        //Felülírjuk a fájlt az előző file segítségével
        public static void UpdateFileByFile()
        {
            //Kiolvassuk a fálj sorainak számát
            var linesLength = 0;
            using (var sr = new StreamReader(Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments), "CustomerInfo.txt")))
            {
                while (sr.ReadLine() != null)
                {
                    linesLength++;
                }
            }

            using (var sw = new StreamWriter(Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments), "CustomerInfo.txt")))
            {
                for (var i = 0; i < linesLength; i++)
                {
                    //Beírja a vásárlót a fájlba
                    var name = valuedCustomers[i].CustomerName;
                    var address = valuedCustomers[i].Address;
                    var phone = valuedCustomers[i].PhoneNumber;
                    var id = valuedCustomers[i].CustomerID;
                    var email = valuedCustomers[i].Email;
                    var spendAmount = valuedCustomers[i].SpentAmount;
                    var onEmailList = valuedCustomers[i].IsOnEmailList;
                    var currentSpendings = valuedCustomers[i].CurrentSpending;
                    sw.WriteLine($"{name}:{address}:{phone}:{id}:{email}:{spendAmount}:{(onEmailList == true ? "true" : "false")}:{currentSpendings}");
                }
            }
        }

        //Felülírjuk a fájlt a memóriába betöltött listával segítségével
        public static void UpdateFileByList()
        {
            //Kiolvassuk a fálj sorainak számát
            var linesLength = valuedCustomers.Count;
            

            using (var sw = new StreamWriter(Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments), "CustomerInfo.txt")))
            {
                for (var i = 0; i < linesLength; i++)
                {
                    //Beírja a vásárlót a fájlba
                    var name = valuedCustomers[i].CustomerName;
                    var address = valuedCustomers[i].Address;
                    var phone = valuedCustomers[i].PhoneNumber;
                    var id = valuedCustomers[i].CustomerID;
                    var email = valuedCustomers[i].Email;
                    var spendAmount = valuedCustomers[i].SpentAmount;
                    var onEmailList = valuedCustomers[i].IsOnEmailList;
                    var currentSpendings = valuedCustomers[i].CurrentSpending;
                    sw.WriteLine($"{name}:{address}:{phone}:{id}:{email}:{spendAmount}:{(onEmailList == true ? "true" : "false")}:{currentSpendings}");
                }
            }
        }

        //Beírja a fájlba az új vásárlót
        public static void AddCustomer(string newname, string newaddress, string newphone, string newemail, string newonEmailList)
        {
            ConsoleLogger cl = new ConsoleLogger();
            int linesLength = 0;
            using (var sr = new StreamReader(Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments), "CustomerInfo.txt")))
            {
                while (sr.ReadLine() != null)
                {
                    linesLength++;
                }
            }
            using (var sw = new StreamWriter(Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments), "CustomerInfo.txt")))
            {
                for (var i = 0; i < linesLength; i++)
                {
                    //Beírja a vásárlót a fájlba
                    var name = valuedCustomers[i].CustomerName;
                    var address = valuedCustomers[i].Address;
                    var phone = valuedCustomers[i].PhoneNumber;
                    var id = valuedCustomers[i].CustomerID;
                    var email = valuedCustomers[i].Email;
                    var spendAmount = valuedCustomers[i].SpentAmount;
                    var onEmailList = valuedCustomers[i].IsOnEmailList;
                    var currentSpending = valuedCustomers[i].CurrentSpending;
                    sw.WriteLine($"{name}:{address}:{phone}:{id}:{email}:{spendAmount}:{(onEmailList == true ? "true" : "false")}:{currentSpending}");
                }
                //Beírja a hozáadott customert
                sw.WriteLine($"{newname}:{newaddress}:{newphone}:{"A00000" + Convert.ToString(linesLength + 1)}:{newemail}:{0}:{newonEmailList}:{0}");
                cl.Info($"{newname} Has been succesfully added...");
            }

        }

        //Eltávolítja egy vásárlót a listából felhasználó által megadott ID alapján majd frissiti a fájlt az új lista alapján
        public static void RemoveCustomerByID()
        {
            ConsoleLogger cl = new ConsoleLogger();
            int removeIndex;
            while (true)
            {
                try
                {
                    removeIndex = DataManager.GetIndexByID();
                }
                catch (NotValidIDException)
                {
                    cl.Error("Invalid ID.");
                    continue;
                }
                break;
            }
            string removedName = valuedCustomers[removeIndex].CustomerName;
            valuedCustomers.RemoveAt(removeIndex);
            UpdateFileByList();
            cl.Info($"{removedName} is succesfully deleted form the system...");
        }

        //Elmenti a jelenlegi állapotot egy XML fáljba
        public static void SaveToXML()
        {
            ConsoleLogger cl = new ConsoleLogger();
            XElement root = new XElement("ValuedCustomers");
            foreach (var customer in valuedCustomers)
            {
                root.Add(
                    new XElement("ValuedCustomer",
                        new XElement("Name", customer.CustomerName),
                        new XElement("Address", customer.Address),
                        new XElement("PhoneAddress", customer.PhoneNumber),
                        new XElement("ID", customer.CustomerID),
                        new XElement("Email", customer.Email),
                        new XElement("TotalSpent", customer.SpentAmount),
                        new XElement("IsOnEmailList", customer.IsOnEmailList)
                        ));
            }
            root.Save(Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments), "CustomersXml.xml"));
            cl.Info("Current state saved to XML file to your 'MyDocuments' folder");
        }
    }
} 


 
