import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger
from PIL import Image
import os
import tempfile

def merge_pdfs_and_images():
    # Seleccionar archivos PDF o JPG/PNG
    files = filedialog.askopenfilenames(
        filetypes=[("Archivos PDF e Imágenes", "*.pdf;*.jpg;*.jpeg;*.png")]
    )

    if not files:
        return

    merger = PdfMerger()
    temp_files = [] 

    try:
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in [".pdf"]:
                merger.append(file)
            elif ext in [".jpg", ".jpeg", ".png"]:
                # Convertir imagen a PDF temporalmente
                image = Image.open(file).convert("RGB")
                temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
                image.save(temp_pdf.name, "PDF", resolution=100.0)
                temp_files.append(temp_pdf.name)
                merger.append(temp_pdf.name)

        # Guardar archivo combinado
        output_path = filedialog.asksaveasfilename(
            defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")]
        )
        if output_path:
            merger.write(output_path)
            messagebox.showinfo("Éxito", "PDFs e imágenes combinados con éxito.")
        merger.close()

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

    finally:
        # Borrar los archivos temporales
        for temp in temp_files:
            try:
                os.remove(temp)
            except:
                pass

# Interfaz Tkinter
root = tk.Tk()
root.title("Combinar PDFs e Imágenes")

button = tk.Button(root, text="Combinar PDFs/JPGs", command=merge_pdfs_and_images)
button.pack(pady=10, padx=10)

root.mainloop()
