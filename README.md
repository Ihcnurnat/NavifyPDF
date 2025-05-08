# NavifyPDF: Table of Contents for PDFs

NavifyPDF is a Python project that allows you to generate a clickable Table of Contents (ToC) for PDFs based on a provided YAML structure. It also provides the functionality to replace an old PDF with a new version containing the generated ToC.

## Requirements

Before running the project, make sure you have the required dependencies installed. You can install them by running:

```bash
pip install -r requirements.txt
```

## Examples 

```bash
    python main.py "/Users/runchitan/Desktop/NavifyPDF/OriginalBooks/VICTORIA_HOSKINS_NotesGIT.pdf" "/Users/runchitan/Desktop/NavifyPDF/OriginalBooks/VICTORIA_HOSKINS_NotesGIT_newtest1.pdf" "/Users/runchitan/Desktop/NavifyPDF/Bookmarks/example_bookmarks.yaml"
```

```bash
    python main.py "/Users/runchitan/Desktop/NavifyPDF/OriginalBooks/VICTORIA_HOSKINS_NotesGIT.pdf" "/Users/runchitan/Desktop/NavifyPDF/OriginalBooks/VICTORIA_HOSKINS_NotesGIT_newtest1.pdf" "/Users/runchitan/Desktop/NavifyPDF/Bookmarks/VICTORIA_HOSKINS_NotesGIT.yaml"
```