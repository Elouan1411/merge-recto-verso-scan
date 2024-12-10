# merge-recto-verso-scan

PDF Merger for Scanner is a tool that helps users combine scanned PDF files (front and back) into a properly ordered double-sided document. If your computer doesn't have Python or you don't want to install dependencies, you can use the ready-to-use executable files for Linux or Windows. Ideal for printers and scanners that don't support automatic duplex scanning, this program merges odd and even pages into one seamless PDF.

## Features

- Choose between two options for merging:
  - **Two separate PDFs**: One for odd pages (front side) and one for even pages (back side, scanned in reverse order).
  - **Single PDF**: One PDF containing all odd pages first, followed by all even pages in reverse order.
- Automatically merge pages to generate a properly ordered double-sided PDF.
- Intuitive graphical user interface.
- Save the merged file as a PDF.

## Use the Executables (if you don't have Python or dependencies)

If your computer doesn't have Python installed or you prefer not to install dependencies, you can use the ready-to-use executable files for **Linux** or **Windows**.  
These executables are available in the `releases` section of the repository.

## Requirements

- **Python 3.7 or later**
- Required Python libraries:
  - `tkinter` (included with Python)
  - `PyPDF2` (must be installed)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Elouan1411/merge-recto-verso-scan.git
   ```

2. Install the dependencies:

   ```bash
   pip install PyPDF2
   ```

3. Run the application:
   ```bash
   python3 recto-verso-2-pdf.py
   ```

## Usage

1. Launch the application.
2. Choose one of the following options:
   - **Two separate PDFs**:
     1. Select the file containing the **odd pages (front side)**.
     2. Select the file containing the **even pages (back side)** (scanned in reverse order).
   - **Single PDF**:
     1. Select a PDF file that contains all **odd pages first**, followed by all **even pages in reverse order**.
3. Choose a location and name to save the merged PDF file.

## Example Workflow

### Option 1: Two separate PDFs

1. **Scan the front side**: Scan all odd-numbered pages into a PDF file in order.
2. **Scan the back side**: Flip the stack of paper and scan all even-numbered pages into another PDF file (usually starting from the last page).
3. Use the application to combine both files into a final document with the correct order.

### Option 2: Single PDF

1. **Scan the front side**: Scan all odd-numbered pages first.
2. **Scan the back side**: Continue scanning all even-numbered pages in reverse order into the same file.
3. Use the application to merge the pages automatically.

---

This tool makes double-sided PDF creation easy and accessible for anyone using manual duplex scanning. 🎉
