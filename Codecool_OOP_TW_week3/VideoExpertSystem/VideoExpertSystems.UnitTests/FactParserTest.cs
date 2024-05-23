using NUnit.Framework;
using System;
using System.Collections.Generic;
using System.Text;
using VideoExpertSystem;

namespace VideoExpertSystems.UnitTests
{
    public class FactParserTest
    {
        [Test]
        public void FactParser_GetFactRepository_IsTrue()
        {
            var fp = new FactParser();

            Assert.DoesNotThrow(() => fp.GetFactRepository());
        }
    }
}
