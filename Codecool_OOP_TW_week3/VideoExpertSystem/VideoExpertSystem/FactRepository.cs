using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;

namespace VideoExpertSystem
{
    public class FactRepository
    {

        private List<Fact> _factRepo = new List<Fact>();

        public void AddFact(Fact fact)
        {
            _factRepo.Add(fact);
        }

        public FactEnumerator GetEnumerator()
        {
            return new FactEnumerator(_factRepo);
        }

        public class FactEnumerator : IEnumerator<Fact>
        {
            private List<Fact> factRepo;

            int index = -1;

            public FactEnumerator(List<Fact> factRepo)
            {
                this.factRepo = factRepo;
            }

            object IEnumerator.Current
            {
                get { return Current; }
            }
 
        public Fact Current
            {
                get
                {
                    try
                    {
                        return factRepo[index];
                    }
                    catch (IndexOutOfRangeException)
                    {

                        throw new Exception("Index out of range");
                    }   
                }
            }

            public void Dispose(){ }

            public bool MoveNext()
            {
                index++;
                if (index < factRepo.Count)
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
