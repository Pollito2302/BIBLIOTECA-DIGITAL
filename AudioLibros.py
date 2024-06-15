import tkinter as tk
from tkinter import ttk
import pygame
import os
import time

class AudioLibroApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Audio Libro App")
        self.master.geometry("400x500")
        self.master.configure(background='black')  # Fondo negro

        # Etiqueta para mostrar la imagen
        self.image_label = tk.Label(self.master, background='black')
        self.image_label.pack(pady=20)

        # Etiqueta para el título del libro (blanco y en mayúsculas)
        self.title_label = tk.Label(self.master, font=("Helvetica", 16, "bold"), background='black', foreground='white', text="TÍTULO DEL LIBRO")
        self.title_label.pack(pady=10)

        # Etiqueta para mostrar el tiempo de reproducción
        self.time_label = tk.Label(self.master, font=("Helvetica", 12), background='black')
        self.time_label.pack(pady=10)

        # Barra de reproducción (seek bar)
        self.seek_bar = ttk.Scale(self.master, from_=0, to=100, orient=tk.HORIZONTAL, length=300, command=self.set_audio_position)
        self.seek_bar.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=20)

        # Frame para los botones de reproducción
        self.controls_frame = tk.Frame(self.master, background='black')
        self.controls_frame.pack(side=tk.BOTTOM, pady=10)

        # Botón de reproducción
        self.play_button = ttk.Button(self.controls_frame, text="▶ Play", style='Small.TButton', command=self.play_audio)
        self.play_button.pack(side=tk.LEFT, padx=5)

        # Botón de pausa
        self.pause_button = ttk.Button(self.controls_frame, text="⏸ Pause", style='Small.TButton', command=self.pause_audio)
        self.pause_button.pack(side=tk.LEFT, padx=5)

        # Crear el menú principal
        self.create_menu()

        # Configuración de pygame
        pygame.init()
        pygame.mixer.init()

        # Rutas de los archivos
        self.image_path = os.path.join(os.path.dirname(__file__), "conde.png")
        self.audio_path = r"C:\Users\hp\Documents\uli\proyecto\El Conde de Montecristo Parte 1 -Alejandro Dumas- Audiolibro.mp3"

        self.title = "El Conde de Montecristo"

        # Intentar cargar la imagen y mostrar el libro al iniciar la aplicación
        self.load_book()

        # Variable para almacenar el tiempo de inicio de reproducción
        self.start_time = None

        # Actualizar el tiempo de reproducción y la barra de reproducción cada segundo
        self.update_time()

    def create_menu(self):
        # Crear una barra de menú
        self.menu_bar = tk.Menu(self.master)

        # Menú desplegable 'Menu'
        self.menu_options = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_options.add_command(label="Página Principal", command=self.show_home)
        self.menu_options.add_command(label="Categorías", command=self.show_categories)
        self.menu_options.add_command(label="Audio Libros", command=self.show_audiobooks)
        self.menu_options.add_command(label="Descargas", command=self.show_downloads)

        # Agregar el menú 'Menu' a la barra de menú
        self.menu_bar.add_cascade(label="Menu", menu=self.menu_options)

        # Configurar la barra de menú en la ventana principal
        self.master.config(menu=self.menu_bar)

    def show_home(self):
        # Implementación de la página principal
        print("Mostrando Página Principal")

    def show_categories(self):
        # Implementación de la página de categorías
        print("Mostrando Categorías")

    def show_audiobooks(self):
        # Implementación de la página de audio libros
        print("Mostrando Audio Libros")

    def show_downloads(self):
        # Implementación de la página de descargas
        print("Mostrando Descargas")

    def load_book(self):
        # Intentar cargar la imagen
        try:
            self.image = tk.PhotoImage(file=self.image_path)

            # Escalar la imagen
            new_width = 150  # Nuevo ancho deseado
            width, height = self.image.width(), self.image.height()
            new_height = int(height * (new_width / width))  # Mantener la proporción
            self.image = self.image.subsample(width // new_width, height // new_height)

            self.image_label.config(image=self.image)

            # Centrar la imagen
            self.image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        except tk.TclError as e:
            print(f"Error al cargar la imagen: {e}")

        # Actualizar el título del libro
        self.title_label.config(text=self.title.upper())

    def play_audio(self):
        try:
            pygame.mixer.music.load(self.audio_path)
            pygame.mixer.music.play()
            self.start_time = time.time()  # Iniciar el contador de tiempo
        except pygame.error as e:
            print(f"Error al cargar el audio: {e}")

    def pause_audio(self):
        pygame.mixer.music.pause()

    def update_time(self):
        if pygame.mixer.music.get_busy() and self.start_time is not None:
            elapsed_time = time.time() - self.start_time
            minutes = int(elapsed_time // 60)
            seconds = int(elapsed_time % 60)
            time_str = f"Tiempo transcurrido: {minutes:02d}:{seconds:02d}"
            self.time_label.config(text=time_str)

            # Actualizar la posición de la barra de reproducción
            if pygame.mixer.music.get_pos() > 0:
                current_pos = pygame.mixer.music.get_pos() / 1000  # Convertir a segundos
                song_length = pygame.mixer.music.get_length() / 1000  # Convertir a segundos
                self.seek_bar.set((current_pos / song_length) * 100)

        else:
            self.time_label.config(text="")
            self.seek_bar.set(0)

        self.master.after(1000, self.update_time)  # Actualizar cada segundo

    def set_audio_position(self, value):
        if pygame.mixer.music.get_busy():
            song_length = pygame.mixer.music.get_length() / 1000  # Convertir a segundos
            seek_pos = float(value) * song_length / 100
            pygame.mixer.music.set_pos(seek_pos)

def main():
    root = tk.Tk()
    app = AudioLibroApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
