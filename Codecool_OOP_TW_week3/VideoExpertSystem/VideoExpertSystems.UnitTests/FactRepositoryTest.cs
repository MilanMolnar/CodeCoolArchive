using NUnit.Framework;
using System;
using System.Collections.Generic;
using VideoExpertSystem;

namespace VideoExpertSystems.UnitTests
{
    public class FactRepositoryTest
    {
        [Test]
        public void FactRepository_AddFact_IsTrue()
        {
            var factRepo = new FactRepository();
           
            Assert.DoesNotThrow(() => factRepo.AddFact(new Fact("", "")));
        }

        [Test]
        public void FactEnumerator_HasCurrentFact_IsTrue()
        {
            Fact fact1 = new Fact("1", "1");
            List<Fact> factList = new List<Fact>() { fact1 };

            var enumerator = new FactRepository.FactEnumerator(factList);

            Assert.DoesNotThrow(()=>enumerator.MoveNext());
        }

        [Test]
        public void FactEnumerator_HasNextFact_IsTrue()
        {
            Fact fact1 = new Fact("1", "1");
            Fact fact2 = new Fact("2", "2");
            List<Fact> factList = new List<Fact>() {fact1, fact2};

            var enumerator = new FactRepository.FactEnumerator(factList);

            enumerator.MoveNext();
            Assert.DoesNotThrow(() => enumerator.MoveNext());
        }
    }
}