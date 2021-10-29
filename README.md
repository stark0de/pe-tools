# PE-Tools
This repository contains various tools useful for offensive operations (reversing, etc) regarding the PE (Portable Executable) format

Installs needed:
pip3 install pefile

pip3 install colorama

## Signature searcher
This tool simply finds all .exe files in the C drive and searches for a keyword in their Authenticode signature. This is useful to find all the files signed by the same company (this proves to be useful for thick app pentesting for example).

For more info about Authenticode check this: https://comodosslstore.com/resources/what-is-microsoft-authenticode-code-signing-certificate/

## Exported symbols
This tool simply outputs all of the exported functions of the PE files found in a given directory.

## StringFileInfo searcher
This tool finds all .exe and .dll files in the C drive and searches por a specific keyword in the StringFileInfo block (this is what you see when you right click a binary > go to Properties > Details). This is useful for the same purposes than the Signature searcher.

## .NET checker
This tool checks all exe and DLL files in a given directory to see if they were built using .NET or not. This is useful to check which files are worth looking at dnSpy. This can also be done manually using CFF Explorer, for example.

## Weird sections
This tool checks all exe and DLL files in a given directory to see if they have uncommon memory sections.

## WCF check
This tool checks for all the exe files in directory to see if they import various DLLs which are used by the Windows Communication Foundation (WCF) framework.
