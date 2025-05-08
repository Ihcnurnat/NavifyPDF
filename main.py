import argparse
import PyPDF2
import yaml
from fpdf import FPDF
from utils import get_pdf_metadata, add_bookmarks_to_pdf, get_bookmark_structure

def load_yaml(yaml_file):
    """Load the bookmark structure from the YAML file."""
    with open(yaml_file, 'r') as file:
        return yaml.safe_load(file)

def add_toc_to_pdf(pdf_writer, toc_structure, parent_title='', offset=0):
    """Recursively add table of contents to the PDF with clickable links."""
    for chapter in toc_structure:
        if isinstance(chapter, dict):
            title = chapter['title']
            page_number = chapter['page_number'] - 1 + offset  # Adjust for 0-based index

            # Add the bookmark for the chapter
            bookmark = pdf_writer.add_outline_item(title, page_number)

            # Recursively add sections or subsections
            if 'sections' in chapter:
                add_toc_to_pdf(pdf_writer, chapter['sections'], parent_title=title, offset=offset)
            if 'subsections' in chapter:
                add_toc_to_pdf(pdf_writer, chapter['subsections'], parent_title=title, offset=offset)

        else:
            # Handle cases where the chapter is a string (shouldn't happen in expected format)
            print(f"Warning: Unexpected format for chapter: {chapter}")

def generate_pdf_with_clickable_toc(input_pdf, output_pdf, toc_structure):
    """Generate a PDF with a clickable table of contents."""
    pdf_writer = PyPDF2.PdfWriter()

    # Load input PDF
    with open(input_pdf, "rb") as input_file:
        pdf_reader = PyPDF2.PdfReader(input_file)

        # Add original PDF pages to the writer
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

    # Add bookmarks from the TOC structure
    add_toc_to_pdf(pdf_writer, toc_structure['chapters'], offset=toc_structure.get('offset', 0))

    # Write the output PDF
    with open(output_pdf, "wb") as output_file:
        pdf_writer.write(output_file)

def main():
    """Main function to process the PDF and add TOC."""
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Generate PDF with Table of Contents (TOC)")
    parser.add_argument("input_pdf", help="Path to the input PDF")
    parser.add_argument("output_pdf", help="Path to the output PDF (use the same for replacing)")
    parser.add_argument("yaml_file", help="Path to the YAML file containing TOC structure")
    
    args = parser.parse_args()

    # Load the bookmark structure from YAML file
    toc_structure = load_yaml(args.yaml_file)

    # Generate the PDF with the clickable TOC
    generate_pdf_with_clickable_toc(args.input_pdf, args.output_pdf, toc_structure)

if __name__ == "__main__":
    main()
