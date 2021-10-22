import pefile
import sys
import os

if len(sys.argv) != 2:
   print("Usage: python3 exported-symbols.py \"C:\Path\\to\directory\"")
   sys.exit()

directory=sys.argv[1]

for root, dirs, files in os.walk(directory, topdown = True):
   for name in files:
      if os.path.join(root, name).endswith(".exe") or os.path.join(root, name).endswith(".dll"):
          x=os.path.join(root,name)
          pe = pefile.PE(x)
          print("------------"+str(x)+"------------")
          try:
              for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
                  print(exp.name.decode('utf-8'))
          except AttributeError:
              print("No EAT (Export Address Table)")
              continue 
