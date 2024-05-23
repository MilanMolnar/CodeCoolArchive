using NUnit.Framework;
using VideoExpertSystem;

namespace VideoExpertSystems.UnitTests
{
    class QuestionTest
    {
        [Test]
        public void Construct_Tester_NewQuestion()
        {
            var q = new Question("Tibi?", "Is any milk left, darling?", new Answer());

            Assert.AreEqual(q.Id, "Tibi?");
            Assert.AreEqual(q.TheQuestion, "Is any milk left, darling?");
        }
    }
}
