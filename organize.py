"""Sort files by extension into folders"""
import shutil
from pathlib import Path

CATEGORIES = {"Images": {".jpg", ".png", ".gif"}, "Docs": {".pdf", ".docx", ".txt", ".md"}, "Code": {".py", ".js", ".html"}}

def organize(folder):
    folder = Path(folder)
    for f in folder.iterdir():
        if f.is_file():
            for cat, exts in CATEGORIES.items():
                if f.suffix.lower() in exts:
                    dest = folder / cat
                    dest.mkdir(exist_ok=True)
                    shutil.move(str(f), dest / f.name)
                    print(f"{f.name} -> {cat}")
                    break
