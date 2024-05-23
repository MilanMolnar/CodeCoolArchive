using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;

namespace VideoExpertSystem
{
    public class RuleRepository
    {
        private List<Question> questionList = new List<Question>();


        public void AddQuestion(Question question)
        {
            this.questionList.Add(question);
        }
        public QuestionEnumerator GetEnumerator()
        {
            return new QuestionEnumerator(questionList);
        }

        public class QuestionEnumerator : IEnumerator<Question>
        {
            private List<Question> questionRepo;

            int index = -1;

            public QuestionEnumerator(List<Question> factRepo)
            {
                this.questionRepo = factRepo;
            }

            object IEnumerator.Current
            {
                get { return Current; }
            }

            public Question Current
            {
                get
                {
                    try
                    {
                        return questionRepo[index];
                    }
                    catch (IndexOutOfRangeException)
                    {

                        throw new Exception("Index out of range");
                    }
                }
            }

            public void Dispose() { }

            public bool MoveNext()
            {
                index++;
                if (index < questionRepo.Count)
                {
                    return true;
                }
                return false;
            }

            public void Reset()
            {
                throw new NotImplementedException();
            }
        }
    }
}
