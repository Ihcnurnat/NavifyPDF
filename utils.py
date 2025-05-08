import PyPDF2
import yaml

def get_pdf_metadata(pdf_path):
    """Extract metadata from a PDF, such as page count and title."""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        metadata = reader.metadata
        page_count = len(reader.pages)
    return metadata, page_count

def add_bookmarks_to_pdf(pdf_writer, toc_structure, offset=0):
    """Add bookmarks to a PDF writer from a TOC structure."""
    for chapter in toc_structure:
        # Add a bookmark to the first page of the chapter
        page_number = chapter["page_number"] - 1 + offset  # Apply offset for correct page number
        pdf_writer.add_bookmark(
            chapter["title"],
            page_number  # Adjust for zero-indexed pages
        )

def get_bookmark_structure(yaml_file):
    """Load the structure of the bookmarks from a YAML file."""
    with open(yaml_file, 'r') as file:
        toc_structure = yaml.safe_load(file)
    return toc_structure
