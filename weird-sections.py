import pefile
import sys
import os
from colorama import init,  Fore

init()

if len(sys.argv) != 2:
   print("Usage: python3 weird-sections.py <Pathtofolder>")
   sys.exit()

keyword=sys.argv[1]
normal_sections=[".text",".tls", ".tls$",".vsdata", ".xdata",".sxdata", ".srdata",".sdata",".sbss", ".rsrc", ".reloc",".rdata",".pdata",".idlsym",".idata",".edata",".drective", ".drectve",".data",".cormeta",".debug$S",".debug$F",".debug$P",".debug$T",".bss"]
counter=0

for root, dirs, files in os.walk(keyword, topdown = True):
    for name in files:
        if os.path.join(root, name).endswith(".exe") or os.path.join(root, name).endswith(".dll"):
           try:
              x=os.path.join(root,name)
              #print(x)               
              pe =  pefile.PE(x)
              for section in pe.sections:
                  if section not in normal_sections:
                     print(Fore.GREEN+"[+] Abnormal section "+section+" in "+x+Fore.WHITE)
                     counter+=1
           except:
                continue

if counter == 0:
   print(Fore.RED+"[-] No abnormal sections found in "+keyword+Fore.WHITE)
