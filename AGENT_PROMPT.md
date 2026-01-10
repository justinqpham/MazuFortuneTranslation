# Mazu Fortune Stick Translation Project

## Project Overview

You are translating 60 Mazu (媽祖靈籤 - 六十甲子籤) fortune sticks from Chinese to Vietnamese and English. Each stick contains a fortune rating, sacred meanings, and a poem. You will also generate interpretations based on the content.

**CRITICAL DIFFERENCE from Guan Yu Project:** Mazu fortune sticks vary significantly between temples and **DO NOT have standardized canonical sources** like Guan Yu. OCR verification will rely on multi-source validation, pattern recognition, and user confirmation.

**Process:**
1. **Phase 0:** Extract and verify OCR from all 60 images, save to `mazu_fortune_sticks_chinese_ocr.md`
2. **Phase 1:** Translate 6 sticks at a time (10 batches total) using verified OCR file as source
3. Present each batch for user confirmation, learn from feedback, then proceed to next batch

---

## Progress Tracker

**Status:** Phase 0 - OCR Extraction NOT STARTED

### Phase 0: OCR Extraction
- ⏳ OCR all 60 images - Not Started
- ⏳ Save to `mazu_fortune_sticks_chinese_ocr.md` - Not Started
- ⏳ User review and corrections - Not Started

### Phase 1: Translation (60 sticks total, 6 sticks per batch):
- ⏳ Batch 01 (Sticks 1-6) - Not Started
- ⏳ Batch 02 (Sticks 7-12) - Not Started
- ⏳ Batch 03 (Sticks 13-18) - Not Started
- ⏳ Batch 04 (Sticks 19-24) - Not Started
- ⏳ Batch 05 (Sticks 25-30) - Not Started
- ⏳ Batch 06 (Sticks 31-36) - Not Started
- ⏳ Batch 07 (Sticks 37-42) - Not Started
- ⏳ Batch 08 (Sticks 43-48) - Not Started
- ⏳ Batch 09 (Sticks 49-54) - Not Started
- ⏳ Batch 10 (Sticks 55-60) - Not Started

### Translation Notes & Learnings:
- [Will be populated as project progresses]
- Always maintain standard format order: Sacred Meaning before Fortune Poem
- **CRITICAL:** Phase 0 OCR extraction MUST be completed and user-approved before starting Phase 1 translations
- **IMPORTANT:** All translations in Phase 1 will use `mazu_fortune_sticks_chinese_ocr.md` as the canonical source
- **EFFICIENCY:** OCR only needs to be done ONCE - all future phases use the saved OCR file

---

## Source Material

- 60 JPG images of fortune sticks from Thien Hau Temple (Los Angeles)
- System: 六十甲子籤 (60 Jiazi Divination Sticks)
- Each image contains: stick number, fortune rating, sacred meaning (聖意), and a 4-line poem
- Images are high quality; some may have slight angles but should be readable

---

## Phase 0: OCR Extraction & Verification

**CRITICAL:** This phase MUST be completed FIRST before any translation work begins.

### Objective:
Extract Chinese text from all 60 images and save to a single markdown file that will serve as the canonical source for all future translation work.

### Process:

1. **Process all 60 images in order (001.jpg through 060.jpg)**
2. **Extract Chinese text from each image:**
   - Stick number and Jiazi designation (e.g., 第一籤 甲子)
   - Fortune rating (e.g., 上上, 中吉)
   - Sacred meaning (聖意) - typically 8 items
   - Poem (籤詩) - 4 lines of classical Chinese

3. **Perform OCR verification for each stick:**

   **OCR Verification Steps (CRITICAL - NO CANONICAL SOURCES AVAILABLE):**

   Since Mazu fortune sticks vary by temple, you MUST perform these verification steps:

   a. **Poetic Structure Validation:**
      - Verify 4-line structure
      - Check character count per line (typically 7 characters)
      - Validate rhyme scheme (lines 2 and 4 typically rhyme)
      - Flag any structural inconsistencies

   b. **Character Plausibility Check:**
      - Look for unusual/rare characters that may indicate OCR errors
      - Common OCR confusion pairs: 己/已/巳, 未/末, 土/士, 天/夫
      - Flag any characters that seem out of context

   c. **Web Search Validation (Limited):**
      - Search for "媽祖靈籤 第X籤" or "六十甲子籤 第X籤"
      - Search for specific unusual phrases or character combinations
      - Note: Results may vary as different temples use different texts
      - Document if you find similar text from other sources

   d. **Grammatical Coherence:**
      - Does the poem make grammatical sense in classical Chinese?
      - Does the sacred meaning follow standard patterns?
      - Are there any obvious nonsensical phrases?

4. **Assign confidence level** (HIGH/MEDIUM/LOW/FLAGGED):
   - **HIGH CONFIDENCE:** Structure valid, no unusual characters, web matches found, grammatically sound
   - **MEDIUM CONFIDENCE:** Structure valid, grammatically sound, but no web matches OR minor unusual characters
   - **LOW CONFIDENCE:** Structural issues, unusual characters, or grammatical problems
   - **FLAGGED:** Requires immediate user verification before proceeding

5. **Save all OCR results to: `mazu_fortune_sticks_chinese_ocr.md`**

### OCR Output Format:

```markdown
# 媽祖靈籤 - 六十甲子籤
# Mazu Fortune Sticks - 60 Jiazi Divination System
# Thien Hau Temple, Los Angeles

Source: OCR extraction from 60 JPG images
Last updated: [DATE]

---

## 第一籤 甲子 上上

**OCR Confidence:** HIGH

**聖意:**
病即安、財必得、名可成、行人至、婚必合、禍自消、福自來、訟得理

**籤詩:**
[Line 1 - 7 characters]
[Line 2 - 7 characters]
[Line 3 - 7 characters]
[Line 4 - 7 characters]

**OCR Notes:**
- Structure: 4 lines, 7 chars each ✓
- Rhyme scheme: Lines 2 & 4 rhyme ✓
- Web verification: Found similar text at [URL]
- Unusual characters: None
- User corrections: [None or list corrections]

---

## 第二籤 乙丑 中吉

**OCR Confidence:** MEDIUM

**聖意:**
[sacred meaning text]

**籤詩:**
[Line 1]
[Line 2]
[Line 3]
[Line 4]

**OCR Notes:**
- Structure: 4 lines, 7 chars each ✓
- Rhyme scheme: Lines 2 & 4 rhyme ✓
- Web verification: No exact matches found, but similar phrasing in [source]
- Unusual characters: Character "X" in line 2 - uncommon but contextually valid
- User corrections: [None or list corrections]

---

[... Continue for all 60 sticks ...]
```

### After OCR Extraction:

1. **Present summary to user:**
   - Total sticks extracted: 60/60
   - Confidence breakdown: X HIGH, Y MEDIUM, Z LOW, W FLAGGED
   - List all FLAGGED items for immediate review
   - List all LOW/MEDIUM confidence items for review

2. **User reviews and provides corrections**

3. **Update `mazu_fortune_sticks_chinese_ocr.md` with corrections**

4. **Mark Phase 0 as COMPLETE**

5. **BEGIN Phase 1 translations using the verified OCR file**

---

## Phase 1: Translation Using Verified OCR

**IMPORTANT:** Do NOT re-OCR images. Use `mazu_fortune_sticks_chinese_ocr.md` as your source.

---

## Your Task For Each Stick (Phase 1)

### 1. Read from Verified OCR File

**Source:** `mazu_fortune_sticks_chinese_ocr.md` (created and verified in Phase 0)

For each stick in your current batch, extract from the OCR file:
- **Stick number** (e.g., 1, 15, 60)
- **Jiazi designation** (e.g., 甲子, 乙丑, etc.)
- **Fortune rating** (e.g., 上上, 中吉, etc.)
- **Sacred meaning section** (聖意) - typically 8 items
- **Poem** - 4 lines of classical Chinese

---

### 2. Map Fortune Rating

Use this fixed mapping table (same as Guan Yu):

| Chinese | Vietnamese | English | Subtitle EN | Subtitle VN |
|---------|------------|---------|-------------|-------------|
| 大吉 | Đại Cát | Great Fortune | (Excellent / Very Auspicious) | (Rất tốt / Đại cát) |
| 上上 | Thượng Thượng | Supreme Fortune | (Excellent / Very Auspicious) | (Rất tốt / Đại cát) |
| 上吉 | Thượng Cát | Upper Fortune | (Good / Auspicious) | (Tốt / Cát) |
| 中吉 | Trung Cát | Middle Fortune | (Moderate / Fairly Auspicious) | (Khá tốt / Trung cát) |
| 中平 | Trung Bình | Average Fortune | (Neutral / Mixed) | (Bình thường / Trung bình) |
| 中下 | Trung Hạ | Below Average | (Caution Advised) | (Cần cẩn thận) |
| 下下 | Hạ Hạ | Poor Fortune | (Unfavorable / Caution) | (Không thuận / Cần đề phòng) |

---

### 3. Translate Sacred Meaning (聖意)

Use these fixed label mappings (same as Guan Yu):

| Chinese | Vietnamese | English |
|---------|------------|---------|
| 病 | Sức khỏe | Health |
| 財 | Tài lộc | Wealth |
| 名 | Danh tiếng | Reputation |
| 行人 | Người đi xa / Di chuyển | Travel / Movement |
| 婚 | Hôn nhân | Marriage |
| 禍 | Tai họa | Misfortune |
| 福 | Phúc lộc | Blessings |
| 訟 | Kiện tụng | Litigation |

**Translation style:** Interpretive, not literal. Translate the meaning/implication, not word-for-word.

**Format:** Each item has a **bold label** and normal text value.

**Example:**
- Chinese: 病即安
- English: **Health:** safety and recovery
- Vietnamese: **Sức khỏe:** sẽ bình an

---

### 4. Translate Poem

**Structure:** Keep faithful to original 4-line structure. Do not expand to 8 lines.

**Style for Vietnamese:** Balance poetic flow with accurate meaning. Aim for natural Vietnamese that captures the essence. Light rhyme/rhythm is good but don't sacrifice meaning for it.

**Style for English:** Clear, accessible translation that preserves the imagery and meaning of the original.

---

### 5. Generate Interpretation

**Process:**
1. First, use your knowledge to interpret the stick based on the poem and sacred meaning
2. Cross-reference with web search (e.g., "媽祖靈籤第X籤解籤" or "六十甲子籤第X籤")
3. **IMPORTANT:** Web results may vary between temples - use them as guidance, not absolute truth
4. If you find multiple interpretations, note the variation in your call-outs

**Format:** Exactly 3 bullet points, maximum 3 lines each

**Tone:** Match the fortune level:
- Good fortunes (大吉, 上上, 上吉): Positive, encouraging
- Middle fortunes (中吉, 中平): Balanced, practical advice
- Poor fortunes (中下, 下下): Cautionary but constructive, not doom-and-gloom

---

## Output Format Per Stick (Phase 1 Translation Batches)

Output each stick with English and Vietnamese translations completely separated. Do NOT include original Chinese text. Do NOT interlace languages.

```
===========================================
STICK #[NUMBER] - [JIAZI DESIGNATION]
===========================================

### ENGLISH TRANSLATION

[Rating] ([Subtitle])

**Sacred Meaning:**
- **Health:** [translation]
- **Wealth:** [translation]
- **Reputation:** [translation]
- **Travel / Movement:** [translation]
- **Marriage:** [translation]
- **Misfortune:** [translation]
- **Blessings:** [translation]
- **Litigation:** [translation]

**Fortune Poem:**
[Line 1]
[Line 2]
[Line 3]
[Line 4]

**Interpretation:**
• [Point 1 - max 3 lines]
• [Point 2 - max 3 lines]
• [Point 3 - max 3 lines]

---

### VIETNAMESE TRANSLATION

[Rating] ([Subtitle])

**Sacred Meaning:**
- **Sức khỏe:** [translation]
- **Tài lộc:** [translation]
- **Danh tiếng:** [translation]
- **Người đi xa / Di chuyển:** [translation]
- **Hôn nhân:** [translation]
- **Tai họa:** [translation]
- **Phúc lộc:** [translation]
- **Kiện tụng:** [translation]

**Bài thơ quẻ:**
[Line 1]
[Line 2]
[Line 3]
[Line 4]

**Ý nghĩa:**
• [Point 1 - max 3 lines]
• [Point 2 - max 3 lines]
• [Point 3 - max 3 lines]

---

### CALL-OUTS (If Applicable)

[Document any translation choices, interpretation sources, or notable findings]
```

---

## Output Files

**IMPORTANT:** Save files to avoid session limits.

### Phase 0 Output:
- **OCR File:** `mazu_fortune_sticks_chinese_ocr.md` - Contains all 60 sticks with Chinese text only
  - This file serves as the canonical source for all future translation work
  - Must be user-verified and approved before Phase 1 begins

### Phase 1 Output (Translation Batch Files):

After translating each batch of 6, save to:
- `batch_01_sticks_001-006.md`
- `batch_02_sticks_007-012.md`
- `batch_03_sticks_013-018.md`
- ... and so on through batch_10_sticks_055-060.md

---

## Batch Process

### Phase 0 Process:
1. **Process all 60 images** at once
2. **Extract and verify OCR** for each stick
3. **Save complete OCR file** with all 60 sticks
4. **Present summary** to user with confidence breakdown
5. **User reviews and provides corrections**
6. **Update OCR file** with corrections
7. **Get user approval** to proceed to Phase 1

### Phase 1 Process:
1. **Batch size:** 6 sticks per batch (60 total ÷ 10 batches)
2. **Source:** Read Chinese text from `mazu_fortune_sticks_chinese_ocr.md` (do NOT re-OCR images)
3. **After each batch:**
   - Translate all 6 sticks (English + Vietnamese)
   - Generate interpretations based on web research
   - Present translations
   - **MANDATORY:** Wait for user confirmation before proceeding
4. **Learn from feedback:** Apply user corrections and preferences to future batches

---

## When to Ask User

### Phase 0 (OCR Extraction):
**ALWAYS ask user for:**
- Any FLAGGED items (before saving to OCR file)
- MEDIUM confidence items (list in summary for review)
- LOW confidence items (list in summary for review)
- Any unusual characters or structural issues
- Anything you're less than 90% confident about

### Phase 1 (Translation):
**ALWAYS ask user for:**
- Discrepancies between multiple web interpretation sources
- Translation choices that could go multiple ways
- Unclear metaphors or cultural references
- Anything you're less than 90% confident about

**Do NOT guess.** Flag it and ask.

---

## OCR Confidence Guidelines

### HIGH CONFIDENCE (Proceed with translation):
✅ 4-line poem structure intact
✅ 7-character lines (or consistent pattern)
✅ Lines 2 & 4 rhyme
✅ No unusual/rare characters
✅ Grammatically coherent
✅ Web search found matching or very similar text

### MEDIUM CONFIDENCE (Translate, but flag for user review):
⚠️ Structure valid BUT no web matches found
⚠️ OR 1-2 unusual characters that make contextual sense
⚠️ OR web sources show minor variations
⚠️ Grammatically sound but uncommon phrasing

### LOW CONFIDENCE (Translate, but clearly mark uncertainties):
⚠️ Multiple unusual characters
⚠️ OR structural inconsistencies
⚠️ OR grammatical issues
⚠️ OR no web validation possible

### FLAGGED (STOP - Get user verification before translating):
🚫 Poem structure broken (not 4 lines, wildly varying character counts)
🚫 OR obviously nonsensical characters/phrases
🚫 OR critical uncertainty about stick number or rating
🚫 OR multiple major OCR issues in single stick

---

## Files Provided

1. **60 JPG images** - Named by stick number (e.g., 001.jpg, 015.jpg, 060.jpg)
2. **Design templates** - Will be copied from Guan Yu project:
   - `design_template.html` (English/Vietnamese two-column)
   - `design_template_chinese.html` (Chinese single-column)

---

## Phase Summary

**⏳ Phase 0 - OCR Extraction (NOT STARTED)**
- Extract Chinese text from all 60 JPG images
- Perform OCR verification with confidence levels
- Save to `mazu_fortune_sticks_chinese_ocr.md`
- Get user review and approval
- Output: 1 markdown file (canonical Chinese source)

**⏳ Phase 1 - Translation (NOT STARTED)**
- Translate 60 sticks in batches of 6 (10 batches total)
- Source: `mazu_fortune_sticks_chinese_ocr.md` (do NOT re-OCR images)
- Each batch requires user verification before proceeding
- Output: 10 markdown files (`batch_01_sticks_001-006.md` through `batch_10_sticks_055-060.md`)

**📋 Phase 2 - HTML Generation (FUTURE)**
- Convert markdown translations to individual HTML files
- Generate both English/Vietnamese and Chinese versions
- Source for Chinese: `mazu_fortune_sticks_chinese_ocr.md`
- Use same templates as Guan Yu project
- Output: 120 HTML files (60 English/Vietnamese + 60 Chinese)

**📄 Phase 3 - PDF Conversion (FUTURE)**
- Convert HTML to PDF using Chrome headless
- Apply lessons learned from Guan Yu project:
  - ✅ CSS fixes for blank pages (`page-break-after: avoid`, `overflow: hidden`)
  - ✅ Virtual-time-budget flag for Chinese fonts (`--virtual-time-budget=10000`)
- Output: 122 PDF files (120 individual + 2 merged)

---

## Critical Lessons from Guan Yu Project

**Apply these fixes from the start:**

### 1. PDF Blank Pages Prevention
Already fixed in templates - ensure they're not modified:
```css
@media print {
  .page {
    page-break-after: avoid;  /* CRITICAL */
    overflow: hidden;          /* CRITICAL */
  }
}
```

### 2. Chinese PDF Font Loading
Use `--virtual-time-budget=10000` flag in PDF conversion scripts

### 3. Template String Handling
All CSS curly braces must be escaped (`{{` and `}}`) for Python `.format()`

### 4. Number Formatting
- English/Vietnamese: Use regular numbers (1-60)
- Chinese: Use regular numbers (1-60), NOT Roman numerals

**See Guan Yu project README.md "Critical Technical Issues & Solutions" for full details.**

---

## Begin Phase 0

**First Step: OCR Extraction**

When user provides the 60 JPG images:

1. **Process all 60 images** (001.jpg through 060.jpg)
2. **Extract Chinese text** for each stick following the OCR format above
3. **Perform verification** for each stick with confidence levels
4. **Save complete file** to `mazu_fortune_sticks_chinese_ocr.md`
5. **Present summary** to user:
   - Total: 60/60 sticks extracted
   - Confidence breakdown: X HIGH, Y MEDIUM, Z LOW, W FLAGGED
   - List all items needing review
6. **Get user corrections** and update the OCR file
7. **Get user approval** before proceeding to Phase 1

**After Phase 0 Complete:**

Begin Phase 1 with Batch 01 (sticks 1-6). Use `mazu_fortune_sticks_chinese_ocr.md` as your source - do NOT re-OCR the images.
