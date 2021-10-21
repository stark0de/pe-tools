import pefile
import os
import subprocess
import sys

if len(sys.argv) != 2:
   print("Usage: python3 signature-searcher.py <keyword ex: Microsoft>")
   sys.exit()

keyword=sys.argv[1]

#Still need to add a feature to exclude paths

for root, dirs, files in os.walk("C:\\", topdown = True):
   for name in files:
      if os.path.join(root, name).endswith(".exe"):
          x=os.path.join(root,name)
          result=subprocess.Popen("powershell.exe -c \"(Get-AuthenticodeSignature '"+x+"').SignerCertificate.Subject\"", stderr=subprocess.STDOUT, shell=True,stdout=subprocess.PIPE).communicate()[0]
          if keyword in str(result):
             print(x+"::::"+str(result))