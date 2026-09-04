#!/usr/bin/env python3
"""
Organiza los .md en carpetas temáticas.
"""

import argparse
import shutil
from pathlib import Path

FOLDER_RULES = {
    "value-investing": [
        "graham", "buffett", "fisher", "lynch", "munger", "greenblatt",
        "deep value", "margin of safety", "intelligent investor", "inversor inteligente",
        "common stocks", "acciones ordinarias", "security analysis"
    ],
    "mental-models": [
        "munger", "poor charlie", "latticework", "thinking", "biases", "psychology"
    ],
    "strategy-moats": [
        "7 powers", "hamilton helmer", "crossing the chasm", "moat", "competitive"
    ],
    "macro-cycles": [
        "dalio", "debt crisis", "capital returns", "chancellor", "cycles", "blyth"
    ],
    "valuation": [
        "damodaran", "valuation", "dcf", "biotechnology valuation"
    ],
    "quantitative": [
        "quantitative", "härdle", "applied quantitative"
    ],
    "psychology-money": [
        "housel", "psychology of money", "como piensan los ricos", "arte de gastar"
    ],
    "other": []
}

def classify(filename: str) -> str:
    lower = filename.lower()
    for folder, keywords in FOLDER_RULES.items():
        if folder == "other":
            continue
        for kw in keywords:
            if kw in lower:
                return folder
    return "other"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--root", default=".")
    args = parser.parse_args()

    root = Path(args.root)
    md_files = [f for f in root.glob("*.md") if f.name not in ("README.md", "llms.txt", "AGENTS.md")]

    moves = []
    for f in md_files:
        folder = classify(f.name)
        dest_dir = root / "books" / folder
        dest = dest_dir / f.name
        moves.append((f, dest_dir, dest))

    print(f"Se moverán {len(moves)} archivos a books/...\n")
    for src, dest_dir, dest in moves:
        print(f"  {src.name}  →  books/{dest_dir.name}/")

    if args.dry_run:
        print("\nModo dry-run: no se aplicaron cambios.")
        return

    for src, dest_dir, dest in moves:
        dest_dir.mkdir(parents=True, exist_ok=True)
        if dest.exists():
            print(f"⚠ Ya existe, saltando: {dest}")
            continue
        shutil.move(str(src), str(dest))
        print(f"✓ {src.name} → {dest}")

    print("\nListo.")

if __name__ == "__main__":
    main()
