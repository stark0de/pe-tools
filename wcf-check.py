import pefile
import os
import sys
from colorama import init,  Fore

init()

if len(sys.argv) != 2:
   print("Usage: python3 wcf-check.py <Pathtofolder>")
   sys.exit()

keyword=sys.argv[1]

for root, dirs, files in os.walk(keyword, topdown = True):
   for name in files:
      if os.path.join(root, name).endswith(".exe"):
          x=os.path.join(root,name)
          #print(x)
          try:
             pe = pefile.PE(x)
             if b"System.ServiceModel.Primitives.dll" in [y.dll for y in pe.DIRECTORY_ENTRY_IMPORT]:
                print(Fore.GREEN+"WCF usage in :"+x+Fore.WHITE)
             elif b"System.ServiceModel.dll" in [y.dll for y in pe.DIRECTORY_ENTRY_IMPORT]:
                print(Fore.GREEN+"WCF usage in :"+x+Fore.WHITE)
                        
          except:
             pass
