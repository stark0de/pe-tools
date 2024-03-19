import sys
import os

if len(sys.argv) != 2:
    print("Usage: python3 varfileinfo-searcher.py <keyword ex: Microsoft>")
    sys.exit()

keyword = sys.argv[1]

for root, dirs, files in os.walk("C:\\", topdown=True):
    for name in files:
        if (
            os.path.join(root, name).endswith(".exe")
            or os.path.join(root, name).endswith(".dll")
        ):
            try:
                x = os.path.join(root, name)
                pe = pefile.PE(x)
                var_version_info = {}
                for fileinfo in pe.FileInfo[0]:
                    if fileinfo.Key.decode() == "VarFileInfo":
                        for st in fileinfo.Var:
                            for entry in st.entry.items():
                                var_version_info[entry[0].decode()] = entry[1].decode()
                for i in var_version_info:
                    keyword = keyword.lower()
                    if keyword in var_version_info[i].lower():
                        print(
                            "The file: "
                            + str(x)
                            + " contains the "
                            + keyword
                            + " keyword in the VarFileInfo block"
                        )
                        break
            except:
                continue
