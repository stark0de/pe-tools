import os
import msilib
import warnings

def fxn():
    warnings.warn("deprecated", DeprecationWarning)

def extract_msi_information_keyword(msi_path, keyword):
    try:
        db = msilib.OpenDatabase(msi_path, msilib.MSIDBOPEN_READONLY)
        view = db.OpenView("SELECT * FROM Property")
        view.Execute(None)

        record = view.Fetch()
        keyword_found = False
        while record:
            if keyword.lower() in record.GetString(2).lower():
                keyword_found = True
                break
            record = view.Fetch()

        view.Close()
        db.Close()

        return keyword_found
    except Exception as e:
        print(f"Error processing {msi_path}: {e}")
        return False

def extract_msi_information(msi_path):
    print("-"*30+msi_path+"-"*30)
    try:
        db = msilib.OpenDatabase(msi_path, msilib.MSIDBOPEN_READONLY)
        view = db.OpenView("SELECT * FROM Property")
        view.Execute(None)

        record = view.Fetch()
        while record:
            print(record.GetString(1), ":", record.GetString(2))
            record = view.Fetch()

        view.Close()
        db.Close()
    except Exception as e:
        print(f"Error processing {msi_path}: {e}")

def search_installers_for_keyword(root_path, keyword):
    for root, dirs, files in os.walk(root_path):
        for name in files:
            if name.endswith(".msi"):
                msi_path = os.path.join(root, name)
                keyword_found = extract_msi_information_keyword(msi_path, keyword)
                if keyword_found:
                    print(f"Checking {msi_path} for keyword '{keyword}':")
                    extract_msi_information(msi_path)
                    print("\n" + "=" * 50 + "\n")

if __name__ == "__main__":
    with warnings.catch_warnings(action="ignore"):
        fxn()
    import sys

    if len(sys.argv) != 3:
        print("Usage: python3 search_installers_for_keyword.py <path to search> <keyword>")
        sys.exit(1)
