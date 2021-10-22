# PE-Tools
This repository contains various tools useful for offensive operations (reversing, etc) regarding the PE (Portable Executable) format

Installs needed: pip3 install pefile

## Signature searcher
This tool simply finds all .exe files in the C drive and searches for a keyword in their Authenticode signature. This is useful to find all the files signed by the same company (this proves to be useful for thick app pentesting for example).

For more info about Authenticode check this: https://comodosslstore.com/resources/what-is-microsoft-authenticode-code-signing-certificate/

## Exported symbols
This tool simply outputs all of the exported functions of the PE files found in a given directory
