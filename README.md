# Mazu Fortune Stick Translation Project

Translation of 100 Mazu (天后靈籤) fortune sticks from Chinese to English and Vietnamese, designed for Thien Hau Temple (天后宮) in Los Angeles.

## Overview

This project provides complete translations of traditional Chinese fortune sticks used at Mazu temples. Each stick includes:
- **Fortune Rating:** Upper (上籤), Middle (中籤), or Lower (下籤)
- **Four-line Poem:** Classical Chinese poetry (七言詩)
- **Interpretation:** Traditional explanation of the fortune

Output formats:
- **Bilingual PDF:** English and Vietnamese side-by-side
- **Chinese PDF:** Traditional Chinese for reference
- **Merged Collections:** Complete 100-stick compilations

## Project Structure

```
MazuFortuneTranslation/
├── translations/           # OCR and translation files (10 batches)
├── templates/              # HTML templates for PDF generation
├── scripts/                # Generation and conversion scripts
├── source_images/          # Original fortune stick photos (001-100.jpg)
└── output/                 # Generated HTML and PDF files
```

## Quick Start

### Prerequisites
- Python 3
- Google Chrome (for PDF conversion)
- Ghostscript (`brew install ghostscript` for PDF merging)

### Generate All Files

```bash
# 1. Generate HTML from translations
python3 scripts/generate_html.py --all

# 2. Convert to PDF (English/Vietnamese)
./scripts/convert_html_to_pdf.sh

# 3. Convert to PDF (Chinese)
./scripts/convert_chinese_html_to_pdf.sh

# 4. Merge into complete collections
./scripts/merge_pdfs.sh
```

### Generate Specific Sticks

```bash
# Single stick
python3 scripts/generate_html.py --batch 1
./scripts/convert_html_to_pdf.sh --stick 5
./scripts/convert_chinese_html_to_pdf.sh --stick 5

# Range of sticks
./scripts/convert_html_to_pdf.sh --from 1 --to 10
./scripts/convert_chinese_html_to_pdf.sh --from 1 --to 10
```

## Output Files

| File | Description |
|------|-------------|
| `output/stick_XXX.html` | Individual English/Vietnamese HTML |
| `output/stick_XXX_chinese.html` | Individual Chinese HTML |
| `output/pdfs/stick_XXX.pdf` | Individual English/Vietnamese PDF |
| `output/pdfs/stick_XXX_chinese.pdf` | Individual Chinese PDF |
| `output/Mazu_Fortune_Sticks_Complete.pdf` | All 100 English/Vietnamese sticks |
| `output/Mazu_Fortune_Sticks_Chinese_Complete.pdf` | All 100 Chinese sticks |

## Temple Information

**Thien Hau Temple (天后宮)**
- Address: 750 N. Yale St., Los Angeles, CA 90012
- Phone: 213-680-1860

## Technical Notes

- Chinese PDFs require `--virtual-time-budget=10000` flag for proper Google Fonts loading
- Templates use Python's `.format()` method (CSS braces must be escaped as `{{` and `}}`)
- Stick numbers in Chinese use proper Chinese numerals (一, 二, 三... 一百)

## Documentation

- [AGENT_PROMPT.md](AGENT_PROMPT.md) - Detailed project instructions and OCR guidelines
- [HTML_PDF_GENERATION_GUIDE.md](HTML_PDF_GENERATION_GUIDE.md) - Technical guide for HTML/PDF generation

## License

This project is for educational and religious purposes for Thien Hau Temple.
