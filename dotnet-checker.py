import pefile
import sys
import os
from colorama import init,  Fore

init()

if len(sys.argv) != 2:
   print("Usage: python3 dotnet-checker.py <Pathtofolder>")
   sys.exit()

keyword=sys.argv[1]
dotnet=[]
others=[]

for root, dirs, files in os.walk(keyword, topdown = True):
    for name in files:
       if os.path.join(root, name).endswith(".exe") or os.path.join(root, name).endswith(".dll"):
          try:
              x=os.path.join(root,name)
              #print(x)               
              pe =  pefile.PE(x)
              isDotNet = pe.OPTIONAL_HEADER.DATA_DIRECTORY[14]
              if isDotNet.VirtualAddress == 0 and isDotNet.Size == 0:
                 others.append(x)
              else:
                 dotnet.append(x)
          except:
               continue
              
print(Fore.GREEN+"=========================== .NET executables ==============================="+Fore.WHITE)
for i in dotnet:
    print(i)
print(Fore.RED+"=========================== Non-.NET executables ==========================="+Fore.WHITE)
for i in others:
    print(i) 
