using System;
using System.Collections.Generic;
using System.Text;

namespace VideoExpertSystem
{
    public abstract class Value
    {
        public abstract List<string> GetInputPattern();

        public abstract bool GetSelectionType();
    }
}
