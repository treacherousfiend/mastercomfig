import argparse
import sys
from pathlib import Path

import vpk

parser = argparse.ArgumentParser(description="Pack VPK")
parser.add_argument("dir", type=str)
args = parser.parse_args()
dir = Path(args.dir).absolute()

if not dir.is_dir():
    print("Argument must be a directory.")
    sys.exit(1)

folder_name = dir.parts[-1]

newpak = vpk.new(str(dir))
newpak.save(f"{folder_name}.vpk")
print(f"Wrote to {folder_name}.vpk.")
