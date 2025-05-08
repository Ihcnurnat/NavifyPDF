import argparse
import PyPDF2
import yaml
from utils import get_bookmark_structure

def generate_pdf_with_clickable_toc(input_pdf, output_pdf, toc_structure):
    """Generate a PDF with a clickable table of contents."""
    pdf_writer = PyPDF2.PdfWriter()

    with open(input_pdf, "rb") as input_file:
        pdf_reader = PyPDF2.PdfReader(input_file)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

    # Get items from either 'contents' or legacy 'chapters' key
    toc_items = toc_structure.get('contents', toc_structure.get('chapters', []))
    add_toc_to_pdf(pdf_writer, toc_items, offset=toc_structure.get('offset', 0))

    with open(output_pdf, "wb") as output_file:
        pdf_writer.write(output_file)

def add_toc_to_pdf(pdf_writer, toc_structure, parent=None, offset=0):
    """Recursively add table of contents with explicit children key support."""
    for item in toc_structure:
        if not isinstance(item, dict):
            continue

        title = item.get('title')
        page_number = item.get('page_number')
        if not title or page_number is None:
            continue

        # Add bookmark with parent reference
        bookmark = pdf_writer.add_outline_item(
            title,
            page_number - 1 + offset,  # Convert to 0-based and apply offset
            parent
        )

        # Process children if they exist
        children = item.get('children', [])
        if children:
            add_toc_to_pdf(pdf_writer, children, parent=bookmark, offset=offset)

def main():
    """Main function to process the PDF and add TOC."""
    parser = argparse.ArgumentParser(description="Generate PDF with Table of Contents (TOC)")
    parser.add_argument("input_pdf", help="Path to the input PDF")
    parser.add_argument("output_pdf", help="Path to the output PDF")
    parser.add_argument("yaml_file", help="Path to the YAML file containing TOC structure")
    
    args = parser.parse_args()
    toc_structure = get_bookmark_structure(args.yaml_file)
    generate_pdf_with_clickable_toc(args.input_pdf, args.output_pdf, toc_structure)

if __name__ == "__main__":
    main()