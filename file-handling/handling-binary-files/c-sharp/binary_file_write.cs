﻿/*
Isaac Computer Science
Usage licensed under the Open Government Licence v3.0

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
using System.Collections.Generic;
using System.IO;

namespace MyApplication
{
    class Program
    {
        // The Main method is the entry point for all C# programs
        public static void Main() {
            var player_stats = new Dictionary<string, double>() {
                {"health", 100},
                {"hunger", 10},
                {"money", 20.00},
                {"lives", 3}
            };
            WriteBinaryFile(player_stats);
        }
        

        // Write data to a binary file
        public static void WriteBinaryFile(Dictionary<string, double> player_stats) {
            string filename = "treasure.game";

            // Write to a new file using File and BinaryWriter
            using (var stream = File.Open(filename, FileMode.Create))
            using (var binaryWriter = new BinaryWriter(stream)) {
                // Write each key and value pair to the file
                foreach (var item in player_stats) {
                    binaryWriter.Write(item.Key);
                    binaryWriter.Write(item.Value);
                }
            }
        }

        
    }
}