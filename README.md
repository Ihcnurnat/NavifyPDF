# NavifyPDF: Table of Contents for PDFs

NavifyPDF is a Python project that allows you to generate a clickable Table of Contents (ToC) for PDFs based on a provided YAML structure. It also provides the functionality to replace an old PDF with a new version containing the generated ToC.

## Requirements

Before running the project, make sure you have the required dependencies installed. You can install them by running:

```bash
pip install -r requirements.txt
```

## 3. Run the Command

```bash
python main.py input.pdf output.pdf toc.yaml
```

### Examples 

```bash
    python main.py "/Users/runchitan/Desktop/NavifyPDF/OriginalBooks/VICTORIA_HOSKINS_NotesGIT.pdf" "/Users/runchitan/Desktop/NavifyPDF/OriginalBooks/VICTORIA_HOSKINS_NotesGIT_newtest1.pdf" "/Users/runchitan/Desktop/NavifyPDF/Bookmarks/example_bookmarks.yaml"
```

```bash
    python main.py "/Users/runchitan/Desktop/NavifyPDF/OriginalBooks/VICTORIA_HOSKINS_NotesGIT.pdf" "/Users/runchitan/Desktop/NavifyPDF/OriginalBooks/VICTORIA_HOSKINS_NotesGIT_newtest1.pdf" "/Users/runchitan/Desktop/NavifyPDF/Bookmarks/VICTORIA_HOSKINS_NotesGIT.yaml"
```

## 🚀 Workflow

### 1. Prepare Input Files
- **Original PDF** (e.g., `book.pdf`)
- **YAML ToC definition** (e.g., `toc.yaml`)

### 2. Create ToC YAML File
```yaml
offset: 0  # Page number adjustment (see below)
contents:
  - title: "Front Matter"
    page_number: 1
    children: []
  
  - title: "Chapter 1"
    page_number: 5
    children:
      - title: "Section 1.1"
        page_number: 6
```

## Why Empty `children: []` is Optional

In your YAML structure, empty `children` arrays can be omitted because:

1. **Default Behavior**: 
   - The parser treats missing `children` the same as empty `children: []`
   - Both cases indicate no further nesting

2. **Working Cases in Your Example**:
   ```yaml
   - title: "Definition 2.2."  # Works without children
     page_number: 4
   
   - title: "Example 2.3."     # Works with explicit empty children
     page_number: 5
     children: []