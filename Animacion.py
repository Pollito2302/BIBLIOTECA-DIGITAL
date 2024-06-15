import tkinter as tk
from PIL import Image, ImageTk

class AnimacionApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x500")
        self.master.configure(bg='white')  # Cambiar el fondo de la ventana a blanco
        
        # Cargar la imagen
        self.image = Image.open("buho2.png")
        self.photo = ImageTk.PhotoImage(self.image)
        
        self.label_image = tk.Label(self.master, image=self.photo, bg='white')
        self.label_image.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Crear la etiqueta con la fuente "Rowdies"
        self.label_text = tk.Label(self.master, text="Biblioteca del buho", font=("Rowdies", 24), bg='white')
        self.label_text.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        
        # Iniciar la animación
        self.animar_aparicion()
    
    def animar_aparicion(self):
        for alpha in range(0, 256, 8):
            self.master.attributes("-alpha", alpha/255)  
            self.master.update_idletasks()  
            self.master.after(20)  
        
        self.master.attributes("-alpha", 1)

def main():
    root = tk.Tk()
    app = AnimacionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


