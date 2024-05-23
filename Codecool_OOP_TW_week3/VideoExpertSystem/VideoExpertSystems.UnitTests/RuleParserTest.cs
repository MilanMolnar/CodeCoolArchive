using NUnit.Framework;
using System;
using System.Collections.Generic;
using System.Text;
using VideoExpertSystem;

namespace VideoExpertSystems.UnitTests
{
    class RuletParserTest
    {
        [Test]
        public void RuleParser_GetRuleRepository_IsTrue()
        {
            var rp = new RuleParser();

            Assert.DoesNotThrow(() => rp.GetRuleRepository());
        }
    }
}
