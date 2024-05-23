using System;
using System.Collections.Generic;
using System.Text;

namespace VideoExpertSystem
{
    public class Answer
    {
        public List<Value> valueList;

        public Answer()
        {
            this.valueList = new List<Value>();
        }

        public bool EvaluateAnswerByInput(string input)
        {
            foreach (var item in valueList)
            {
                if (item.GetInputPattern().Contains(input))
                    return item.GetSelectionType();
            }
            throw new Exception("Wrong attribute! No value like " + input);
        }

        public void AddValue(Value value)
        {
            this.valueList.Add(value);
        }
    }
}
