# NavifyPDF: Table of Contents for PDFs

NavifyPDF is a Python project that allows you to generate a clickable Table of Contents (ToC) for PDFs based on a provided YAML structure. It also provides the functionality to replace an old PDF with a new version containing the generated ToC.

## Requirements

Before running the project, make sure you have the required dependencies installed. You can install them by running:

```bash
pip install -r requirements.txt
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

#### Use ChatGPT or Deepseek fot .yaml

Use the following prompt for .yaml generation

```markdown
**Task:** Generate a YAML table of contents (ToC) with the following specifications:  

1. **Structure**:  
   - Use `offset: 17` (adjust if needed)  
   - Start with "Front Matter" (`page_number: -16`) and "Contents" (`page_number: -6`)  
   - Format chapters as `"Chapter X: Title"` (not "CHAPTER X")  
   - Include all sections/sub-sections as nested `children` arrays  

2. **Input**:  
   ```text
   [PASTE THE CONTENTS PAGE OF YOUR PDF HERE]
```


### **How to Use This Prompt**  
1. Copy the prompt above.  
2. When you need a ToC, paste the prompt into your request *followed by* the contents page text from your PDF.  
3. I’ll generate a YAML ToC with:  
   - Correct offset/page numbers  
   - Nested sections  
   - Math-friendly formatting  

Let me know if you’d like any adjustments to the prompt!



### 3. Run the Command
You'll specify both the input and output. Then define the offset you want. Here offset is the distance between the first page of .pdf and the first page printed, under the assumption that .pdf increase exactly at the same speed of the printed page number. 
```bash
python main.py <input.pdf> <output.pdf> <bookmarks_toc.yaml>
```

#### Examples 

```bash
    python main.py "VICTORIA_HOSKINS_NotesGIT.pdf" "VICTORIA_HOSKINS_NotesGIT_new.pdf" "VICTORIA_HOSKINS_NotesGIT.yaml"
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