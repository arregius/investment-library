#!/usr/bin/env python3
"""
Limpia nombres de archivos .md del repo investment-library.
Solo renombra archivos, no modifica el contenido.
"""

import re
import argparse
from pathlib import Path

NOISE_PATTERNS = [
    r"\s*--\s*Anna[’']?s?\s*Archive.*$",
    r"\s*-?\s*Anna[’']?s?\s*Archive.*$",
    r"\s*_compressed(_compressed)?\.md$",
    r"\s*-?\s*[a-f0-9]{8,}\s*",
    r"\s*--\s*\d{4}\s*--\s*.*$",
    r"\s*-\s*\d{4}\s*-\s*.*Archive.*$",
    r"\s*\(The Wiley.*$",
    r"\s*--\s*1st ed.*$",
    r"\s*--\s*3,\s*\d{4}.*$",
    r"\s*_+\s*",
]

def clean_name(name: str) -> str:
    original = name
    if name.lower().endswith(".md"):
        stem = name[:-3]
    else:
        stem = name

    for pat in NOISE_PATTERNS:
        stem = re.sub(pat, "", stem, flags=re.IGNORECASE)

    stem = re.sub(r"[\s_]+", " ", stem)
    stem = re.sub(r"\s*-\s*", " - ", stem)
    stem = stem.strip(" -_.")
    stem = re.sub(r"\s{2,}", " ", stem)

    if len(stem) > 120:
        stem = stem[:117].rsplit(" ", 1)[0] + "..."

    new_name = stem + ".md"
    return new_name if new_name != original else original

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Solo mostrar cambios")
    parser.add_argument("--root", default=".", help="Raíz del repo")
    args = parser.parse_args()

    root = Path(args.root)
    md_files = [f for f in root.glob("*.md") if f.name not in ("README.md", "llms.txt", "AGENTS.md")]

    changes = []
    for f in sorted(md_files):
        new_name = clean_name(f.name)
        if new_name != f.name:
            changes.append((f, root / new_name))

    if not changes:
        print("No hay archivos que renombrar.")
        return

    print(f"Se renombrarán {len(changes)} archivos:\n")
    for old, new in changes:
        print(f"  {old.name}")
        print(f"  → {new.name}\n")

    if args.dry_run:
        print("Modo dry-run: no se aplicaron cambios.")
        return

    for old, new in changes:
        if new.exists():
            print(f"⚠ Saltando (ya existe): {new.name}")
            continue
        old.rename(new)
        print(f"✓ {old.name} → {new.name}")

    print("\nListo.")

if __name__ == "__main__":
    main()
