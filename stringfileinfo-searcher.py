import pefile
import sys
import os

if len(sys.argv) != 2:
   print("Usage: python3 stringfileinfo-searcher.py <keyword ex: Microsoft>")
   sys.exit()

keyword=sys.argv[1]

for root, dirs, files in os.walk("C:\\", topdown = True):
   for name in files:
      if os.path.join(root, name).endswith(".exe") or os.path.join(root, name).endswith(".dll"):
          try:
              x=os.path.join(root,name)
              #print(x)               
              pe =  pefile.PE(x)
              string_version_info = {}
              for fileinfo in pe.FileInfo[0]:
                  if fileinfo.Key.decode() == 'StringFileInfo':
                     for st in fileinfo.StringTable:
                         for entry in st.entries.items():
                             string_version_info[entry[0].decode()] = entry[1].decode()
              for i in string_version_info:
                  #print(string_version_info[i])
                  keyword=keyword.lower()
                  if keyword in string_version_info[i].lower():
                     print("The file: "+str(x)+" contains the "+keyword+ " keyword in the StringFileInfo block")
                     break
          except:
               continue
