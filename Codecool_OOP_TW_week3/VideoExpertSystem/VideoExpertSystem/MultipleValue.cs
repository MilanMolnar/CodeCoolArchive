using System;
using System.Collections.Generic;
using System.Text;

namespace VideoExpertSystem
{
    public class MultipleValue : Value
    {
        List<string> paramList;
        bool SelectionType { get; set; }
        public MultipleValue(List<string> paramList, bool selectionType)
        {
            this.paramList = paramList;
            this.SelectionType = selectionType;
        }

        public override List<string> GetInputPattern()
        {
            return this.paramList;
        }

        public override bool GetSelectionType()
        {
            return this.SelectionType;
        }
    }
}
