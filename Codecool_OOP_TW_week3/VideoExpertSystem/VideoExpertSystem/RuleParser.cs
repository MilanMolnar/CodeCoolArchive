using System;
using System.Collections.Generic;
using System.Text;
using System.IO;
using System.Xml.Serialization;
using System.Xml;
using System.Linq;

namespace VideoExpertSystem
{
    public class RuleParser : XMLParser
    {

        public RuleRepository GetRuleRepository()
        {
            RuleRepository ruleRepository = new RuleRepository();
            LoadXmlDocument("Rules.xml");
            foreach (XmlNode node in xmlDoc.DocumentElement)
            {
                Answer ans = new Answer();
                foreach(XmlNode node2 in node.ChildNodes[1].ChildNodes)
                {
                    string rules = node2.ChildNodes[0].Attributes["value"].Value;
                    List<string> stringOfLists = rules.Split(",").ToList<string>();
                    if (stringOfLists.Count>1)
                    {
                        ans.AddValue(new MultipleValue(stringOfLists, Convert.ToBoolean(node2.Attributes["value"].Value)));
                    }
                    else if(stringOfLists.Count==1)
                    {
                        ans.AddValue(new SingleValue(stringOfLists[0], Convert.ToBoolean(node2.Attributes["value"].Value)));
                    }
                    else
                    {
                        throw new Exception("No NULL attribute accepted here!");
                    }   
                }
                Question question = new Question(node.Attributes["id"].Value,node.ChildNodes[0].InnerText,ans);
                ruleRepository.AddQuestion(question);
            }
            return ruleRepository;
            
        }
    }
}
