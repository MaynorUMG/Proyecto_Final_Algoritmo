import webbrowser
# Implementamos la libreria webbrowser para poder pegar links en nuestro proyecto
import tkinter as tk
from tkinter import filedialog, END, messagebox
# Implementamos extensiones/librerias de tkinder para utilizar Filechooseer, e implementar Mensajes/Alertas

jm_archivo_abierto = None
# Significado jm = Junior y Maynor
def jm_abrir_manual():
    webbrowser.open("https://github.com/MaynorUMG/Proyecto_Final_Algoritmo/blob/main/README.md")

def jm_abrir_ayuda():
    jm_ventana = tk.Toplevel(jm_principal)
    jm_ventana.title("Ventana de Ayuda")
    jm_ventana.config(bg="#51D1F6")
    jm_ventana.geometry("250x200")

    jm_boton_informacion = tk.Button(jm_ventana, text="Informacion",font=("Comic Sans MS", 10), command=jm_informacion)
    jm_boton_informacion.pack(pady=5)

    jm_boton_manual = tk.Button(jm_ventana, text="Abrir Manual de Usuario",font=("Comic Sans MS", 10), command=jm_abrir_manual)
    jm_boton_manual.pack(pady=5)

    jm_boton_integrantes = tk.Button(jm_ventana, text="Integrantes",font=("Comic Sans MS", 10), command=jm_integrantes)
    jm_boton_integrantes.pack(pady=5)

    jm_boton_cerrar = tk.Button(jm_ventana, text="Cerrar",font=("Comic Sans MS", 10), command=jm_ventana.destroy)
    jm_boton_cerrar.pack(pady=5)


def jm_informacion():
    jm_ventana = tk.Toplevel(jm_principal)
    jm_ventana.config(bg="#51D1F6")
    jm_ventana.title("informacion")
    jm_ventana.geometry("600x350")

    jm_titulo = tk.Label(jm_ventana, text="Informacion sobre nuestro proyecto",background="#51D1F6",foreground="#484e50", font=("Comic Sans MS", 20))
    jm_titulo.pack(pady=20)

    jm_info = tk.Label(jm_ventana, text="Nuestro proyecto trata de un menu manejador de archivos, programado en lenguaje de \n programación python utilizando la libreria de interfaz grafica (GUI) Tkinder, dentro de las \n opciones de nuestra aplicación se encuentran: \n Abrir archivo utilizando un Filechooser \n Guardar como: Para guardar archivos con diferentes extrensiones \n Guardar: Para guardar las modificaciones realizadas en el archivo \n",background="#51D1F6", foreground="#484e50", font=("Comic Sans MS", 10))
    jm_info.pack(pady=20)



def jm_integrantes():
    jm_ventana = tk.Toplevel(jm_principal)
    jm_ventana.title("Integrantes")
    jm_ventana.config(bg="#51D1F6")
    jm_ventana.geometry("600x200")

    jm_junior = tk.Label(jm_ventana, text="Junior Alvaro René Barrios Flores  Carnet: 7690-25-16187",background="#51D1F6",foreground="#484e50",font=("Arial", 15))
    jm_junior.pack(pady=40)

    jm_maynor = tk.Label(jm_ventana, text="Maynor Suriel Del Valle Alvarado  Carnet: 7690-25-21809",background="#51D1F6",foreground="#484e50", font=("Arial", 15))
    jm_maynor.pack(pady=20)


def jm_guardar_archivo():
    archivo = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if archivo is None:
        return
    contenido = texto.get("1.0", END)
    archivo.write(contenido)
    archivo.close()


def jm_archivo():
    global jm_archivo_abierto
    archivo = filedialog.askopenfilename()

    if archivo:
        jm_archivo_abierto = archivo 
        with open(archivo, "r") as file:
            contenido = file.read()
            texto.delete("1.0", END)
            texto.insert("1.0", contenido)


def jm_guardar_cambios():
    global jm_archivo_abierto

    if jm_archivo_abierto is None:
        messagebox.showerror("", "No se pudieron guardar los cambios, selecione un archivo")
        return

    contenido = texto.get("1.0", END)
    with open(jm_archivo_abierto, "w") as file:
        file.write(contenido)
        messagebox.showinfo("", "Cambios guardados")


def jm_deshacer():
    try:
        texto.edit_undo()
    except:
        pass

def jm_rehacer():
    try:
        texto.edit_redo()
    except:
        pass

jm_principal = tk.Tk()
jm_principal.config(bg="#51D1F6")
jm_principal.title("Menú Principal")
jm_principal.geometry("750x750")

jm_titulo = tk.Label(jm_principal, text="Bienvenido a nuestro proyecto", background="#51D1F6",foreground="#484e50", font=("Comic Sans MS", 30))
jm_titulo.pack(pady=20)
jm_titulo = tk.Label(jm_principal, text="Ingrese una opción",background="#51D1F6",foreground="#484e50", font=("Comic Sans MS", 20))
jm_titulo.pack(pady=20)
jm_boton_archivo = tk.Button(jm_principal, text="Abrir Archivo", font=("Comic Sans MS", 10),  command=jm_archivo)
jm_boton_archivo.pack(pady=5)
jm_boton_guardar = tk.Button(jm_principal, text="Guardar Como",font=("Comic Sans MS", 10), command=jm_guardar_archivo)
jm_boton_guardar.pack(pady=5)
jm_boton_guardar = tk.Button(jm_principal, text="Guardar",font=("Comic Sans MS", 10), command=jm_guardar_cambios)
jm_boton_guardar.pack(pady=5)
jm_boton_deshacer = tk.Button(jm_principal, text="Deshacer",font=("Comic Sans MS", 10),  command=jm_deshacer)
jm_boton_deshacer.pack(pady=5)
jm_boton_rehacer = tk.Button(jm_principal, text="Rehacer",font=("Comic Sans MS", 10),  command=jm_rehacer)
jm_boton_rehacer.pack(pady=5)
jm_boton_ayuda = tk.Button(jm_principal, text="Ayuda",font=("Comic Sans MS", 10), command=jm_abrir_ayuda)
jm_boton_ayuda.pack(pady=5)
jm_boton_cerrar = tk.Button(jm_principal, text="Cerrar", font=("Comic Sans MS", 10), command=jm_principal.destroy)
jm_boton_cerrar.pack()
texto = tk.Text(jm_principal, wrap=tk.WORD, undo=True)
texto.pack(expand=True, fill=tk.BOTH)

jm_principal.mainloop()