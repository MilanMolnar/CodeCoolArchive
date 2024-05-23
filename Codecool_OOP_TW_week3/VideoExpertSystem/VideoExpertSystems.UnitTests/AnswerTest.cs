using NUnit.Framework;
using System;
using VideoExpertSystem;

namespace VideoExpertSystems.UnitTests
{
    public class AnswerTest
    {
        [Test]
        public void AddValue_ValueAdded_ValueListLenghtIncrease()
        {
            var value = new SingleValue("", true);
            var answer = new Answer();

            answer.AddValue(value);
            answer.AddValue(value);

            Assert.AreEqual(2, answer.valueList.Count);
        }
        [Test]
        public void EvaluateAnswerByInput_SeePossibleOutputs_FalseTrueException()
        {
            var answer = new Answer();

            answer.AddValue(new SingleValue("a", true));
            answer.AddValue(new SingleValue("b", false));

            Assert.IsTrue(answer.EvaluateAnswerByInput("a"));
            Assert.IsFalse(answer.EvaluateAnswerByInput("b"));
            Assert.Throws<System.Exception>(() => answer.EvaluateAnswerByInput("g"));
        }
    }
}
