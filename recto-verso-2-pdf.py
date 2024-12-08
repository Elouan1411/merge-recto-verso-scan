import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs():
    # Open file dialog to select first PDF
    file1 = filedialog.askopenfilename(
        title="Select the first PDF (odd pages)", 
        filetypes=[("PDF files", "*.pdf")]
    )
    if not file1:
        return

    # Open file dialog to select second PDF
    file2 = filedialog.askopenfilename(
        title="Select the second PDF (even pages in reverse order)", 
        filetypes=[("PDF files", "*.pdf")]
    )
    if not file2:
        return

    try:
        # Read PDFs
        reader1 = PdfReader(file1)
        reader2 = PdfReader(file2)
        writer = PdfWriter()

        # Reverse the pages of the second PDF
        reversed_pages = list(reader2.pages)[::-1]

        # Merge pages alternately
        max_pages = max(len(reader1.pages), len(reversed_pages))
        for i in range(max_pages):
            if i < len(reader1.pages):
                writer.add_page(reader1.pages[i])
            if i < len(reversed_pages):
                writer.add_page(reversed_pages[i])

        # Save output PDF
        output_file = filedialog.asksaveasfilename(
            title="Save Merged PDF As",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")]
        )
        if output_file:
            with open(output_file, "wb") as output:
                writer.write(output)
            messagebox.showinfo("Success", "PDF created successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the GUI
root = tk.Tk()
root.title("PDF Merger")
root.minsize(400, 200)  # Set minimum window size

# Add a label and button
label = tk.Label(root, text="Merge PDF files for double-sided scanning")
label.pack(pady=20)

merge_button = tk.Button(root, text="Merge PDFs", command=merge_pdfs)
merge_button.pack(pady=20)

# Run the application
root.mainloop()
