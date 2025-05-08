import PyPDF2
import yaml

def get_pdf_metadata(pdf_path):
    """Extract metadata from a PDF."""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        return reader.metadata, len(reader.pages)

def get_bookmark_structure(yaml_file):
    """Load and validate the YAML bookmark structure."""
    try:
        with open(yaml_file, 'r') as file:
            data = yaml.safe_load(file)
            if not isinstance(data, dict):
                raise ValueError("YAML root must be a dictionary")
            
            # Validate structure
            if 'contents' not in data and 'chapters' not in data:
                raise ValueError("YAML must contain 'contents' or 'chapters' key")
            
            if 'contents' in data and not isinstance(data['contents'], list):
                raise ValueError("'contents' must be a list")
                
            if 'chapters' in data and not isinstance(data['chapters'], list):
                raise ValueError("'chapters' must be a list")
            
            return {
                'offset': data.get('offset', 0),
                'contents': data.get('contents', data.get('chapters', []))
            }
    except yaml.YAMLError as e:
        print(f"YAML parsing error: {e}")
        raise
    except Exception as e:
        print(f"Error in YAML structure: {e}")
        raise