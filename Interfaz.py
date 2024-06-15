from customtkinter import CTk, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkCheckBox, CTkImage
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='biblioteca'
)

def registrarse():
    # Obtener los datos del usuario
    nombre_usuario = correo.get()
    contraseña = contrasenna.get()
    # CONSULTAS
    try:
        if conexion.is_connected():
            cursor = conexion.cursor()
            consulta = "INSERT INTO usuarios (nombre_usuario, contraseña) VALUES (%s, %s)"
            valores = (nombre_usuario, contraseña)
            cursor.execute(consulta, valores)
            conexion.commit()
            messagebox.showinfo("Registrarse", "Registro exitoso")
            cursor.close()
        else:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error al registrar usuario: {e}")

def inicio_sesion():
    # Obtener los datos del usuario
    nombre_usuario = correo.get()
    contraseña = contrasenna.get()
    # CONSULTA INICIO_SESION
    try:
        if conexion.is_connected():
            cursor = conexion.cursor()
            consulta = "SELECT * FROM usuarios WHERE nombre_usuario = %s AND contraseña = %s"
            valores = (nombre_usuario, contraseña)
            cursor.execute(consulta, valores)
            usuario = cursor.fetchone()
            if usuario:
                messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso")
            else:
                messagebox.showerror("Inicio de Sesión", "Nombre de usuario o contraseña incorrectos")
            cursor.close()
        else:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error al iniciar sesión: {e}")

def toggle_password():
    if checkbox.get() == 1:
        contrasenna.configure(show="")
    else:
        contrasenna.configure(show="*")

# VENTANA PRINCIPAL
root = CTk()
root.geometry("500x600+350+20")
root.minsize(480, 500)
root.config(bg='#010101')
root.title("Iniciar Sesión")

frame = CTkFrame(root, fg_color='#010101')
frame.grid(column=0, row=0, sticky='nsew', padx=50, pady=50)

frame.columnconfigure([0, 1], weight=1)
frame.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Cargar imágenes 
logo_image = Image.open('C:/Daniela-Osamu/Python Dany/proyecto/images/logo6.gif')
new_width, new_height = 325, 100
logo_image = logo_image.resize((new_width, new_height))
logo = ImageTk.PhotoImage(logo_image)

# Logo
CTkLabel(frame, image=logo, text='').grid(columnspan=2, row=0)

# Campo de correo electrónico
correo = CTkEntry(frame, placeholder_text='Correo electrónico', border_color='#8000B4',
                  fg_color='#010101', width=220, height=40, text_color='white', placeholder_text_color='gray')
correo.grid(columnspan=2, row=1, padx=4, pady=4)

# Campo de contraseña
contrasenna = CTkEntry(frame, show="*", placeholder_text='Contraseña', border_color='#8000B4',
                       fg_color='#010101', width=220, height=40, text_color='white', placeholder_text_color='gray')
contrasenna.grid(columnspan=2, row=2, padx=4, pady=4)

# Checkbox para mostrar la contraseña
checkbox = CTkCheckBox(frame, text="Mostrar contraseña", hover_color='#7f5af0', border_color='#8000B4',
                       fg_color='#2cb67d', text_color='white')
checkbox.grid(columnspan=2, row=3, padx=4, pady=4)
checkbox.configure(command=toggle_password)

# Botón de iniciar sesión
bt_iniciar = CTkButton(frame, text='INICIAR SESIÓN', border_color='#8000B4', fg_color='#010101',
                       hover_color='#2cb67d', corner_radius=12, border_width=2, command=inicio_sesion)
bt_iniciar.grid(columnspan=2, row=4, padx=4, pady=4)

# Botón de registro
bt_registro = CTkButton(frame, text='REGISTRARSE', border_color='#8000B4', fg_color='#010101',
                        hover_color='#2cb67d', corner_radius=12, border_width=2, command=registrarse)
bt_registro.grid(columnspan=2, row=5, padx=4, pady=4)

# Establecer el icono de la ventana
root.call('wm', 'iconphoto', root._w, logo)

# Iniciar el bucle principal de la ventana
root.mainloop()
