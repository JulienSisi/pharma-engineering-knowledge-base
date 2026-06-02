#!/usr/bin/env python3
"""
translate_repo.py
─────────────────
Translates all Markdown files in the pharma-engineering-knowledge-base repo
into English (en), German (de), and Italian (it), and reorganises the repo
into language subfolders:

  pharma-engineering-knowledge-base/
  ├── fr/   ← original French content (moved here)
  ├── en/   ← English translation
  ├── de/   ← German translation
  └── it/   ← Italian translation

Usage
─────
  # 1. Create a .env file with your API key:
  echo "ANTHROPIC_API_KEY=sk-ant-..." > .env

  # 2. Run from inside the repo root:
  python3 translate_repo.py

Requirements
────────────
  pip install anthropic python-dotenv

Notes
─────
- The script moves the existing French files into a fr/ subfolder.
- It translates each file individually so you can resume if interrupted.
- Already-translated files are skipped (idempotent).
- Technical terms (GMP, CMMS, OEE, MTBF, CAPA, SOP, etc.) are preserved.
- Code blocks and Markdown structure are preserved.
- Rate limiting: 1-second pause between API calls.
"""

import os
import sys
import time
import shutil
import anthropic
from dotenv import load_dotenv

# ── Configuration ─────────────────────────────────────────────────────────────

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))

LANGUAGES = {
    "en": "English",
    "de": "German",
    "it": "Italian",
}

# Technical terms that must NOT be translated
PRESERVED_TERMS = [
    "GMP", "cGMP", "CMMS", "ERP", "OEE", "MTBF", "MTTR", "CAPA", "SOP",
    "WP", "MDS", "FORM", "API", "IPM", "RPN", "ISA-95", "TPM", "RCM",
    "CBM", "CPP", "CQA", "REMS", "ALCOA", "IQ", "OQ", "PQ", "URS",
    "FAT", "SAT", "DQ", "CQV", "CAPEX", "OPEX", "CDMO", "HPAPI", "ADC",
    "WFI", "CIP", "SIP", "HVAC", "SHE", "FDA", "EMA", "SwissMedic",
    "FMEA", "RCA", "DMAIC", "SME", "KPI", "IoT", "PAT", "MES", "SCADA",
    "LSM", "ICH", "GAMP", "ISPE",
]

# ── Helpers ────────────────────────────────────────────────────────────────────

def get_md_files(folder: str) -> list[str]:
    """Recursively collect all .md files under folder."""
    result = []
    for root, _, files in os.walk(folder):
        for f in files:
            if f.endswith(".md"):
                result.append(os.path.join(root, f))
    return sorted(result)


def relative_path(path: str, base: str) -> str:
    return os.path.relpath(path, base)


def translate_content(client: anthropic.Anthropic, content: str, target_lang: str, target_lang_name: str) -> str:
    """Call Claude API to translate a single Markdown file content."""

    preserved = ", ".join(PRESERVED_TERMS)

    prompt = f"""You are a professional pharmaceutical/technical translator.

Translate the following Markdown document from French into {target_lang_name}.

Rules:
1. Preserve ALL Markdown formatting exactly (headers, tables, code blocks, lists, bold, italic, links).
2. Do NOT translate these technical terms — keep them exactly as-is: {preserved}
3. Do NOT translate proper nouns: Celgene, WuXi AppTec, Lonza, Visp, MAFFIOLI, Oracle, Consensus, GitHub, Revlimid, Thalomid, Otezla, Lénalidomide, Thalidomide, Aprémilast (you may use their common English/target-language names if universally known).
4. Preserve all ASCII diagrams and code blocks without any changes.
5. Translate section titles and body text naturally and professionally.
6. Do NOT add any preamble or explanation — output ONLY the translated Markdown.

---DOCUMENT TO TRANSLATE---
{content}
---END OF DOCUMENT---"""

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    # Charge les variables d'environnement depuis .env
    load_dotenv()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌  ANTHROPIC_API_KEY not found.")
        print("    Create a .env file with: ANTHROPIC_API_KEY=sk-ant-...")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    # ── Step 1: Move existing files into fr/ ──────────────────────────────────
    fr_dir = os.path.join(REPO_ROOT, "fr")
    os.makedirs(fr_dir, exist_ok=True)

    folders_to_move = ["01_celgene-memoir", "02_lonza-research", "03_future-projects"]
    root_mds = ["README.md"]

    for folder in folders_to_move:
        src = os.path.join(REPO_ROOT, folder)
        dst = os.path.join(fr_dir, folder)
        if os.path.exists(src) and not os.path.exists(dst):
            shutil.copytree(src, dst)
            print(f"📁  Copied {folder} → fr/{folder}")

    for md in root_mds:
        src = os.path.join(REPO_ROOT, md)
        dst = os.path.join(fr_dir, md)
        if os.path.exists(src) and not os.path.exists(dst):
            shutil.copy2(src, dst)
            print(f"📄  Copied {md} → fr/{md}")

    # ── Step 2: Collect all French .md files ─────────────────────────────────
    fr_files = get_md_files(fr_dir)
    print(f"\n📚  Found {len(fr_files)} Markdown files to translate.\n")

    # ── Step 3: Translate into each target language ───────────────────────────
    for lang_code, lang_name in LANGUAGES.items():
        lang_dir = os.path.join(REPO_ROOT, lang_code)
        os.makedirs(lang_dir, exist_ok=True)
        print(f"\n{'─'*60}")
        print(f"🌐  Translating into {lang_name} ({lang_code}/)...")
        print(f"{'─'*60}")

        for fr_path in fr_files:
            # Mirror the path under the target language folder
            rel = relative_path(fr_path, fr_dir)
            target_path = os.path.join(lang_dir, rel)

            # Skip if already translated
            if os.path.exists(target_path):
                print(f"  ⏭️   Skipping (exists): {rel}")
                continue

            # Ensure parent directory exists
            os.makedirs(os.path.dirname(target_path), exist_ok=True)

            # Read source
            with open(fr_path, "r", encoding="utf-8") as f:
                content = f.read()

            print(f"  🔄  Translating: {rel}", end="", flush=True)

            try:
                translated = translate_content(client, content, lang_code, lang_name)
                with open(target_path, "w", encoding="utf-8") as f:
                    f.write(translated)
                print(f" ✅")
            except Exception as e:
                print(f" ❌  Error: {e}")

            # Polite pause between API calls
            time.sleep(1)

    # ── Step 4: Summary ───────────────────────────────────────────────────────
    print(f"\n{'═'*60}")
    print("✅  Translation complete! Repo structure:")
    for lang_code, lang_name in [("fr", "French (original)"), *LANGUAGES.items()]:
        count = len(get_md_files(os.path.join(REPO_ROOT, lang_code)))
        print(f"  {lang_code}/  ← {lang_name} ({count} files)")

    print(f"\n📦  Next steps:")
    print("  git add .")
    print("  git commit -m 'Add multilingual support: en, de, it'")
    print("  git push")


if __name__ == "__main__":
    main()
