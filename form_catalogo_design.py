import os
import webbrowser
import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar, Button, END, Label, ttk

class CatalogoConstruccion:
    def __init__(self, panel_principal):
        self.panel_principal = panel_principal
        self.pdf_directory = r"C:\Users\DELL\OneDrive\Escritorio\PROYECTO\PDFS"  # Cambia esta ruta a donde están tus archivos PDF
        self.setup_ui()

    def setup_ui(self):
        self.panel_principal.title("Gestor de Libros PDF")
        ancho_ventana = 800
        alto_ventana = 600
        self.panel_principal.geometry(f"{ancho_ventana}x{alto_ventana}")
        self.panel_principal.configure(bg="lightgrey")

        # Frame principal
        frame_principal = tk.Frame(self.panel_principal, bg="lightblue")
        frame_principal.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        # Botón del menú desplegable
        boton_menu = tk.Menubutton(frame_principal, text="☰", relief="raised", font=("Helvetica", 14, "bold"))
        boton_menu.grid(row=0, column=0, pady=10, padx=10, sticky="nw")  # Alinea el botón a la parte superior izquierda
        boton_menu.menu = tk.Menu(boton_menu, tearoff=0)
        boton_menu["menu"] = boton_menu.menu
        boton_menu.menu.add_command(label="Página Principal", command=lambda: self.abrir_ventana("Página Principal"))
        boton_menu.menu.add_command(label="Libros", command=lambda: self.abrir_ventana("Libros"))
        boton_menu.menu.add_command(label="Audiolibros", command=lambda: self.abrir_ventana("Audiolibros"))
        boton_menu.menu.add_command(label="Descargas", command=lambda: self.abrir_ventana("Descargas"))

        # Etiqueta de Categorías
        label_categorias = Label(frame_principal, text="Categorías", font=("Helvetica", 16, "bold"), bg="lightpink")
        label_categorias.grid(row=1, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        # Combobox para seleccionar categoría
        categorias = ["Español", "Biologia", "Filosofia", "Matematicas", "Lectura", "Historia", "Quimica", "Fisica", "GUIAS"]
        self.categorias_combobox = ttk.Combobox(frame_principal, values=categorias, state="readonly", font=("Helvetica", 12))
        self.categorias_combobox.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        # Frame para la lista de libros PDF
        frame_libros = tk.Frame(frame_principal, bg="white", bd=2, relief="sunken")
        frame_libros.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

        scrollbar = Scrollbar(frame_libros)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = Listbox(frame_libros, yscrollcommand=scrollbar.set, width=70, height=15, font=("Helvetica", 12))
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=self.listbox.yview)

        # Botones para mostrar y abrir libros
        boton_mostrar = Button(frame_principal, text="Mostrar Libros", command=self.mostrar_libros, font=("Helvetica", 12), bg="lightblue")
        boton_mostrar.grid(row=4, column=0, pady=10, sticky="w")

        boton_abrir = Button(frame_principal, text="Abrir Libro", command=self.abrir_seleccion, font=("Helvetica", 12), bg="lightgreen")
        boton_abrir.grid(row=4, column=1, pady=10, sticky="e")

    def listar_pdfs(self, directory):
        """Lista todos los archivos PDF en el directorio dado."""
        return [f for f in os.listdir(directory) if f.endswith('.pdf')]

    def abrir_pdf(self, pdf_path):
        """Abre un archivo PDF con el visor predeterminado del sistema."""
        webbrowser.open(pdf_path)

    def mostrar_libros(self):
        """Muestra los archivos PDF en la lista según la categoría seleccionada."""
        categoria_seleccionada = self.categorias_combobox.get()
        libros_categoria = self.obtener_libros_por_categoria(categoria_seleccionada)
        self.listbox.delete(0, END)  # Limpiar la lista
        if not libros_categoria:
            messagebox.showinfo("Información", f"No se encontraron libros en la categoría '{categoria_seleccionada}'.")
            return
        for libro in libros_categoria:
            self.listbox.insert(END, libro)

    def abrir_seleccion(self):
        """Abre el archivo PDF seleccionado."""
        seleccion = self.listbox.curselection()
        if seleccion:
            pdf_to_open = os.path.join(self.pdf_directory, self.listbox.get(seleccion))
            self.abrir_pdf(pdf_to_open)
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un libro para abrir.")

    def obtener_libros_por_categoria(self, categoria):
        """Función simulada para obtener libros por categoría."""
        libros_por_categoria = {
            "Español": ["Manual-de-espanol-Tejiendo-el-espanol-A1.pdf", "ESPANOL-PARA-ESTRANJEROS-1.pdf", "Espanol_en_marcha_BasicoGuia_didactica.pdf"],
            "Biologia": ["biologia.PDF", "Biología: conceptos y fundamentos básicos.pdf", "Biologia Basica.pdf", "67707248.pdf"],
            "Filosofia": ["apuntes_de_filosofia_edincr.pdf", "La_Materia_Como_Categoria_Filosofica-K.pdf", "8448616006.pdf", "filosofia-i.pdf", "1461-2019-10-22-Las concepciones filosóficas de la materia_PDF .pdf"],
            "Matematicas": ["Geometria Analitica.pdf", "Matemáticas Básicas", "libro-blanco-de-las-matematicas.pdf", "Fundamentos de matematicas.pdf", "49e8f315f5a6b3cee6f01470e9093068.pdf", "matematicaipoli.pdf"],
            "Quimica": ["57_Propiedad_de_la_materia.pdf", "LibroQuimica.pdf", "EL002687.pdf", "QUIMICA.pdf", "Chang-QuimicaGeneral7thedicion.pdf", "quimica-i-unidad-i-1.pdf", "5_Quimica_General.pdf", "Quimica_IB_diploma.pdf", ""],
            "Historia": ["132404.pdf", "24_Historia_de_Mexico_II.pdf"],
            "Fisica": ["fisica-general-libro-completo.pdf", "EL002693.pdf", "FisicaUniversitariaVolumen2-WEB.pdf", "Fundamentos de física - Volumen 1 - Serway & Vuille - 9ed.pdf", "Física básica.pdf", "CB2.pdf"],
            "GUIAS": ["GUIA CBQS 2023 OK1.pdf"],
        }
        return libros_por_categoria.get(categoria, [])

    def abrir_ventana(self, ventana):
        """Función simulada para abrir una nueva ventana."""
        messagebox.showinfo("Abrir Ventana", f"Abrir la ventana: {ventana}")


# Iniciar la aplicación
root = tk.Tk()
app = CatalogoConstruccion(root)
root.mainloop()

