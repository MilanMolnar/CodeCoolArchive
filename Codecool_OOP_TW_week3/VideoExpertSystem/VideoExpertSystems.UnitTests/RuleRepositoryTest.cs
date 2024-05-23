using NUnit.Framework;
using System;
using System.Collections.Generic;
using System.Text;
using VideoExpertSystem;

namespace VideoExpertSystems.UnitTests
{
    public class RuleRepositoryTest
    {
        [Test]
        public void RuleRepository_AddQuestion_IsTrue()
        {
            var ruleRepo = new RuleRepository();
            Answer answer = new Answer();

            Assert.DoesNotThrow(() => ruleRepo.AddQuestion(new Question("", "",answer)));
        }

        [Test]
        public void QuestionEnumerator_HasCurrentFact_IsTrue()
        {
            Answer answer = new Answer();
            Question question = new Question("1", "1",answer);
            List<Question> questionList = new List<Question>() { question };

            var enumerator = new RuleRepository.QuestionEnumerator(questionList);

            Assert.DoesNotThrow(() => enumerator.MoveNext());
        }

        [Test]
        public void QuestionEnumerator_HasNextFact_IsTrue()
        {
            Answer answer = new Answer();
            Question question1 = new Question("1", "1", answer);
            Question question2 = new Question("2", "2", answer);
            List<Question> questionList = new List<Question>() { question1, question2 };

            var enumerator = new RuleRepository.QuestionEnumerator(questionList);

            enumerator.MoveNext();
            Assert.DoesNotThrow(() => enumerator.MoveNext());
        }
    }
}
