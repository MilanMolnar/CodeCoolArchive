using System;
using System.Xml;

namespace VideoExpertSystem
{
    public class FactParser : XMLParser
    {
        public string Description { get; set; }
        public string Id { get; set; }


        public FactRepository GetFactRepository()
        {
            var factRepository = new FactRepository();
            LoadXmlDocument("Facts.xml");
            
            foreach (XmlNode node in xmlDoc.DocumentElement)
            {
                string id = node.Attributes["id"].Value;
                string desc = node.ChildNodes[0].Attributes["value"].Value;
                Fact fact = new Fact(desc, id);
                
                foreach (XmlNode item in node.ChildNodes[1])
                {
                    fact.SetFactValueById(item.Attributes["id"].Value, Convert.ToBoolean(item.InnerText));
                    fact.SetOfId.Add(item.Attributes["id"].Value);
                }
                factRepository.AddFact(fact);   
            }
            return factRepository;
        }
    }
}
