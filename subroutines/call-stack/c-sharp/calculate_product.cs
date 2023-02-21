/*
Raspberry Pi Foundation
Developed as part of Ada Computer Science 
Usage licensed under CC BY-NC-SA 4.0

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

namespace AdaCodeSamples 
{
    class CallStack
    {
        // The Main method is the entry point for all C# programs
        public static void Main()
        {
            // Demonstrates the use of call stacks
            Console.WriteLine("Please enter a number");
            string num1String = Console.ReadLine();
            int num1 = Convert.ToInt32(num1String);

            Console.WriteLine("Please enter another number");
            string num2String = Console.ReadLine();
            int num2 = Convert.ToInt32(num2String);

            CalculateProduct(num1, num2);
        }
        

        // Calculates the product of two numbers
        public static void CalculateProduct(int n1, int n2)
        {
            int product = n1 * n2;
            Console.WriteLine(product);
        }
        
        
    }
}