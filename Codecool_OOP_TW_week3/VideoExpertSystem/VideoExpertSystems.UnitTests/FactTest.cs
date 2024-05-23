using NUnit.Framework;
using System;
using System.Collections.Generic;
using System.Text;
using VideoExpertSystem;

namespace VideoExpertSystems.UnitTests
{
    class FactTest
    {
        [Test]
        public void SetFactValueById_ValueAdded_ValueListLenghtIncrease()
        {
            var fact = new Fact("", "");
            fact.SetFactValueById("", true);
            Assert.AreEqual(1, fact.Value.Count);
        }
        [Test]
        public void GetValueById_ReturnValue_FindsTheValue()
        {
            var fact = new Fact("", "");
            fact.SetFactValueById("i", true);

            Assert.IsTrue(fact.GetValueById("i"));
            Assert.Throws<Exception>(() => fact.GetValueById("g"));

        }
    }
}
