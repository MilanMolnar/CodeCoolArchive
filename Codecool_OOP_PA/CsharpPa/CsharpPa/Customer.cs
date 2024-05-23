using System;
using System.Collections.Generic;
using System.Text;

namespace api
{
    public class Customer : Person
    {
        public Customer(
            string customerName,
            string address,
            string phoneNumber,
            string customerID,
            string email,
            int spentAmount,
            bool isOnEmailList,
            int currentSpending )
            : base(customerName, address, phoneNumber)
        {
            CustomerID = customerID;
            Email = email;
            SpentAmount = spentAmount;
            IsOnEmailList = isOnEmailList;
            CurrentSpending = currentSpending;

        }

        public int CurrentSpending { get; set; }
        public string CustomerID { get; set; }
        public string Email { get; set; }
        public int SpentAmount { get; set; }
        public bool IsOnEmailList { get; set; }

        public virtual double CalculateAmount()
        {
            return CurrentSpending;
        }
    }
}
