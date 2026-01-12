#!/bin/bash
# Convert all English/Vietnamese HTML files to PDF using Chrome headless mode
#
# Usage:
#     # Convert all files:
#     ./scripts/convert_html_to_pdf.sh
#
#     # Convert specific stick:
#     ./scripts/convert_html_to_pdf.sh --stick 42
#
#     # Convert range of sticks:
#     ./scripts/convert_html_to_pdf.sh --from 1 --to 10

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
INPUT_DIR="${PROJECT_ROOT}/output/htmls"
OUTPUT_DIR="${PROJECT_ROOT}/output/pdfs"

# Parse arguments
STICK=""
FROM=""
TO=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --stick)
            STICK="$2"
            shift 2
            ;;
        --from)
            FROM="$2"
            shift 2
            ;;
        --to)
            TO="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Check Chrome exists
if [ ! -f "$CHROME" ]; then
    echo "ERROR: Google Chrome not found at $CHROME"
    exit 1
fi

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Build file list
if [ -n "$STICK" ]; then
    # Single stick
    html_files="${INPUT_DIR}/stick_$(printf '%03d' $STICK).html"
    if [ ! -f "$html_files" ]; then
        echo "ERROR: File not found: $html_files"
        exit 1
    fi
    html_files=("$html_files")
elif [ -n "$FROM" ] && [ -n "$TO" ]; then
    # Range of sticks
    html_files=()
    for i in $(seq $FROM $TO); do
        file="${INPUT_DIR}/stick_$(printf '%03d' $i).html"
        if [ -f "$file" ]; then
            html_files+=("$file")
        fi
    done
else
    # All sticks (excluding Chinese)
    html_files=(${INPUT_DIR}/stick_[0-9][0-9][0-9].html)
fi

total_files=${#html_files[@]}
if [ $total_files -eq 0 ]; then
    echo "No HTML files found to convert"
    exit 1
fi

current=0
echo "Converting $total_files HTML files to PDF..."

for html_file in "${html_files[@]}"; do
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
        else
            echo ""
            echo "WARNING: Failed to convert $filename"
        fi
    fi
done

echo ""
echo "Conversion complete! Generated $current PDF files in $OUTPUT_DIR"
