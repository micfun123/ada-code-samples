' Raspberry Pi Foundation
' Usage licensed under CC BY-NC-SA 4.0
' Note: This file is designed to be copied out and compiled on your machine.
' To run this file you need to:
' 1. Copy the contents
' 2. Paste them into the Visual Basic IDE of your choice (Visual Studio, for example)
' 3. Compile the program
' 4. Run the program

Module Program

    ' The Main subroutine is the default entry point for a VB program
    Sub Main()
        Dim myString As String = "An aardvark is an animal"
        Dim newString As String = ChangeString(myString)
        Console.WriteLine(newString)
    End Sub

    Function ChangeString(ByVal myString As String) As String
        Dim newString As String = ""

        For Each character In myString

            If character = "a" Then
                newString = newString & "b"
            Else
                newString = newString & character
            End If
        Next

        Return newString
    End Function


End Module
