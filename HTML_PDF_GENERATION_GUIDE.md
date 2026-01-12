# HTML and PDF Generation Guide for Mazu Fortune Sticks

This guide explains how to convert markdown translation files into HTML and PDF files.

---

## Overview

**Process Flow:**
```
Translation Batch Files (.md)
        ↓
   Python Scripts
        ↓
   HTML Files (individual)
        ↓
   Chrome Headless (shell script)
        ↓
   PDF Files (individual)
        ↓
   Ghostscript (shell script)
        ↓
   Merged PDF (complete collection)
```

**Output Files:**
- 100 English/Vietnamese HTML files (`stick_001.html` to `stick_100.html`)
- 100 Chinese HTML files (`stick_001_chinese.html` to `stick_100_chinese.html`)
- 200 individual PDF files
- 2 merged PDF files (English/Vietnamese complete + Chinese complete)

---

## Prerequisites

### Required Software:
1. **Python 3** - For parsing markdown and generating HTML
2. **Google Chrome** - For headless PDF generation
3. **Ghostscript** - For merging PDFs

### Verify Installation:
```bash
# Python
python3 --version

# Chrome (macOS path)
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --version

# Ghostscript
gs --version
```

### Install Ghostscript (if needed):
```bash
# macOS with Homebrew
brew install ghostscript
```

---

## File Structure

```
MazuFortuneTranslation/
├── AGENT_PROMPT.md                  # Project instructions
├── HTML_PDF_GENERATION_GUIDE.md     # This guide
├── translations/                    # OCR and translation files
│   ├── batch_01_sticks_001-010.md   # Translation batches
│   ├── batch_02_sticks_011-020.md
│   ├── ... (10 batch files)
│   ├── ocr_batch_01_sticks_001-010.md  # OCR files
│   └── ... (10 OCR files)
├── templates/                       # HTML templates
│   ├── design_template.html         # English/Vietnamese template
│   └── design_template_chinese.html # Chinese template
├── scripts/
│   ├── generate_html.py             # Single script for all HTML generation
│   ├── convert_html_to_pdf.sh
│   ├── convert_chinese_html_to_pdf.sh
│   └── merge_pdfs.sh
├── source_images/                   # Original fortune stick photos
│   └── 001.jpg through 100.jpg
└── output/                          # Generated files (created on demand)
    ├── stick_001.html
    ├── stick_001_chinese.html
    ├── ... (200 HTML files)
    └── pdfs/
        ├── stick_001.pdf
        ├── stick_001_chinese.pdf
        └── ... (200 PDF files)
```

---

## Phase 2: HTML Generation

### Step 1: Understand the Templates

#### English/Vietnamese Template (`design_template.html`)
Uses placeholders that Python replaces:
- `{stick_num}` - Stick number (1-100)
- `{en_rating}` - English fortune rating (e.g., "Upper Fortune")
- `{en_subtitle}` - English subtitle (e.g., "Good / Auspicious")
- `{en_poem}` - English poem text (4 lines)
- `{en_interpretation}` - English interpretation of 解曰 (single paragraph)
- `{en_extended_interpretation}` - Extended interpretation bullets (3 bullet points as `<li>` tags)
- `{vn_rating}` - Vietnamese fortune rating (e.g., "Thượng Quẻ")
- `{vn_subtitle}` - Vietnamese subtitle (e.g., "Tốt / Cát")
- `{vn_poem}` - Vietnamese poem text (4 lines)
- `{vn_interpretation}` - Vietnamese interpretation of 解曰 (single paragraph)
- `{vn_extended_interpretation}` - Extended interpretation bullets (3 bullet points as `<li>` tags)

**CRITICAL:** CSS curly braces `{}` must be escaped as `{{}}` for Python's `.format()` method.

#### Chinese Template (`design_template_chinese.html`)
Uses placeholders:
- `{stick_num}` - Stick number with Chinese prefix (第一籤 1)
- `{rating}` - Fortune rating in Chinese
- `{poem}` - Chinese poem text
- `{interpretation}` - Chinese 解曰 text

### Step 2: Create HTML Generation Scripts

**For English/Vietnamese (per batch):**

```python
#!/usr/bin/env python3
"""Generate HTML files for Batch XX (Sticks XXX-XXX)"""

import os
import re

def parse_stick_data(md_file_path):
    """Parse markdown file and extract data for each stick"""
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by stick markers
    sticks = re.split(r'=+\nSTICK #(\d+)\n=+', content)

    parsed_sticks = []
    for i in range(1, len(sticks), 2):
        stick_num = int(sticks[i])
        stick_content = sticks[i + 1]

        # Extract English section
        en_match = re.search(r'### ENGLISH TRANSLATION\n\n(.*?)\n\n---\n\n### VIETNAMESE TRANSLATION', stick_content, re.DOTALL)
        if not en_match:
            continue
        en_section = en_match.group(1)

        # Extract Vietnamese section
        vn_match = re.search(r'### VIETNAMESE TRANSLATION\n\n(.*?)(?:\n\n---|$)', stick_content, re.DOTALL)
        if not vn_match:
            continue
        vn_section = vn_match.group(1)

        # Parse English
        en_rating_match = re.match(r'([^\(]+)\s*\(([^\)]+)\)', en_section)
        en_rating = en_rating_match.group(1).strip() if en_rating_match else ""
        en_subtitle = en_rating_match.group(2).strip() if en_rating_match else ""

        # For Mazu: No sacred meanings - extract poem directly
        en_poem_match = re.search(r'\*\*Fortune Poem:\*\*\n((?:(?!\*\*).+\n?)+)', en_section, re.MULTILINE)
        en_poem = en_poem_match.group(1).strip() if en_poem_match else ""

        # Extract Interpretation (解曰 translation - single paragraph)
        en_interp_match = re.search(r'\*\*Interpretation:\*\*\n((?:(?!\*\*).+\n?)+)', en_section, re.MULTILINE)
        en_interpretation = en_interp_match.group(1).strip() if en_interp_match else ""

        # Extract Extended Interpretation (bullet points)
        en_ext_interp_match = re.search(r'\*\*Extended Interpretation:\*\*\n((?:•[^\n]+\n?)+)', en_section, re.MULTILINE)
        en_extended_interpretation = en_ext_interp_match.group(1) if en_ext_interp_match else ""

        # Parse Vietnamese
        vn_rating_match = re.match(r'([^\(]+)\s*\(([^\)]+)\)', vn_section)
        vn_rating = vn_rating_match.group(1).strip() if vn_rating_match else ""
        vn_subtitle = vn_rating_match.group(2).strip() if vn_rating_match else ""

        vn_poem_match = re.search(r'\*\*Bài Thơ Quẻ:\*\*\n((?:(?!\*\*).+\n?)+)', vn_section, re.MULTILINE)
        vn_poem = vn_poem_match.group(1).strip() if vn_poem_match else ""

        # Extract Giải Quẻ (解曰 translation - single paragraph)
        vn_interp_match = re.search(r'\*\*Giải Quẻ:\*\*\n((?:(?!\*\*).+\n?)+)', vn_section, re.MULTILINE)
        vn_interpretation = vn_interp_match.group(1).strip() if vn_interp_match else ""

        # Extract Ý Nghĩa Mở Rộng (bullet points)
        vn_ext_interp_match = re.search(r'\*\*Ý Nghĩa Mở Rộng:\*\*\n((?:•[^\n]+\n?)+)', vn_section, re.MULTILINE)
        vn_extended_interpretation = vn_ext_interp_match.group(1) if vn_ext_interp_match else ""

        parsed_sticks.append({
            'num': stick_num,
            'en_rating': en_rating,
            'en_subtitle': en_subtitle,
            'en_poem': en_poem,
            'en_interpretation': en_interpretation,
            'en_extended_interpretation': en_extended_interpretation,
            'vn_rating': vn_rating,
            'vn_subtitle': vn_subtitle,
            'vn_poem': vn_poem,
            'vn_interpretation': vn_interpretation,
            'vn_extended_interpretation': vn_extended_interpretation
        })

    return parsed_sticks

def format_interpretation(text):
    """Convert markdown bullets to HTML list items"""
    lines = text.strip().split('\n')
    html_lines = []
    for line in lines:
        if line.startswith('•'):
            content = line[1:].strip()
            html_lines.append(f'          <li>{content}</li>')
    return '\n'.join(html_lines)

def generate_html(stick_data, template_path='design_template.html'):
    """Generate HTML for a single stick using external template"""
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    html = template.format(
        stick_num=stick_data['num'],
        en_rating=stick_data['en_rating'],
        en_subtitle=stick_data['en_subtitle'],
        en_poem=stick_data['en_poem'],
        en_interpretation=stick_data['en_interpretation'],  # Single paragraph
        en_extended_interpretation=format_interpretation(stick_data['en_extended_interpretation']),  # Bullets
        vn_rating=stick_data['vn_rating'],
        vn_subtitle=stick_data['vn_subtitle'],
        vn_poem=stick_data['vn_poem'],
        vn_interpretation=stick_data['vn_interpretation'],  # Single paragraph
        vn_extended_interpretation=format_interpretation(stick_data['vn_extended_interpretation'])  # Bullets
    )
    return html

def main():
    md_file = 'batch_01_sticks_001-010.md'  # Change per batch
    sticks = parse_stick_data(md_file)

    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)

    for stick in sticks:
        html = generate_html(stick)
        filename = f"{output_dir}/stick_{stick['num']:03d}.html"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Generated: {filename}")

    print(f"\nSuccessfully generated {len(sticks)} HTML files!")

if __name__ == '__main__':
    main()
```

**For Chinese:**

```python
#!/usr/bin/env python3
"""Generate all Chinese HTML files from OCR markdown"""

import os
import re

def parse_chinese_markdown(filepath):
    """Parse the Chinese OCR markdown file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by stick sections (## 第X籤)
    sections = re.split(r'\n## (第\d+籤\s+[上中下]籤)\n', content)[1:]

    sticks = []
    for i in range(0, len(sections), 2):
        if i + 1 >= len(sections):
            break

        header = sections[i]
        body = sections[i + 1]

        # Extract stick number and rating from header
        # e.g., "第1籤 中籤"
        match = re.match(r'第(\d+)籤\s+([上中下]籤)', header)
        if not match:
            continue

        stick_num = int(match.group(1))
        rating = match.group(2)

        # Format stick number for display
        stick_display = f'第{stick_num}籤'

        # Extract poem
        poem_match = re.search(r'\*\*籤詩:\*\*\n((?:(?!\*\*).+\n?)+)', body)
        poem = poem_match.group(1).strip() if poem_match else ''

        # Extract interpretation (解曰)
        interp_match = re.search(r'\*\*解曰:\*\*\n((?:(?!\*\*).+\n?)+)', body)
        interpretation = interp_match.group(1).strip() if interp_match else ''

        sticks.append({
            'stick_num': stick_display,
            'stick_num_int': stick_num,
            'rating': rating,
            'poem': poem,
            'interpretation': interpretation
        })

    return sticks

def generate_html(stick_data, template_path='design_template_chinese.html'):
    """Generate HTML for a single stick"""
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    html = template.format(
        stick_num=stick_data['stick_num'],
        rating=stick_data['rating'],
        poem=stick_data['poem'],
        interpretation=stick_data['interpretation']
    )
    return html

def main():
    sticks = parse_chinese_markdown('mazu_fortune_sticks_chinese_ocr.md')
    print(f"Found {len(sticks)} sticks in markdown")

    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)

    for stick_data in sticks:
        html = generate_html(stick_data)
        output_path = f"{output_dir}/stick_{stick_data['stick_num_int']:03d}_chinese.html"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Generated: {output_path}")

    print(f"\nSuccessfully generated {len(sticks)} Chinese HTML files!")

if __name__ == '__main__':
    main()
```

### Step 3: Run HTML Generation

```bash
# Navigate to project directory
cd /Users/justinqpham/Library/CloudStorage/Dropbox/Projects/MazuFortuneTranslation

# Generate English/Vietnamese HTML (run each batch script)
python3 scripts/generate_batch01_html.py
python3 scripts/generate_batch02_html.py
# ... repeat for all 10 batches

# Generate Chinese HTML
python3 scripts/generate_all_chinese_html.py
```

---

## Phase 3: PDF Conversion

### Step 1: Create PDF Conversion Scripts

**English/Vietnamese PDFs (`convert_html_to_pdf.sh`):**

```bash
#!/bin/bash
# Convert all HTML files to PDF using Chrome headless mode

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
INPUT_DIR="output"
OUTPUT_DIR="output/pdfs"

mkdir -p "$OUTPUT_DIR"

total_files=$(ls ${INPUT_DIR}/stick_*.html 2>/dev/null | grep -v chinese | wc -l | tr -d ' ')
current=0

echo "Converting $total_files HTML files to PDF..."

for html_file in ${INPUT_DIR}/stick_[0-9][0-9][0-9].html; do
    if [ -f "$html_file" ]; then
        filename=$(basename "$html_file" .html)
        pdf_file="${OUTPUT_DIR}/${filename}.pdf"
        abs_html_path="$(cd "$(dirname "$html_file")" && pwd)/$(basename "$html_file")"

        "$CHROME" \
            --headless \
            --disable-gpu \
            --print-to-pdf="$pdf_file" \
            --print-to-pdf-no-header \
            --no-margins \
            "file://${abs_html_path}" \
            2>/dev/null

        if [ $? -eq 0 ]; then
            current=$((current + 1))
            printf "\r[%3d/%3d] Converted: %s" "$current" "$total_files" "$filename"
        fi
    fi
done

echo ""
echo "Conversion complete! Generated $current PDF files"
```

**Chinese PDFs (`convert_chinese_html_to_pdf.sh`):**

```bash
#!/bin/bash
# Convert all Chinese HTML files to PDF using Chrome headless mode
# CRITICAL: --virtual-time-budget=10000 allows time for Google Fonts to load

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
INPUT_DIR="output"
OUTPUT_DIR="output/pdfs"

mkdir -p "$OUTPUT_DIR"

total_files=$(ls ${INPUT_DIR}/stick_*_chinese.html 2>/dev/null | wc -l | tr -d ' ')
current=0

echo "Converting $total_files Chinese HTML files to PDF..."
echo "Using: Chrome headless mode with font loading delay"

for html_file in ${INPUT_DIR}/stick_*_chinese.html; do
    if [ -f "$html_file" ]; then
        filename=$(basename "$html_file" .html)
        pdf_file="${OUTPUT_DIR}/${filename}.pdf"
        abs_html_path="$(cd "$(dirname "$html_file")" && pwd)/$(basename "$html_file")"

        # CRITICAL: --virtual-time-budget=10000 gives Chrome 10 seconds
        # to download Google Fonts before generating PDF
        "$CHROME" \
            --headless \
            --disable-gpu \
            --print-to-pdf="$pdf_file" \
            --print-to-pdf-no-header \
            --no-margins \
            --virtual-time-budget=10000 \
            "file://${abs_html_path}" \
            2>/dev/null

        if [ $? -eq 0 ]; then
            current=$((current + 1))
            printf "\r[%3d/%3d] Converted: %s" "$current" "$total_files" "$filename"
        fi
    fi
done

echo ""
echo "Conversion complete! Generated $current PDF files"
```

### Step 2: Run PDF Conversion

```bash
# Make scripts executable
chmod +x scripts/convert_html_to_pdf.sh
chmod +x scripts/convert_chinese_html_to_pdf.sh

# Convert English/Vietnamese HTMLs to PDF
./scripts/convert_html_to_pdf.sh

# Convert Chinese HTMLs to PDF
./scripts/convert_chinese_html_to_pdf.sh
```

---

## Phase 3b: PDF Merging

### Create Merge Script (`merge_pdfs.sh`)

```bash
#!/bin/bash
# Merge all individual PDF files into complete collections

PDF_DIR="output/pdfs"

# Merge English/Vietnamese PDFs
echo "Merging English/Vietnamese PDFs..."
OUTPUT_EN="Mazu_Fortune_Sticks_Complete.pdf"
pdf_files=$(ls ${PDF_DIR}/stick_[0-9][0-9][0-9].pdf | sort -V)
gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite \
   -sOutputFile="$OUTPUT_EN" \
   $pdf_files

if [ $? -eq 0 ]; then
    file_size=$(ls -lh "$OUTPUT_EN" | awk '{print $5}')
    echo "✅ Created: $OUTPUT_EN ($file_size)"
fi

# Merge Chinese PDFs
echo ""
echo "Merging Chinese PDFs..."
OUTPUT_CN="Mazu_Fortune_Sticks_Chinese_Complete.pdf"
pdf_files_cn=$(ls ${PDF_DIR}/stick_*_chinese.pdf | sort -V)
gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite \
   -sOutputFile="$OUTPUT_CN" \
   $pdf_files_cn

if [ $? -eq 0 ]; then
    file_size=$(ls -lh "$OUTPUT_CN" | awk '{print $5}')
    echo "✅ Created: $OUTPUT_CN ($file_size)"
fi

echo ""
echo "Merge complete!"
```

### Run Merge

```bash
chmod +x scripts/merge_pdfs.sh
./scripts/merge_pdfs.sh
```

---

## Critical Issues & Solutions

### Issue 1: Blank Pages in PDF Output

**Problem:** Chrome headless creates extra blank pages after each fortune stick.

**Solution:** Add these CSS rules in `@media print` section of templates:
```css
@media print {
  .page {
    page-break-after: avoid;  /* CRITICAL */
    overflow: hidden;          /* CRITICAL */
  }
}
```

### Issue 2: Chinese PDF Shows Only Frame (No Text)

**Problem:** Chinese PDFs render with only the decorative frame, no text content.

**Root Cause:** Google Fonts (Noto Serif TC) not loading before PDF generation.

**Solution:** Add `--virtual-time-budget=10000` flag to Chrome command:
```bash
"$CHROME" \
    --headless \
    --disable-gpu \
    --print-to-pdf="$pdf_file" \
    --print-to-pdf-no-header \
    --no-margins \
    --virtual-time-budget=10000 \  # CRITICAL: 10 seconds for fonts
    "file://${abs_html_path}"
```

**Evidence:** Without flag: ~17KB (frame only). With flag: ~290-364KB (full content with fonts).

### Issue 3: Python Template KeyError

**Problem:** `KeyError: '\n      margin'` when running Python script.

**Root Cause:** CSS curly braces `{}` conflict with Python's `.format()` method.

**Solution:** Escape all CSS curly braces by doubling them:
- `{` becomes `{{`
- `}` becomes `}}`
- Only placeholders like `{stick_num}` use single braces

### Issue 4: Regex Not Matching All Content

**Problem:** Multi-line content (poems, interpretations) not fully captured.

**Solution:** Use negative lookahead regex:
```python
# OLD - Only captures single line
poem_match = re.search(r'\*\*Fortune Poem:\*\*\n([^\n]+)', body)

# NEW - Captures all lines until next section
poem_match = re.search(r'\*\*Fortune Poem:\*\*\n((?:(?!\*\*).+\n?)+)', body)
```

---

## Verification Checklist

After each phase, verify:

### HTML Verification:
- [ ] 100 English/Vietnamese HTML files exist (`stick_001.html` to `stick_100.html`)
- [ ] 100 Chinese HTML files exist (`stick_001_chinese.html` to `stick_100_chinese.html`)
- [ ] Open sample HTMLs in browser to verify layout
- [ ] Check that all placeholders were replaced (no `{stick_num}` visible)

### PDF Verification:
- [ ] 200 individual PDFs exist in `output/pdfs/`
- [ ] English/Vietnamese PDFs are ~250-350KB each (not ~17KB)
- [ ] Chinese PDFs are ~290-400KB each (not ~17KB)
- [ ] Open sample PDFs to verify content is visible
- [ ] No extra blank pages

### Merged PDF Verification:
- [ ] `Mazu_Fortune_Sticks_Complete.pdf` exists
- [ ] `Mazu_Fortune_Sticks_Chinese_Complete.pdf` exists
- [ ] Each merged PDF has exactly 100 pages
- [ ] Total size is reasonable (typically 15-30MB each)

---

## Quick Reference Commands

```bash
# Full workflow
cd /Users/justinqpham/Library/CloudStorage/Dropbox/Projects/MazuFortuneTranslation

# 1. Generate all HTML files
for i in {01..10}; do python3 scripts/generate_batch${i}_html.py; done
python3 scripts/generate_all_chinese_html.py

# 2. Convert to PDF
./scripts/convert_html_to_pdf.sh
./scripts/convert_chinese_html_to_pdf.sh

# 3. Merge PDFs
./scripts/merge_pdfs.sh

# Verify results
ls -la output/*.html | wc -l          # Should be 200
ls -la output/pdfs/*.pdf | wc -l      # Should be 200
ls -la *.pdf                           # Should show 2 merged PDFs
```

---

## Notes for Mazu Project

### Key Differences from Guan Yu Project:

1. **No Sacred Meanings:** Mazu sticks don't have the 8-item 聖意 section
   - Guan Yu has: Poem + Sacred Meanings (8 items) + Interpretation
   - Mazu has: Poem + Interpretation (解曰) + Extended Interpretation (3 bullets)

2. **Simpler Fortune Ratings:** Only 3 levels (上籤/中籤/下籤)
   - Guan Yu has 5+ levels; Mazu has only Upper/Middle/Lower

3. **Mazu Translation Structure:**
   - **Fortune Poem** (Bài Thơ Quẻ): 4-line poem translation
   - **Interpretation** (Giải Quẻ): Direct translation of 解曰 - single paragraph
   - **Extended Interpretation** (Ý Nghĩa Mở Rộng): 3 bullet points with expanded guidance

4. **Template Placeholders for Mazu:**
   - `{en_interpretation}` / `{vn_interpretation}` - single paragraph (解曰 translation)
   - `{en_extended_interpretation}` / `{vn_extended_interpretation}` - bullet points as `<li>` tags

5. **Chinese OCR Source:** Use `mazu_fortune_sticks_chinese_ocr.md` or OCR batch files
   - Parsing regex may differ from Guan Yu format
