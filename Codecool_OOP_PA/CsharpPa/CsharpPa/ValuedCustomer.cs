using System;
using System.Collections.Generic;
using System.Text;
using cmd;

namespace api
{
    public class ValuedCustomer : Customer
    {
        public ValuedCustomer(string customerName, string address, string phoneNumber, string customerID,
        string email, int spentAmount, bool isOnEmailList, int currentSpending)
            : base(customerName, address, phoneNumber, customerID, email, spentAmount, isOnEmailList, currentSpending)
        {
            DiscountLevel = SetDiscountLevel();
        }

        public readonly decimal DiscountLevel;

        //Leárazás kiszámítása
        public decimal SetDiscountLevel()
        {
            int discountIncrementRange = SpentAmount/500;
            switch (discountIncrementRange)
            {
                case 0:
                    return 0;
                case 1:
                    return 0.05m;
                case 2:
                    return 0.06m;
                case 3:
                    return 0.08m;
                default:
                    return 0.1m;
            }
        }

        //Visszatér a leárazás értékével az elköltött mennyiséghez viszonyítva 
        public double GetDiscount()
        {
            return CurrentSpending * (double)DiscountLevel;
        }

        //Visszatér a tényleges árral
        public override double CalculateAmount()
        {
            return base.CalculateAmount() - GetDiscount();
        }

        //Kiiratás megformázása a ToString függvény felülírásával 
        public override string ToString()
        {
            return 
                $"Customer's ID: {CustomerID}\nCustomer's Name: {CustomerName}\nCustomer's Address: {Address}\n" +
                $"Customer's Phone Number: {PhoneNumber}\nCustomer's E-mail address: {Email}\n" +
                $"Spending: {SpentAmount:C2}\nCustomer is on E-mail list: {IsOnEmailList}\n";
        }

        //Hozzáadja a jelenleg elköltött mennyiséget az összesen elköltötthöz
        public void UpdateSpendings()
        {
            SpentAmount += Convert.ToInt32(CalculateAmount());
        }

        //Kiiratáshoz szükséges Leárazási szinttel tér vissza
        public string GetDiscountLevel()
        {
            if (SetDiscountLevel() < 0.05m)
            {
                return "No Discount level";
            }
            else if (SetDiscountLevel() >= 0.05m && SetDiscountLevel() < 0.06m)
            {
                return "Discount level 1, you are eligible for a discount of 5%";
            }
            else if (SetDiscountLevel() >= 0.06m && SetDiscountLevel() < 0.08m)
            {
                return "Discount level 2, you are eligible for a discount of 6%";
            }
            else if (SetDiscountLevel() >= 0.08m && SetDiscountLevel() < 0.1m)
            {
                return "Discount level 3, you are eligible for a discount of 8%";
            }
            else if (SetDiscountLevel() >= 0.1m)
            {
                return "Discount level 4, you are eligible for a discount of 10%";
            }
            return "Default";
        }
    }
}
