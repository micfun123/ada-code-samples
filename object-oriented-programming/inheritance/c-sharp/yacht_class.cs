/*
Raspberry Pi Foundation
Developed to be used alongside Isaac Computer Science, part of the National Centre for Computing Education
Usage licensed under CC BY-SA 4

Note: This file is designed to be copied out and compiled on your machine.
In order for it to compile properly you need to ensure that the project name is the same as the "namespace" in this file.
To run this file you need to:
1. Copy the contents
2. Paste them into the C# IDE of your choice (Visual Studio, for example)
3. Change the namespace to match your project (if necessary)
4. Compile the program
5. Run the program
*/

using System;
using System.IO;


namespace IsaacCodeSamples
{
    class Boat
    {

        private string name;
        private float length;
        private int capacity;
        private int berths;
        protected float unitCost;

        // Constructor method
        public Boat(string givenName, float givenLength, int givenCapacity, int givenBerths, float givenUnitCost)
        {
            name = givenName;
            length = givenLength;
            capacity = givenCapacity;
            berths = givenBerths;
            unitCost = givenUnitCost;
        }

    }

    class Yacht : Boat  // Inherits from Boat
    {
        
        private int masts;

        // Constructor method
        public Yacht(string givenName, float givenLength, int givenCapacity, int givenBerths, float givenUnitCost, int givenMasts) : base(givenName, givenLength, givenCapacity, givenBerths, givenUnitCost)
        {
            masts = givenMasts;
        }

    }


    class Testing
    {
        
        // The Main method is the entry point for all C# programs
        public static void Main()
        {
            Yacht myYacht = new Yacht("Mary Sue", 15.7F, 300, 6, 54.5F, 2);
        }

    }

}
