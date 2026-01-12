# Mazu Fortune Stick Translation Project

## Project Structure

```
MazuFortuneTranslation/
├── AGENT_PROMPT.md              # This file - project instructions
├── HTML_PDF_GENERATION_GUIDE.md # Guide for HTML/PDF generation
├── README.md                    # Project overview and usage
├── translations/                # OCR and translation files
│   ├── batch_01_sticks_001-010.md
│   ├── batch_02_sticks_011-020.md
│   ├── ... (10 batch files)
│   ├── ocr_batch_01_sticks_001-010.md
│   ├── ocr_batch_02_sticks_011-020.md
│   └── ... (10 OCR files)
├── templates/                   # HTML templates
│   ├── design_template.html              # English/Vietnamese bilingual (Python template)
│   ├── design_template_chinese.html      # Chinese only (Python template)
│   ├── design_template_preview.html      # Preview with stick 1 content (for design)
│   └── design_template_chinese_preview.html  # Chinese preview with stick 1
├── scripts/                     # Generation scripts
│   ├── generate_html.py              # HTML generation from translations
│   ├── convert_html_to_pdf.sh        # English/Vietnamese HTML → PDF
│   ├── convert_chinese_html_to_pdf.sh # Chinese HTML → PDF (with font loading)
│   └── merge_pdfs.sh                 # Merge individual PDFs into collections
├── source_images/               # Original fortune stick photos
│   ├── 001.jpg through 100.jpg
└── output/                      # Generated HTML/PDF files (created on demand)
    ├── stick_001.html
    ├── stick_001_chinese.html
    ├── pdfs/
    │   ├── stick_001.pdf
    │   └── stick_001_chinese.pdf
    ├── Mazu_Fortune_Sticks_Complete.pdf          # Merged English/Vietnamese
    └── Mazu_Fortune_Sticks_Chinese_Complete.pdf  # Merged Chinese
```

---

## Project Overview

You are translating 100 Mazu (天后靈籤) fortune sticks from Chinese to Vietnamese and English. Each stick contains a fortune rating, a poem, and an interpretation (解曰).

**KEY DIFFERENCE FROM GUAN YU PROJECT:** Mazu sticks have a SIMPLER structure than Guan Yu sticks:
- **NO sacred meanings section (聖意)** - Mazu sticks do not have the 8-item sacred meanings that Guan Yu sticks have
- **Simpler fortune ratings:** 上籤 (Upper), 中籤 (Middle), 下籤 (Lower) - only 3 levels
- **4-line poem** (籤詩) - typically 7 characters per line (七言詩)
- **Interpretation** (解曰) - a short classical Chinese interpretation

---

## CRITICAL: IMAGE READING INSTRUCTIONS

### The Problem (Lesson Learned)
Previous OCR attempts failed due to **rushing through images**. When reading 100 images quickly, Claude made significant errors:
- **Column reading errors** - Misread the right-to-left vertical column order
- **Line truncation** - Lines got cut off or merged incorrectly
- **Missing characters** - Dropped characters at line starts/ends
- **~40-50% error rate** when rushing

### The Solution: SLOW AND CAREFUL Reading

**For EACH image, you MUST:**

1. **Take your time** - Do NOT rush. Accuracy over speed.

2. **Identify the structure first:**
   - Header: 天后靈籤 (top)
   - Stick number: Arabic numeral
   - Fortune rating: 上籤/中籤/下籤
   - Poem area: 4 vertical columns (RIGHT side)
   - 解曰 area: vertical text (LEFT side, marked with 解曰)

3. **Read poem columns RIGHT-TO-LEFT:**
   - Column 1 (rightmost) = Line 1 of poem
   - Column 2 = Line 2 of poem
   - Column 3 = Line 3 of poem
   - Column 4 (leftmost of poem area) = Line 4 of poem

4. **Read each column TOP-TO-BOTTOM:**
   - Start at top character
   - Work down to bottom character
   - Each line should have ~7 characters (七言詩)

5. **Verify line length:**
   - Count characters in each line
   - If a line has significantly fewer than 7 characters, you may have missed something
   - If a line has more than 7-8 characters, you may have merged two columns

6. **Read 解曰 separately:**
   - Located on LEFT side of stick
   - Usually 4 phrases of 4 characters each (e.g., 福不期得，富不期驕，知滿知足，諸禍潛消)

### Quality Checklist (Do This For EVERY Stick)
- [ ] Did I identify all 4 poem columns?
- [ ] Did I read right-to-left?
- [ ] Does each line have ~7 characters?
- [ ] Did I read 解曰 completely?
- [ ] Am I confident in every character?

---

## Progress Tracker

**Status:** Phase 1 COMPLETE - Ready for Phase 2 (HTML Generation)

### Phase 1: OCR + Translation (100 sticks total, 10 sticks per batch):
- ✅ Batch 01 (Sticks 1-10) - COMPLETE
- ✅ Batch 02 (Sticks 11-20) - COMPLETE
- ✅ Batch 03 (Sticks 21-30) - COMPLETE
- ✅ Batch 04 (Sticks 31-40) - COMPLETE
- ✅ Batch 05 (Sticks 41-50) - COMPLETE
- ✅ Batch 06 (Sticks 51-60) - COMPLETE
- ✅ Batch 07 (Sticks 61-70) - COMPLETE
- ✅ Batch 08 (Sticks 71-80) - COMPLETE
- ✅ Batch 09 (Sticks 81-90) - COMPLETE
- ✅ Batch 10 (Sticks 91-100) - COMPLETE

### Errors & Lessons Learned:
1. **DO NOT RUSH** - Previous OCR had ~40-50% error rate from rushing
2. **Column order matters** - Right-to-left, top-to-bottom
3. **Line length varies** - Typical is 7 characters, but 5-8 is acceptable. Do NOT flag lines as "incomplete" based on character count alone
4. **Semantic check over character count** - If the line makes grammatical and semantic sense, it is complete. Only flag if meaning is unclear or nonsensical
5. **This temple's sticks are UNIQUE** - Web sources show different versions (Penghu/Taiwan), do NOT use web to "correct" - trust the source images
6. **Create OCR file per batch** - Document any actual issues clearly
7. **Do not include Chinese in translation output** - Labels like "Interpretation" and "Giải Quẻ" should NOT have Chinese characters next to them

---

## Source Material

### Primary Source (AUTHORITATIVE):
- **Source Images:** `source_images/001.jpg` through `source_images/100.jpg`
- These are the ONLY authoritative source
- Image quality is GOOD - characters are clear and readable

### Web Sources (USE WITH CAUTION):
- Web search "天后靈籤 第X籤" may show DIFFERENT stick versions
- Thien Hau Temple (LA) uses a DIFFERENT set than Taiwan's Penghu Tianhou Temple
- Do NOT "correct" source images based on web results
- Web search is ONLY useful if a character is truly unreadable in the image

### Temple Information:
- **Temple:** Thien Hau Temple (天后宮), Los Angeles
- **Address:** 750 N. Yale St., Los Angeles, CA 90012
- **Phone:** 213-680-1860

---

## Mazu Stick Structure

Each stick contains ONLY:
1. **Header:** 天后靈籤 (Mazu Fortune Stick)
2. **Stick number:** Arabic numeral (1-100)
3. **Fortune rating:** 上籤/中籤/下籤 (Upper/Middle/Lower)
4. **Poem (籤詩):** 4 lines of classical Chinese poetry (typically 7 characters per line)
5. **Interpretation (解曰):** Short classical Chinese interpretation

**IMPORTANT:** There is NO sacred meanings section (聖意) in Mazu sticks. Do NOT add one.

### Visual Layout of Fortune Stick:
```
┌─────────────────────────────────────┐
│          天后靈籤                    │ ← Header (top)
│            XX                        │ ← Stick Number
│          籤 上/中/下                 │ ← Fortune Rating
│                                      │
│   (解曰)    [Col 4] [Col 3] [Col 2] [Col 1] │
│   [解曰     Line4   Line3   Line2   Line1   │ ← READ RIGHT TO LEFT
│    text]                                     │
│                                      │
│           天后宮                     │ ← Temple name
│        213-680-1860                  │
│  750 N. Yale St., Los Angeles...     │
└─────────────────────────────────────┘
```

**Reading order:** Rightmost column first → Leftmost column last
**Each column:** Top character first → Bottom character last

---

## Output Files Per Batch

For each batch, create TWO files:

### 1. OCR File: `ocr_batch_XX_sticks_XXX-XXX.md`
Contains:
- Corrected Chinese text for each stick
- Fortune rating
- Poem (籤詩) - 4 lines
- Interpretation (解曰)
- OCR confidence notes

### 2. Translation File: `batch_XX_sticks_XXX-XXX.md`
Contains:
- Full English translation
- Full Vietnamese translation
- Extended interpretations
- CALL-OUTS section

---

## Fortune Rating Mapping

| Chinese | Vietnamese | English | Subtitle EN | Subtitle VN |
|---------|------------|---------|-------------|-------------|
| 上籤 | Thượng Quẻ | Upper Fortune | (Good / Auspicious) | (Tốt / Cát) |
| 中籤 | Trung Quẻ | Middle Fortune | (Neutral / Mixed) | (Bình thường / Trung bình) |
| 下籤 | Hạ Quẻ | Lower Fortune | (Caution Advised) | (Cần cẩn thận) |

---

## Output Format Per Stick (Translation File)

```
===========================================
STICK #[NUMBER]
===========================================

### ENGLISH TRANSLATION

[Rating] ([Subtitle])

**Fortune Poem:**
[Line 1]
[Line 2]
[Line 3]
[Line 4]

**Interpretation (解曰):**
[English translation of 解曰]

**Extended Interpretation:**
• [Point 1 - max 3 lines]
• [Point 2 - max 3 lines]
• [Point 3 - max 3 lines]

---

### VIETNAMESE TRANSLATION

[Rating] ([Subtitle])

**Bài Thơ Quẻ:**
[Line 1]
[Line 2]
[Line 3]
[Line 4]

**Giải Quẻ (解曰):**
[Vietnamese translation of 解曰]

**Ý Nghĩa Mở Rộng:**
• [Point 1 - max 3 lines]
• [Point 2 - max 3 lines]
• [Point 3 - max 3 lines]

---
```

---

## CALL-OUTS Section (REQUIRED at End of Each Batch)

```markdown
### CALL-OUTS

**OCR Notes:**
- Stick #X: [Any difficulties reading, unclear characters, etc.]
- Stick #Y: [Notes on image quality or character clarity]

**Translation Notes:**
- Stick #X: [Classical Chinese idioms explained, cultural references, etc.]
- Stick #Y: [Any translation choices that could go multiple ways]

**Confidence Levels:**
- HIGH: Sticks #X, #Y, #Z (clear image, confident in all characters)
- MEDIUM: Sticks #A, #B (mostly clear, 1-2 characters uncertain)
- LOW: Sticks #C (requires user verification - [specific concern])

**Items Requiring User Review:**
- Stick #X: [Specific question or concern]
- [List anything needing user confirmation]
```

---

## Batch Process

### For Each Batch:

1. **Read images SLOWLY and CAREFULLY** (10 images per batch)
   - One image at a time
   - Follow the quality checklist above
   - Do NOT rush

2. **Create OCR file:** `ocr_batch_XX_sticks_XXX-XXX.md`
   - Document the Chinese text extracted
   - Note any unclear characters

3. **Create Translation file:** `batch_XX_sticks_XXX-XXX.md`
   - Full English and Vietnamese translations
   - Extended interpretations
   - CALL-OUTS section

4. **Present to user for review**
   - Summarize any concerns or questions
   - Wait for user approval

5. **DO NOT proceed to next batch until user confirms**

---

## Phase Summary

**✅ Phase 1 - OCR + Translation (COMPLETE)**
- Read source images carefully
- Translated 100 sticks in batches of 10
- Output: 20 files (10 OCR + 10 translation files) in `translations/` folder

**📋 Phase 2 - HTML Generation (READY)**
- Convert markdown translations to individual HTML files
- Use templates in `templates/` folder
- Run: `python3 scripts/generate_html.py --batch 1` (or `--all` for all batches)
- Output: 200 HTML files (100 English/Vietnamese + 100 Chinese)
- **Scripts ready:** `generate_html.py` tested and working

**📋 Phase 3 - PDF Conversion (READY)**
- Convert HTML to PDF using Chrome headless
- Run: `./scripts/convert_html_to_pdf.sh --from 1 --to 100` (English/Vietnamese)
- Run: `./scripts/convert_chinese_html_to_pdf.sh --from 1 --to 100` (Chinese)
- **CRITICAL:** Chinese script uses `--virtual-time-budget=10000` for Google Fonts loading
- Output: 200 individual PDF files

**📋 Phase 4 - PDF Merging (READY)**
- Merge individual PDFs into complete collections
- Run: `./scripts/merge_pdfs.sh`
- Output: 2 merged PDFs (English/Vietnamese + Chinese)
- Requires: Ghostscript (`brew install ghostscript`)

---

## CRITICAL: HTML/PDF Generation Instructions

**ALWAYS read `HTML_PDF_GENERATION_GUIDE.md` before creating any HTML or PDF files.**

The guide contains:
- Python scripts for parsing batch markdown files and generating HTML
- Shell scripts for Chrome headless PDF conversion
- Critical CSS fixes for print layout (avoid blank pages)
- `--virtual-time-budget=10000` flag for Chinese fonts
- Template placeholder documentation

**Do NOT manually write HTML files** - use Python scripts with templates to avoid slow generation and errors.

---

## Scripts Reference

### generate_html.py
Generates HTML files from translation markdown files.
```bash
# Generate HTML for a specific batch
python3 scripts/generate_html.py --batch 1

# Generate HTML for all batches
python3 scripts/generate_html.py --all
```

### convert_html_to_pdf.sh
Converts English/Vietnamese HTML files to PDF using Chrome headless.
```bash
# Convert a single stick
./scripts/convert_html_to_pdf.sh --stick 1

# Convert a range
./scripts/convert_html_to_pdf.sh --from 1 --to 10

# Convert all (default)
./scripts/convert_html_to_pdf.sh
```

### convert_chinese_html_to_pdf.sh
Converts Chinese HTML files to PDF. Uses `--virtual-time-budget=10000` for Google Fonts loading.
```bash
# Same arguments as convert_html_to_pdf.sh
./scripts/convert_chinese_html_to_pdf.sh --from 1 --to 10
```

### merge_pdfs.sh
Merges individual PDFs into complete collections using Ghostscript.
```bash
# Merge all PDFs
./scripts/merge_pdfs.sh

# Merge only English/Vietnamese
./scripts/merge_pdfs.sh --english

# Merge only Chinese
./scripts/merge_pdfs.sh --chinese
```
Requires: `brew install ghostscript`

---

## Begin Phase 1

**Start with Batch 01 (Sticks 1-10):**

1. Read each source image `source_images/001.jpg` through `source_images/010.jpg`
2. **TAKE YOUR TIME** - read each image carefully
3. Extract Chinese text following the column-reading instructions above
4. Create `ocr_batch_01_sticks_001-010.md`
5. Create `batch_01_sticks_001-010.md` with translations
6. Present to user and WAIT for confirmation before Batch 02
