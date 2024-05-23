using System;
using System.Collections.Generic;
using System.Text;

namespace VideoExpertSystem
{
    public class Fact
    {
        public string Description { get; set; }
        public string Id { get; set; }

        public List<Value> Value { get; set; }

        public HashSet<String> SetOfId { get; set; }



        public Fact(string description, string id)
        {
            Description = description;
            Id = id;
            this.Value = new List<Value>();
            this.SetOfId = new HashSet<string>();
        }

        public HashSet<String> GetIdHashSet()
        {
            return this.SetOfId;
        }

        public void SetFactValueById(String id, bool value)
        {
            Value.Add(new SingleValue(id, value));
        }

        public bool GetValueById(String id)
        {
            foreach (var item in Value)
            {
                if (item.GetInputPattern()[0].Equals(id))
                {
                    return item.GetSelectionType();
                }
            }
            throw new Exception("No Id like that");
        }

        public string GetDescription()
        {
            return this.Description;
        }
    }
}
