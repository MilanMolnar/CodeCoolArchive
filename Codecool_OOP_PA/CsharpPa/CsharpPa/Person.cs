using System;
using System.Collections.Generic;
using System.Text;

namespace api
{
    abstract public class Person
    {
        public Person(string customerName, string address, string phoneNumber)
        {
            this.CustomerName = customerName;
            this.Address = address;
            this.PhoneNumber = phoneNumber;
        }

        public string CustomerName { get; set; }
        public string Address { get; set; }
        public string PhoneNumber { get; set; }
        
    }
    
}
