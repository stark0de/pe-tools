import pefile
import sys
import os
from colorama import init,  Fore

init()

if len(sys.argv) != 2:
   print("Usage: python3 dotnetremotingsearcher.py <Pathtofolder>")
   sys.exit()

keyword=sys.argv[1]
dotnetremoting=[]

for root, dirs, files in os.walk(keyword, topdown = True):
    for name in files:
       if os.path.join(root, name).endswith(".exe"):
          try:
              x=os.path.join(root,name)
              #print(x)               
              pe =  pefile.PE(x)
              pe.parse_data_directories()
              for entry in pe.DIRECTORY_ENTRY_IMPORT:
                 for imp in entry.imports:
                     if "RegisterChannel" in imp.name and "mscorlib" in entry.dll:
                         dotnetremoting.append(x)
                     elif "System.Runtime.Remoting" in imp.name:
                         dotnetremoting.append(x)
          except:
               continue
              
print(Fore.GREEN+"=========================== Executables using .NET remoting ==============================="+Fore.WHITE)
for i in dotnetremoting:
    print(i)
