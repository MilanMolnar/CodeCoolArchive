using System;


namespace WasteRecycling
{
    public class Dustbin
    {
        public string Color;
        public PaperGarbage[] PaperContent;
        public PlasticGarbage[] PlasticContent;
        public Garbage[] HouseWasteContent;

        public Dustbin(string color)
        {
            Color = color;
            PaperContent = new PaperGarbage[0];
            PlasticContent = new PlasticGarbage[0];
            HouseWasteContent = new Garbage[0];
        }

        private int Cointains(Garbage[] garbages)
        {
            int count = garbages.Length;
            foreach (var garbage in garbages)
            {
                if (garbage == null)
                {
                    count--;
                }
            }
            return count;
        }

        public void DisplayContents()
        {
            Console.WriteLine(Color + " Dustbin!\n");
            Console.WriteLine($"\nHouse waste: {Cointains(HouseWasteContent)} item(s)\n");
            if (HouseWasteContent.Length > 0)
            {
                foreach (Garbage content in HouseWasteContent)
                {
                    if (content != null)
                    {
                        Console.WriteLine($"\t{content.Name}");
                    }
                }
            }
            Console.WriteLine($"\nPaper content: {Cointains(PaperContent)} item(s)\n");
            if (PaperContent.Length > 0)
            {
                foreach (PaperGarbage content in PaperContent)
                {
                    if (content != null)
                    {
                        Console.WriteLine($"\t{content.Name}");
                    }
                }
            }
            Console.WriteLine($"\nPlastic content: {Cointains(PlasticContent)} item(s)\n");
            if (PlasticContent.Length > 0)
            {
                foreach (PlasticGarbage content in PlasticContent)
                {
                    if (content != null)
                    {
                        Console.WriteLine($"\t{content.Name}");
                    }
                }
            }
        }
        public void ThrowOutGarbage(Garbage garbage)
        {

            if (garbage is PlasticGarbage)
            {
                PlasticGarbage plastic = (PlasticGarbage)garbage;

                if (plastic.Cleaned)
                {
                    Array.Resize(ref PlasticContent, +1);
                    PlasticContent[PlasticContent.Length - 1] = plastic;
                }
                else
                {
                    throw new DustbinContentException("The plastic garbage is dirty, clean it first!");
                }
            }
            else if (garbage is PaperGarbage)
            {
                PaperGarbage paper = (PaperGarbage)garbage;
                if (paper.Squeezed)
                {
                    Array.Resize(ref PaperContent, +1);
                    PaperContent[PaperContent.Length - 1] = paper;
                }
                else
                {
                    throw new DustbinContentException("The paper in not squezzed, squezze it!");
                }
            }
            else if (garbage is Garbage)
            {
                Array.Resize(ref HouseWasteContent, +1);
                HouseWasteContent[HouseWasteContent.Length - 1] = garbage;
            }
            else
            {
                throw new DustbinContentException("That isnt trash!");
            }

        }
        public void ThrowOutGarbage(String garbage)
        {
            throw new DustbinContentException("WTF?");
        }

        public void EmptyContents()
        {
            this.PaperContent = new PaperGarbage[0];
            this.PlasticContent = new PlasticGarbage[0];
            this.HouseWasteContent = new Garbage[0];
        }

    }

}
