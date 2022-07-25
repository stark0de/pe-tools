import pefile
import sys
import os

if len(sys.argv) != 3:
   print("Usage: python3 keyword-search-iat-eat.py \"C:\Path\\to\directory\" \"pathalficherodekeywords\"")
   sys.exit()

directory=sys.argv[1]
keywords=open(sys.argv[2],"r").readlines()

for root, dirs, files in os.walk(directory, topdown = True) or os.path.join(root, name).endswith(".dll"):
   for name in files:
      if os.path.join(root, name).endswith(".exe"):
          x=os.path.join(root,name)
          pe = pefile.PE(x)
          try:
              for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
                  funcion = exp.name.decode('utf-8').lower()
                  for word in keywords:
                      word=word.lower()
                      if word in funcion:
                         print(x+" exports: "+funcion)
              for entry in pe.DIRECTORY_ENTRY_IMPORT:
                  for imp in entry.imports:
                      funcion=imp.name.decode('utf-8').lower()
                      for word in keywords:
                          word=word.lower()
                          if word in funcion:
                             print(x+" imports: "+funcion)



          except AttributeError:
              continue
