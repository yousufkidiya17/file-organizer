"""Sort files by extension into folders"""
import shutil
import sys
from pathlib import Path

CATEGORIES = {"Images": {".jpg", ".png", ".gif"}, "Docs": {".pdf", ".docx", ".txt", ".md"}, "Code": {".py", ".js", ".html"}}

def organize(folder, dry=False):
    folder = Path(folder)
    moved = 0
    for f in folder.iterdir():
        if f.is_file():
            for cat, exts in CATEGORIES.items():
                if f.suffix.lower() in exts:
                    dest = folder / cat
                    dest.mkdir(exist_ok=True)
                    if dry:
                        print(f"[dry] {f.name} -> {cat}")
                    else:
                        shutil.move(str(f), dest / f.name)
                        print(f"{f.name} -> {cat}")
                    moved += 1
                    break
    print(f"total: {moved} files")

if __name__ == "__main__":
    dry = "--dry" in sys.argv
    target = [a for a in sys.argv[1:] if not a.startswith("--")]
    organize(target[0], dry)
