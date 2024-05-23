using System;
using System.Collections.Generic;
using System.Text;
using System.Xml;

namespace VideoExpertSystem
{
    public abstract class XMLParser
    {
        protected XmlDocument xmlDoc;
        protected void LoadXmlDocument(string xmlPath)
        {
           xmlDoc = new XmlDocument();
           this.xmlDoc.Load(xmlPath);
        }
    }
}
