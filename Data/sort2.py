import csv
import shutil
from pathlib import Path, PureWindowsPath

# ---------- CONFIG ----------
CSV_PATH   = r"/Users/laurathomas/Github/Paleorocks/PaleoRocks/Data/ACRSortingSpreadsheet.csv"                 # path to your CSV
SOURCE_DIR = Path(r"/Users/laurathomas/Github/Paleorocks/PaleoRocks/Data/ACRPatchesGridNoGlass")    # folder that actually holds the OPX_... images
OUTPUT_DIR = Path(r"/Users/laurathomas/Github/Paleorocks/PaleoRocks/Data/ACRPatchesWholePatchSorting")    # where the sorted folders will be created
LAST_ROW   = 1007                          # last spreadsheet row to process (header = row 1)
MOVE_FILES = False                         # False = copy (safe), True = move
# -----------------------------

fossil_dir    = OUTPUT_DIR / "fossil"
no_fossil_dir = OUTPUT_DIR / "no_fossil"
fossil_dir.mkdir(parents=True, exist_ok=True)
no_fossil_dir.mkdir(parents=True, exist_ok=True)

transfer = shutil.move if MOVE_FILES else shutil.copy2
counts = {"fossil": 0, "no_fossil": 0}
missing = []

with open(CSV_PATH, newline="", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    header = next(reader)  # row 1

    for row_num, row in enumerate(reader, start=2):
        if row_num > LAST_ROW:
            break
        if not row or not row[0].strip():
            continue  # skip blank rows

        # The CSV stores Windows paths from the original machine; keep only the file name
        filename = PureWindowsPath(row[0].strip()).name
        in_patch = row[1].strip().upper() == "TRUE"

        src = SOURCE_DIR / filename
        if not src.exists():
            missing.append((row_num, filename))
            continue

        dest_dir = fossil_dir if in_patch else no_fossil_dir
        transfer(str(src), str(dest_dir / filename))
        counts["fossil" if in_patch else "no_fossil"] += 1

print(f"Fossil in patch:    {counts['fossil']}")
print(f"No fossil in patch: {counts['no_fossil']}")
print(f"Missing files:      {len(missing)}")
for row_num, name in missing[:20]:
    print(f"  row {row_num}: {name}")
if len(missing) > 20:
    print(f"  ... and {len(missing) - 20} more")