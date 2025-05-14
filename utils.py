import PyPDF2
import yaml

def get_pdf_metadata(pdf_path):
    """Extract metadata from a PDF."""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        return reader.metadata, len(reader.pages)

def validate_bookmark_structure(data, path=""):
    """Recursively validate the bookmark structure with detailed error messages."""
    if not isinstance(data, dict):
        raise ValueError(f"{path} must be a dictionary (got {type(data).__name__})")
    
    required_keys = {'title', 'page_number'}
    missing_keys = required_keys - set(data.keys())
    if missing_keys:
        raise ValueError(f"{path} missing required keys: {missing_keys}")
    
    if not isinstance(data['title'], str):
        raise ValueError(f"{path}title must be a string")
    
    if isinstance(data['page_number'], str):
        if not data['page_number'].strip().isdigit() and not data['page_number'].isalpha():
            raise ValueError(f"{path}page_number must be numeric or roman numeral")
    elif not isinstance(data['page_number'], (int, float)):
        raise ValueError(f"{path}page_number must be a number or string")
    
    if 'children' in data:
        if not isinstance(data['children'], list):
            raise ValueError(f"{path}children must be a list")
        for i, child in enumerate(data['children']):
            validate_bookmark_structure(child, f"{path}children[{i}].")

def get_bookmark_structure(yaml_file):
    """Load and validate the YAML bookmark structure with detailed error reporting."""
    try:
        with open(yaml_file, 'r') as file:
            data = yaml.safe_load(file)
            if not isinstance(data, dict):
                raise ValueError("YAML root must be a dictionary")
            
            # Validate top-level structure
            if 'contents' not in data and 'chapters' not in data:
                raise ValueError("YAML must contain either 'contents' or 'chapters' key")
            
            contents = data.get('contents', data.get('chapters', []))
            if not isinstance(contents, list):
                raise ValueError("'contents'/'chapters' must be a list")
            
            # Validate offset
            offset = data.get('offset', 0)
            if not isinstance(offset, (int, float)):
                raise ValueError("offset must be a number")
            
            # Recursively validate all bookmarks
            for i, item in enumerate(contents):
                validate_bookmark_structure(item, f"contents[{i}].")
            
            return {
                'offset': offset,
                'contents': contents
            }
            
    except yaml.YAMLError as e:
        if hasattr(e, 'problem_mark'):
            line = e.problem_mark.line + 1
            column = e.problem_mark.column + 1
            raise ValueError(f"YAML syntax error at line {line}, column {column}: {str(e)}")
        raise ValueError(f"YAML parsing error: {str(e)}")
    except Exception as e:
        raise ValueError(f"Invalid YAML structure: {str(e)}")