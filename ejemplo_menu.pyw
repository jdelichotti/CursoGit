from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()


def infoAdicional():
    messagebox.showinfo("Procesador", "Procesador 2020")


def avisoLiencia():
    messagebox.showwarning("Procesador", "Procesador 2020")


def salirAplicacion():
    valor = messagebox.askquestion("Salir", "¿Desea Salir")
    if valor == "yes":
        root.destroy()


def cerrarDocumento():
    valor = messagebox.askretrycancel(
        "Reintentar", "No es posible cerrar. Documento Bloqueado")
    if valor == False:
        root.destroy()


def abreArchivo():
    archivo = filedialog.askopenfilename(title="Abrir",filetypes=(("Excel XLSX","*.xlsx"),("Excel XLS","*.xls"),("Todos","*.*"))) ##, initialdir="C:"
    print(archivo)  # devuelve la ruta del arhivo seleccionado


barraMenu = Menu(root)
root.config(menu=barraMenu, width=350, height=300)

##-----------------ARCHIVO---------------------##
archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Abrir", command=abreArchivo)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

##-----------------EDICION---------------------##
archivoEdicion = Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

##-----------------HERRAMIENTAS---------------------##
archivoHerramientas = Menu(barraMenu, tearoff=0)


##-----------------Ayuda---------------------##
archivoAyuda = Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLiencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)


root.mainloop()
