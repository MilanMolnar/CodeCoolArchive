using System;
using System.Collections.Generic;
using System.Linq;
using System.Diagnostics;

namespace VideoExpertSystem
{
    public class ESProvider
    {
        private FactParser _factParser;
        private RuleParser _ruleParser;
        private List<Value> answers;

        public List<Value> Answers
        {
            get { return answers; }
            set { answers = value; }
        }

        public ESProvider(FactParser factParser, RuleParser ruleParser)
        {
            _factParser = factParser;
            _ruleParser = ruleParser;
            answers = new List<Value>();
            CollectAnswers();
            Console.WriteLine(Evaluate());
        }
        public void CollectAnswers()
        {
            var ens = _ruleParser.GetRuleRepository().GetEnumerator();
            while (ens.MoveNext())
            {
                Answers.Add(new SingleValue(ens.Current.Id, GetAnswerByQuestion(ens.Current.Id)));
            }
        }

        public bool GetAnswerByQuestion(string questionId)
        {
            var en = _ruleParser.GetRuleRepository().GetEnumerator();
            while (en.MoveNext())
            {
                if (en.Current.Id.Equals(questionId))
                {
                    Console.WriteLine(en.Current.TheQuestion);
                    var userAnswer = Console.ReadLine();
                    return en.Current.EvaluateAnswerByInput(userAnswer);
                }
            }
            throw new Exception("Invalid input");
        }

        public string Evaluate()
        {
            var fr = _factParser.GetFactRepository();
            var em = fr.GetEnumerator();

            while (em.MoveNext())
            {
                var factCounter = 0;
                for (int count = 0; count < em.Current.Value.Count; count++)
                {
                    if (em.Current.Value[count].GetSelectionType().Equals(answers[count].GetSelectionType()))
                    {
                        factCounter++;
                    }
                }
                if (factCounter == 4)
                {
                    OpenUrl(em.Current.Id);
                    return em.Current.Description;
                }
            }
            throw new Exception("Don't mess with us!");
        }

        public void OpenUrl(string name)
        {
            if(!string.IsNullOrEmpty(name))
            {
                try
                {
                    Process proc = new Process();
                    proc.StartInfo.UseShellExecute = true;
                    proc.StartInfo.FileName = name;
                    proc.Start();
                }
                catch
                {
                    Console.WriteLine("Can't open the link!");
                }
            }
        }
    }
}
