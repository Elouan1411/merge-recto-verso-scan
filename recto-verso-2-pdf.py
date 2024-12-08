import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter


def merge_two_files():
    # Select the first PDF file (rectos)
    file1 = filedialog.askopenfilename(title="Select the PDF with odd pages (recto)", filetypes=[("PDF files", "*.pdf")])
    if not file1:
        return

    # Select the second PDF file (versos)
    file2 = filedialog.askopenfilename(title="Select the PDF with even pages (verso, reversed)", filetypes=[("PDF files", "*.pdf")])
    if not file2:
        return

    try:
        reader1 = PdfReader(file1)
        reader2 = PdfReader(file2)
        writer = PdfWriter()

        recto_pages = len(reader1.pages)
        verso_pages = len(reader2.pages)

        # Merge pages
        for i in range(recto_pages):
            writer.add_page(reader1.pages[i])  # Add recto
            if i < verso_pages:  # Add verso if it exists
                writer.add_page(reader2.pages[verso_pages - 1 - i])

        save_pdf(writer)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while merging: {e}")


def merge_single_file():
    # Select the single PDF file
    file = filedialog.askopenfilename(title="Select the PDF with all pages (rectos first, then reversed versos)", filetypes=[("PDF files", "*.pdf")])
    if not file:
        return

    try:
        reader = PdfReader(file)
        writer = PdfWriter()

        total_pages = len(reader.pages)
        mid = (total_pages + 1) // 2  # Adjust for odd number of pages
        rectos = reader.pages[:mid]
        versos = reader.pages[mid:][::-1]

        recto_pages = len(rectos)
        verso_pages = len(versos)

        # Merge pages
        for i in range(recto_pages):
            writer.add_page(rectos[i])  # Add recto
            if i < verso_pages:  # Add verso if it exists
                writer.add_page(versos[i])

        save_pdf(writer)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while merging: {e}")


def save_pdf(writer):
    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if save_path:
        with open(save_path, "wb") as output_file:
            writer.write(output_file)
        messagebox.showinfo("Success", "PDF successfully merged!")


def main():
    # Create the GUI
    root = tk.Tk()
    root.title("Merge Recto Verso PDF")
    root.minsize(300, 150)

    label = tk.Label(root, text="Choose how your pages are scanned:")
    label.pack(pady=10)

    button_two_files = tk.Button(root, text="Two separate PDFs", command=merge_two_files)
    button_two_files.pack(pady=5)

    button_single_file = tk.Button(root, text="Single PDF with rectos first", command=merge_single_file)
    button_single_file.pack(pady=5)

    button_exit = tk.Button(root, text="Exit", command=root.quit)
    button_exit.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
