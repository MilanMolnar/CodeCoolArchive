using System;
using System.Collections.Generic;
using System.Text;

namespace VideoExpertSystem
{
    public class SingleValue : Value
    {
        string Param { get; set; }
        bool SelectionType { get; set; }
        public SingleValue(string param, bool selectionType)
        {
            this.Param = param;
            this.SelectionType = selectionType;
        }

        public override List<string> GetInputPattern()
        {
            List<string> paramList = new List<string>();
            paramList.Add(Param);
            return paramList;
        }

        public override bool GetSelectionType()
        {
            return this.SelectionType;
        }
    }
}
