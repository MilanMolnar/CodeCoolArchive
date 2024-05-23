using System;

namespace WasteRecycling
{
    public class Program
    {
        public static void Main(string[] args)
        {
            
            Garbage rottenTomatoes = new Garbage ("rotten tomato nr.");
           
            PlasticGarbage plastic1 = new PlasticGarbage("plasticlel" , true);

            Dustbin dustbin = new Dustbin("Garbage container");

            dustbin.ThrowOutGarbage(rottenTomatoes);

            dustbin.ThrowOutGarbage(plastic1);

            dustbin.DisplayContents();

            dustbin.EmptyContents();

            dustbin.DisplayContents();
        }
    }
}
