using System;
using System.Collections.Generic;
using System.Text;
using System.Xml.Serialization;

namespace VideoExpertSystem
{
    public class Question
    {
        public string Id { get; set; }
        public string TheQuestion { get; set; }
        public Answer answer;

        public Question(string id, string theQuestion, Answer answer)
        {
            Id = id;
            TheQuestion = theQuestion;
            this.answer = answer;
        }

        public string GetId()
        {
            return Id;
        }

        public string GetQuestion()
        {
            return TheQuestion;
        }

        public Answer GetAnswer()
        {
            return this.answer;
        }

        public bool EvaluateAnswerByInput(string input)
        {
            return answer.EvaluateAnswerByInput(input);
        }
    }
}
