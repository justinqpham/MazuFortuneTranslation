#!/usr/bin/env python3
"""
Generate HTML files for Mazu Fortune Sticks

Usage:
    # Generate all sticks from all batch files:
    python3 scripts/generate_html.py

    # Generate specific batch only:
    python3 scripts/generate_html.py --batch 01

    # Generate specific stick only:
    python3 scripts/generate_html.py --stick 42

    # Generate Chinese HTML files:
    python3 scripts/generate_html.py --chinese
"""

import os
import re
import argparse
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent

def parse_batch_file(md_file_path):
    """Parse a batch markdown file and extract data for each stick

    Supports two formats:
    1. Standard format: ===STICK #N=== with ### ENGLISH/VIETNAMESE sections
    2. Alternative format: ## Stick #N - Rating (English only, needs Vietnamese added)
    """
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    parsed_sticks = []

    # Try standard format first (batches 1-9)
    sticks = re.split(r'=+\nSTICK #(\d+)\n=+', content)

    if len(sticks) > 1:
        # Standard format detected
        for i in range(1, len(sticks), 2):
            stick_num = int(sticks[i])
            stick_content = sticks[i + 1]

            # Extract English section
            en_match = re.search(r'### ENGLISH TRANSLATION\n\n(.*?)\n---\n\n### VIETNAMESE TRANSLATION', stick_content, re.DOTALL)
            if not en_match:
                continue
            en_section = en_match.group(1)

            # Extract Vietnamese section
            vn_match = re.search(r'### VIETNAMESE TRANSLATION\n\n(.*?)(?:\n---\n|$)', stick_content, re.DOTALL)
            if not vn_match:
                continue
            vn_section = vn_match.group(1)

            # Parse English rating and subtitle
            en_rating_match = re.match(r'([^\(]+)\s*\(([^\)]+)\)', en_section.strip())
            en_rating = en_rating_match.group(1).strip() if en_rating_match else ""
            en_subtitle = en_rating_match.group(2).strip() if en_rating_match else ""

            # Extract English poem
            en_poem_match = re.search(r'\*\*Fortune Poem:\*\*\n((?:(?!\*\*).+\n?)+)', en_section)
            en_poem = en_poem_match.group(1).strip() if en_poem_match else ""

            # Extract English interpretation
            en_interp_match = re.search(r'\*\*Interpretation:\*\*\n((?:(?!\*\*).+\n?)+)', en_section)
            en_interpretation = en_interp_match.group(1).strip() if en_interp_match else ""

            # Extract English extended interpretation (supports both • and - bullets)
            en_ext_match = re.search(r'\*\*Extended Interpretation:\*\*\n((?:[•\-][^\n]+\n?)+)', en_section)
            en_extended = en_ext_match.group(1).strip() if en_ext_match else ""

            # Parse Vietnamese rating and subtitle
            vn_rating_match = re.match(r'([^\(]+)\s*\(([^\)]+)\)', vn_section.strip())
            vn_rating = vn_rating_match.group(1).strip() if vn_rating_match else ""
            vn_subtitle = vn_rating_match.group(2).strip() if vn_rating_match else ""

            # Extract Vietnamese poem
            vn_poem_match = re.search(r'\*\*Bài Thơ Quẻ:\*\*\n((?:(?!\*\*).+\n?)+)', vn_section)
            vn_poem = vn_poem_match.group(1).strip() if vn_poem_match else ""

            # Extract Vietnamese interpretation
            vn_interp_match = re.search(r'\*\*Giải Quẻ:\*\*\n((?:(?!\*\*).+\n?)+)', vn_section)
            vn_interpretation = vn_interp_match.group(1).strip() if vn_interp_match else ""

            # Extract Vietnamese extended interpretation (supports both • and - bullets)
            vn_ext_match = re.search(r'\*\*Ý Nghĩa Mở Rộng:\*\*\n((?:[•\-][^\n]+\n?)+)', vn_section)
            vn_extended = vn_ext_match.group(1).strip() if vn_ext_match else ""

            parsed_sticks.append({
                'num': stick_num,
                'en_rating': en_rating,
                'en_subtitle': en_subtitle,
                'en_poem': en_poem,
                'en_interpretation': en_interpretation,
                'en_extended_interpretation': en_extended,
                'vn_rating': vn_rating,
                'vn_subtitle': vn_subtitle,
                'vn_poem': vn_poem,
                'vn_interpretation': vn_interpretation,
                'vn_extended_interpretation': vn_extended
            })
    else:
        # Try alternative format (batch 10 style - English only)
        # This format is incomplete (no Vietnamese) - print warning
        alt_sticks = re.split(r'\n## Stick #(\d+) - ([^\n]+)\n', content)

        if len(alt_sticks) > 1:
            print(f"  WARNING: {md_file_path} uses alternative format (English only, no Vietnamese)")
            print(f"  This batch needs to be reformatted to standard format before HTML generation")

    return parsed_sticks


def number_to_chinese(num):
    """Convert Arabic numeral to Chinese numeral (1-100)"""
    chinese_digits = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']

    if num <= 0 or num > 100:
        return str(num)

    if num == 10:
        return '十'
    elif num < 10:
        return chinese_digits[num]
    elif num < 20:
        return '十' + chinese_digits[num - 10]
    elif num == 100:
        return '一百'
    elif num % 10 == 0:
        return chinese_digits[num // 10] + '十'
    else:
        return chinese_digits[num // 10] + '十' + chinese_digits[num % 10]


def parse_ocr_file(ocr_file_path):
    """Parse an OCR markdown file and extract Chinese data for each stick"""
    with open(ocr_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by stick sections (## 第X籤)
    sections = re.split(r'\n## (第\d+籤\s+[上中下]籤)\n', content)[1:]

    sticks = []
    for i in range(0, len(sections), 2):
        if i + 1 >= len(sections):
            break

        header = sections[i]
        body = sections[i + 1]

        # Extract stick number and rating
        match = re.match(r'第(\d+)籤\s+([上中下]籤)', header)
        if not match:
            continue

        stick_num = int(match.group(1))
        rating = match.group(2)

        # Extract poem
        poem_match = re.search(r'\*\*籤詩:\*\*\n((?:(?!\*\*).+\n?)+)', body)
        poem = poem_match.group(1).strip() if poem_match else ''

        # Extract interpretation
        interp_match = re.search(r'\*\*解曰:\*\*\n((?:(?!\*\*).+\n?)+)', body)
        interpretation = interp_match.group(1).strip() if interp_match else ''

        sticks.append({
            'num': stick_num,
            'stick_num': f'第{number_to_chinese(stick_num)}籤',
            'rating': rating,
            'poem': poem,
            'interpretation': interpretation
        })

    return sticks


def format_extended_interpretation(text):
    """Convert markdown bullets to HTML list items (supports • and - bullets)"""
    lines = text.strip().split('\n')
    html_lines = []
    for line in lines:
        if line.startswith('•'):
            content = line[1:].strip()
            html_lines.append(f'          <li>{content}</li>')
        elif line.startswith('-'):
            content = line[1:].strip()
            html_lines.append(f'          <li>{content}</li>')
    return '\n'.join(html_lines)


def generate_bilingual_html(stick_data, template_path):
    """Generate English/Vietnamese HTML for a single stick"""
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    html = template.format(
        stick_num=stick_data['num'],
        en_rating=stick_data['en_rating'],
        en_subtitle=stick_data['en_subtitle'],
        en_poem=stick_data['en_poem'],
        en_interpretation=stick_data['en_interpretation'],
        en_extended_interpretation=format_extended_interpretation(stick_data['en_extended_interpretation']),
        vn_rating=stick_data['vn_rating'],
        vn_subtitle=stick_data['vn_subtitle'],
        vn_poem=stick_data['vn_poem'],
        vn_interpretation=stick_data['vn_interpretation'],
        vn_extended_interpretation=format_extended_interpretation(stick_data['vn_extended_interpretation'])
    )
    return html


def generate_chinese_html(stick_data, template_path):
    """Generate Chinese HTML for a single stick"""
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    html = template.format(
        stick_num=stick_data['stick_num'],
        rating=stick_data['rating'],
        poem=stick_data['poem'],
        interpretation=stick_data['interpretation']
    )
    return html


def get_batch_files():
    """Get all batch translation files from translations/ folder"""
    translations_dir = PROJECT_ROOT / 'translations'
    batch_files = []
    for i in range(1, 11):
        batch_num = f'{i:02d}'
        start = (i - 1) * 10 + 1
        end = i * 10
        filename = f'batch_{batch_num}_sticks_{start:03d}-{end:03d}.md'
        filepath = translations_dir / filename
        if filepath.exists():
            batch_files.append((batch_num, filepath))
    return batch_files


def get_ocr_files():
    """Get all OCR files from translations/ folder"""
    translations_dir = PROJECT_ROOT / 'translations'
    ocr_files = []
    for i in range(1, 11):
        batch_num = f'{i:02d}'
        start = (i - 1) * 10 + 1
        end = i * 10
        filename = f'ocr_batch_{batch_num}_sticks_{start:03d}-{end:03d}.md'
        filepath = translations_dir / filename
        if filepath.exists():
            ocr_files.append((batch_num, filepath))
    return ocr_files


def main():
    parser = argparse.ArgumentParser(description='Generate HTML files for Mazu Fortune Sticks')
    parser.add_argument('--batch', type=str, help='Generate specific batch only (e.g., 01)')
    parser.add_argument('--stick', type=int, help='Generate specific stick only (e.g., 42)')
    parser.add_argument('--chinese', action='store_true', help='Generate Chinese HTML files')
    parser.add_argument('--output-dir', type=str, default='.', help='Output directory (default: project root)')
    args = parser.parse_args()

    output_dir = Path(args.output_dir) if args.output_dir != '.' else PROJECT_ROOT

    if args.chinese:
        # Generate Chinese HTML files
        template_path = PROJECT_ROOT / 'templates' / 'design_template_chinese.html'
        if not template_path.exists():
            print(f"ERROR: Template not found: {template_path}")
            return

        ocr_files = get_ocr_files()
        if args.batch:
            ocr_files = [(b, f) for b, f in ocr_files if b == args.batch]

        all_sticks = []
        for batch_num, filepath in ocr_files:
            sticks = parse_ocr_file(filepath)
            all_sticks.extend(sticks)
            print(f"Parsed batch {batch_num}: {len(sticks)} sticks")

        if args.stick:
            all_sticks = [s for s in all_sticks if s['num'] == args.stick]

        for stick_data in all_sticks:
            html = generate_chinese_html(stick_data, template_path)
            output_path = output_dir / f"stick_{stick_data['num']:03d}_chinese.html"
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Generated: {output_path.name}")

        print(f"\nSuccessfully generated {len(all_sticks)} Chinese HTML files!")

    else:
        # Generate English/Vietnamese HTML files
        template_path = PROJECT_ROOT / 'templates' / 'design_template.html'
        if not template_path.exists():
            print(f"ERROR: Template not found: {template_path}")
            return

        batch_files = get_batch_files()
        if args.batch:
            batch_files = [(b, f) for b, f in batch_files if b == args.batch]

        all_sticks = []
        for batch_num, filepath in batch_files:
            sticks = parse_batch_file(filepath)
            all_sticks.extend(sticks)
            print(f"Parsed batch {batch_num}: {len(sticks)} sticks")

        if args.stick:
            all_sticks = [s for s in all_sticks if s['num'] == args.stick]

        for stick_data in all_sticks:
            html = generate_bilingual_html(stick_data, template_path)
            output_path = output_dir / f"stick_{stick_data['num']:03d}.html"
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Generated: {output_path.name}")

        print(f"\nSuccessfully generated {len(all_sticks)} HTML files!")


if __name__ == '__main__':
    main()
