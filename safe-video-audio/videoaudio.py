import os
import tkinter as tk
from tkinter import filedialog, messagebox
from yt_dlp import YoutubeDL

def descargar_video():
    url = entrada_url.get()
    carpeta_destino = filedialog.askdirectory()

    if not url or not carpeta_destino:
        messagebox.showwarning("Error", "Debe ingresar una URL y seleccionar una carpeta de destino.")
        return

    try:
        opciones = {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(carpeta_destino, '%(title)s.%(ext)s'),
            'noplaylist': True,
        }

        with YoutubeDL(opciones) as ydl:
            ydl.download([url])

        messagebox.showinfo("Éxito", "Video descargado correctamente.")

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al descargar el video: {str(e)}")

def descargar_audio():
    url = entrada_url.get()
    carpeta_destino = filedialog.askdirectory()

    if not url or not carpeta_destino:
        messagebox.showwarning("Error", "Debe ingresar una URL y seleccionar una carpeta de destino.")
        return

    try:
        opciones = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(carpeta_destino, '%(title)s.%(ext)s'),
        }

        with YoutubeDL(opciones) as ydl:
            ydl.download([url])

        messagebox.showinfo("Éxito", "Audio descargado correctamente.")

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al descargar el audio: {str(e)}")

# Crear ventana de Tkinter
ventana = tk.Tk()
ventana.title("Descargar Video/Audio de YouTube")

# Etiquetas y entradas
tk.Label(ventana, text="URL del Video:").pack(padx=10, pady=5)
entrada_url = tk.Entry(ventana, width=50)
entrada_url.pack(padx=10, pady=5)

# Botones
tk.Button(ventana, text="Descargar Video", command=descargar_video).pack(padx=10, pady=5)
tk.Button(ventana, text="Descargar Audio", command=descargar_audio).pack(padx=10, pady=5)

# Iniciar la ventana
ventana.mainloop()
