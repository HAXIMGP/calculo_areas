import tkinter as tk
from tkinter import messagebox

# Función para calcular el área del cuadrado
def calcular_area_cuadrado():
    try:
        lado = float(entry_lado.get())
        area_cuadrado = lado * lado
        messagebox.showinfo("Resultado", f"El área del cuadrado es: {area_cuadrado}")
        return area_cuadrado
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un valor numérico válido.")
        return 0

# Función para calcular el área del triángulo
def calcular_area_triangulo():
    try:
        base = float(entry_base.get())
        altura = float(entry_altura.get())
        area_triangulo = (base * altura) / 2
        messagebox.showinfo("Resultado", f"El área del triángulo es: {area_triangulo}")
        return area_triangulo
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un valor numérico válido.")
        return 0

# Función para mostrar el formulario para el cuadrado
def mostrar_cuadrado():
    # Limpiar la ventana
    limpiar_ventana()
    
    # Mostrar el formulario para el área del cuadrado
    tk.Label(root, text="Lado (Cuadrado):", font=("Helvetica", 12), bg="#f0f8ff").pack(pady=5)
    global entry_lado
    entry_lado = tk.Entry(root, font=("Helvetica", 12))
    entry_lado.pack(pady=5)
    
    btn_calcular_cuadrado = tk.Button(
        root,
        text="Calcular Área del Cuadrado",
        command=calcular_area_cuadrado,
        font=("Helvetica", 12, "bold"),
        bg="#4CAF50",
        fg="white",
        relief="raised",
        bd=4,
        padx=10, pady=5
    )
    btn_calcular_cuadrado.pack(pady=10)

    btn_volver_seleccion = tk.Button(
        root,
        text="Volver a seleccionar",
        command=mostrar_opciones,
        font=("Helvetica", 12, "bold"),
        bg="#f0a500",
        fg="white",
        relief="raised",
        bd=4,
        padx=10, pady=5
    )
    btn_volver_seleccion.pack(pady=10)

# Función para mostrar el formulario para el triángulo
def mostrar_triangulo():
    # Limpiar la ventana
    limpiar_ventana()
    
    # Mostrar el formulario para el área del triángulo
    tk.Label(root, text="Base (Triángulo):", font=("Helvetica", 12), bg="#f0f8ff").pack(pady=5)
    global entry_base
    entry_base = tk.Entry(root, font=("Helvetica", 12))
    entry_base.pack(pady=5)

    tk.Label(root, text="Altura (Triángulo):", font=("Helvetica", 12), bg="#f0f8ff").pack(pady=5)
    global entry_altura
    entry_altura = tk.Entry(root, font=("Helvetica", 12))
    entry_altura.pack(pady=5)

    btn_calcular_triangulo = tk.Button(
        root,
        text="Calcular Área del Triángulo",
        command=calcular_area_triangulo,
        font=("Helvetica", 12, "bold"),
        bg="#4CAF50",
        fg="white",
        relief="raised",
        bd=4,
        padx=10, pady=5
    )
    btn_calcular_triangulo.pack(pady=10)

    btn_volver_seleccion = tk.Button(
        root,
        text="Volver a seleccionar",
        command=mostrar_opciones,
        font=("Helvetica", 12, "bold"),
        bg="#f0a500",
        fg="white",
        relief="raised",
        bd=4,
        padx=10, pady=5
    )
    btn_volver_seleccion.pack(pady=10)

# Función para limpiar la ventana antes de mostrar el siguiente formulario
def limpiar_ventana():
    for widget in root.winfo_children():
        widget.destroy()

# Función para mostrar las opciones de selección (cuadrado o triángulo)
def mostrar_opciones():
    limpiar_ventana()

    # Botones para elegir el tipo de área
    btn_cuadrado = tk.Button(
        root,
        text="Área del Cuadrado",
        command=mostrar_cuadrado,
        font=("Helvetica", 12, "bold"),
        bg="#4CAF50",
        fg="white",
        relief="raised",
        bd=4,
        padx=10, pady=5
    )
    btn_cuadrado.pack(pady=10)

    btn_triangulo = tk.Button(
        root,
        text="Área del Triángulo",
        command=mostrar_triangulo,
        font=("Helvetica", 12, "bold"),
        bg="#4CAF50",
        fg="white",
        relief="raised",
        bd=4,
        padx=10, pady=5
    )
    btn_triangulo.pack(pady=10)

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Áreas")
root.geometry("400x400")
root.configure(bg="#f0f8ff")   # Fondo suave

# Mostrar las opciones iniciales
mostrar_opciones()

root.mainloop()
