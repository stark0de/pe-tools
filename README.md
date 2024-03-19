# PE-Tools
This repository contains various tools useful for offensive operations (reversing, etc) regarding the PE (Portable Executable) format.

Installs needed:

-pip3 install pefile

-pip3 install colorama

-pip3 install msilib (only for the installer search script)

## Signature searcher
This tool simply finds all .exe files in the C drive and searches for a keyword in their Authenticode signature. This is useful to find all the files signed by the same company (this proves to be useful for thick app pentesting for example).

For more info about Authenticode check this: https://comodosslstore.com/resources/what-is-microsoft-authenticode-code-signing-certificate/

## Exported symbols
This tool simply outputs all of the exported functions of the PE files found in a given directory.

## StringFileInfo searcher
This tool finds all .exe and .dll files in the C drive and searches por a specific keyword in the StringFileInfo block (this is what you see when you right click a binary > go to Properties > Details). This is useful for the same purposes than the Signature searcher.

## VarFileInfo searcher

This tool finds all .exe and .dll files in the C drive and searches por a specific keyword in the VarFileInfo block (similar to StringFileInfo). In most cases it is useful to use both (as well as the signature searcher).

## .NET checker
This tool checks all exe and DLL files in a given directory to see if they were built using .NET or not. This is useful to check which files are worth looking at dnSpy. This can also be done manually using CFF Explorer, for example.

## Weird sections
This tool checks all exe and DLL files in a given directory to see if they have uncommon memory sections.

## WCF check
This tool checks for all the exe files in directory to see if they import various DLLs which are used by the Windows Communication Foundation (WCF) framework.

## .NET remoting checker
This tool checks the IAT of all the .exe files in a directory to check if it imports a .NET remoting-related function and certain DLLs, if this gives positive results, it means a .NET remoting server or client is present in those binaries

## Keyword search IAT, EAT:
This tools just receives as arguments the full path of a folder and the full path of a file containing keywords (1 per line). It will search in all the PE files in the specified directories to check if those keywords are present in any exported or imported functions

## Search installers for keyword:
This tool just looks for all the MSI files recursively in a given folder and parses them to check if they contain a given keyword (this is useful for instance to find the original installer of an application you want to audit). Requires msilib module. Hint: check out C:\Windows\Installer folder.
