import os
import shutil

IMAGE_EXTS = (".jpg", ".jpeg", ".png", ".tif", ".tiff")


def build_reference(sorted_roots, suffix="_cdot"):
    """
    Scan the sorted folders for files named like 'imagename_cdot.ext'.
    Returns {imagename: folder_name}, plus a dict of names found in more than one folder.
    sorted_roots: list of folder paths that already contain sorted '_cdot' images.
    Searches subfolders too; the label is the name of the folder the file sits in.
    """
    reference = {}
    conflicts = {}

    for root in sorted_roots:
        for dirpath, _, files in os.walk(root):
            folder_name = os.path.basename(dirpath)
            for f in files:
                stem, ext = os.path.splitext(f)
                if ext.lower() not in IMAGE_EXTS or not stem.endswith(suffix):
                    continue
                base = stem[: -len(suffix)]           # 'imagename_cdot' -> 'imagename'
                if base in reference and reference[base] != folder_name:
                    conflicts.setdefault(base, {reference[base]}).add(folder_name)
                else:
                    reference[base] = folder_name

    for base in conflicts:                            # ambiguous names get skipped
        reference.pop(base, None)
    return reference, conflicts


def sort_like_cdot(sorted_roots, unsorted_dir, dest_root, suffix="_cdot",
                   move=False, dry_run=True):
    """
    For each image in unsorted_dir named 'imagename.ext', find 'imagename_cdot' in the
    sorted folders and put the unsorted image into dest_root/<same folder name>/.
    """
    reference, conflicts = build_reference(sorted_roots, suffix)
    print(f"Found {len(reference)} sorted '{suffix}' images to use as reference")

    transfer = shutil.move if move else shutil.copy2
    counts, unmatched = {}, []

    for f in os.listdir(unsorted_dir):
        stem, ext = os.path.splitext(f)
        if ext.lower() not in IMAGE_EXTS:
            continue

        # Accept 'imagename.png' (and tolerate 'imagename_cdot.png' if one slips in)
        base = stem[: -len(suffix)] if stem.endswith(suffix) else stem
        folder = reference.get(base)
        if folder is None:
            unmatched.append(f)
            continue

        dest_dir = os.path.join(dest_root, folder)
        if not dry_run:
            os.makedirs(dest_dir, exist_ok=True)
            transfer(os.path.join(unsorted_dir, f), os.path.join(dest_dir, f))
        counts[folder] = counts.get(folder, 0) + 1

    action = "moved" if move else "copied"
    prefix = "[DRY RUN] would have " if dry_run else ""
    for folder, n in counts.items():
        print(f"{prefix}{action} {n} images to {os.path.join(dest_root, folder)}")
    if unmatched:
        print(f"{len(unmatched)} unsorted images had no '{suffix}' match, e.g. {unmatched[:5]}")
    if conflicts:
        print(f"{len(conflicts)} names appear in more than one sorted folder and were skipped: "
              f"{dict(list(conflicts.items())[:5])}")

    return counts, unmatched, conflicts


if __name__ == "__main__":
    # Edit these paths for your data
    sort_like_cdot(
        sorted_roots=[r"/Users/laurathomas/Github/Paleorocks/PaleoRocks/Data/ACRPatchesGridDot/centerFossil",          # folders holding 'imagename_cdot' images
                      r"/Users/laurathomas/Github/Paleorocks/PaleoRocks/Data/ACRPatchesGridDot/edge",
                      r"/Users/laurathomas/Github/Paleorocks/PaleoRocks/Data/ACRPatchesGridDot/noCenterFossil"],
        unsorted_dir=r"/Users/laurathomas/Github/Paleorocks/PaleoRocks/Data/ACRPatchesGridNoGlass",                # folder holding 'imagename' images
        dest_root=r"/Users/laurathomas/Github/Paleorocks/PaleoRocks/Data/ACRPatchesCenterSorting",               # subfolders with the same names get created here
        suffix="_cdot",
        move=False,        # False = copy, True = move
        dry_run=False,      # set to False once the printout looks right
    )