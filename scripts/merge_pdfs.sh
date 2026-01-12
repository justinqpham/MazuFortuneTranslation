#!/bin/bash
# Merge all individual PDF files into complete collections
#
# Usage:
#     # Merge all PDFs:
#     ./scripts/merge_pdfs.sh
#
#     # Merge only English/Vietnamese:
#     ./scripts/merge_pdfs.sh --english
#
#     # Merge only Chinese:
#     ./scripts/merge_pdfs.sh --chinese

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

PDF_DIR="${PROJECT_ROOT}/output/pdfs"
OUTPUT_DIR="${PROJECT_ROOT}/output"

# Parse arguments
MERGE_ENGLISH=true
MERGE_CHINESE=true

while [[ $# -gt 0 ]]; do
    case $1 in
        --english)
            MERGE_CHINESE=false
            shift
            ;;
        --chinese)
            MERGE_ENGLISH=false
            shift
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Check ghostscript exists
if ! command -v gs &> /dev/null; then
    echo "ERROR: Ghostscript (gs) not found"
    echo "Install with: brew install ghostscript"
    exit 1
fi

# Check PDF directory exists
if [ ! -d "$PDF_DIR" ]; then
    echo "ERROR: PDF directory not found: $PDF_DIR"
    echo "Run the PDF conversion scripts first"
    exit 1
fi

# Merge English/Vietnamese PDFs
if [ "$MERGE_ENGLISH" = true ]; then
    echo "Merging English/Vietnamese PDFs..."
    OUTPUT_EN="${OUTPUT_DIR}/Mazu_Fortune_Sticks_Complete.pdf"

    # Get sorted list of English/Vietnamese PDFs (exclude Chinese)
    pdf_files=$(ls ${PDF_DIR}/stick_[0-9][0-9][0-9].pdf 2>/dev/null | sort -V)

    if [ -z "$pdf_files" ]; then
        echo "WARNING: No English/Vietnamese PDF files found"
    else
        count=$(echo "$pdf_files" | wc -l | tr -d ' ')
        echo "Found $count English/Vietnamese PDF files"

        gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite \
           -sOutputFile="$OUTPUT_EN" \
           $pdf_files

        if [ $? -eq 0 ]; then
            file_size=$(ls -lh "$OUTPUT_EN" | awk '{print $5}')
            echo "Created: $OUTPUT_EN ($file_size)"
        else
            echo "ERROR: Failed to merge English/Vietnamese PDFs"
        fi
    fi
fi

# Merge Chinese PDFs
if [ "$MERGE_CHINESE" = true ]; then
    echo ""
    echo "Merging Chinese PDFs..."
    OUTPUT_CN="${OUTPUT_DIR}/Mazu_Fortune_Sticks_Chinese_Complete.pdf"

    # Get sorted list of Chinese PDFs
    pdf_files_cn=$(ls ${PDF_DIR}/stick_*_chinese.pdf 2>/dev/null | sort -V)

    if [ -z "$pdf_files_cn" ]; then
        echo "WARNING: No Chinese PDF files found"
    else
        count=$(echo "$pdf_files_cn" | wc -l | tr -d ' ')
        echo "Found $count Chinese PDF files"

        gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite \
           -sOutputFile="$OUTPUT_CN" \
           $pdf_files_cn

        if [ $? -eq 0 ]; then
            file_size=$(ls -lh "$OUTPUT_CN" | awk '{print $5}')
            echo "Created: $OUTPUT_CN ($file_size)"
        else
            echo "ERROR: Failed to merge Chinese PDFs"
        fi
    fi
fi

echo ""
echo "Merge complete!"
