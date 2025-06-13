import tkinter as tk
from tkinter import messagebox

def calcular_area_cuadrado():
    try:
        lado = float(entry_lado.get())
        area_cuadrado = lado * lado
        messagebox.showinfo("Resultado", f"El área del cuadrado es: {area_cuadrado}")
        return area_cuadrado
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un valor numérico válido.")
        return 0

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

def calcular_area_rectangulo():
    try:
        ancho = float(entry_ancho.get())
        alto = float(entry_alto.get())
        area_rectangulo = ancho * alto
        messagebox.showinfo("Resultado", f"El área del rectángulo es: {area_rectangulo}")
        return area_rectangulo
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un valor numérico válido.")
        return 0

def mostrar_cuadrado():
    limpiar_ventana()
    
    tk.Label(root, text="Lado (Cuadrado):", font=("Helvetica", 12), bg="#40E0D0").pack(pady=5)
    global entry_lado
    entry_lado = tk.Entry(root, font=("Helvetica", 12))
    entry_lado.pack(pady=5)
    
    btn_calcular_cuadrado = tk.Button(
        root,
        text="Calcular Área del Cuadrado",
        command=calcular_area_cuadrado,
        font=("Helvetica", 12, "bold"),
        bg="#FF6347",
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
        bg="#FF6347",
        fg="white",
        relief="raised",
        bd=4,
        padx=10, pady=5
    )
    btn_volver_seleccion.pack(pady=10)

def mostrar_triangulo():
    limpiar_ventana()
    
    tk.Label(root, text="Base (Triángulo):", font=("Helvetica", 12), bg="#40E0D0").pack(pady=5)
    global entry_base
    entry_base = tk.Entry(root, font=("Helvetica", 12))
    entry_base.pack(pady=5)

    tk.Label(root, text="Altura (Triángulo):", font=("Helvetica", 12), bg="#40E0D0").pack(pady=5)
    global entry_altura
    entry_altura = tk.Entry(root, font=("Helvetica", 12))
    entry_altura.pack(pady=5)

    btn_calcular_triangulo = tk.Button(
        root,
        text="Calcular Área del Triángulo",
        command=calcular_area_triangulo,
        font=("Helvetica", 12, "bold"),
        bg="#FF6347",
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
        bg="#FF6347",
        fg="white",
        relief="raised",
        bd=4,
        padx=10, pady=5
    )
    btn_volver_seleccion.pack(pady=10)

def mostrar_rectangulo():
    limpiar_ventana()

    tk.Label(root, text="Ancho (Rectángulo):", font=("Helvetica", 12), bg="#40E0D0").pack(pady=5)
    global entry_ancho
    entry_ancho = tk.Entry(root, font=("Helvetica", 12))
    entry_ancho.pack(pady=5)

    tk.Label(root, text="Alto (Rectángulo):", font=("Helvetica", 12), bg="#40E0D0").pack(pady=5)
    global entry_alto
    entry_alto = tk.Entry(root, font=("Helvetica", 12))
    entry_alto.pack(pady=5)

    btn_calcular_rectangulo = tk.Button(
        root,
        text="Calcular Área del Rectángulo",
        command=calcular_area_rectangulo,
        font=("Helvetica", 12, "bold"),
        bg="#FF6347",
        fg="white",
        relief="raised",
        bd=4,
        padx=10, pady=5
    )
    btn_calcular_rectangulo.pack(pady=10)

    btn_volver_seleccion = tk.Button(
        root,
        text="Volver a seleccionar",
        command=mostrar_opciones,
        font=("Helvetica", 12, "bold"),
        bg="#FF6347",
        fg="white",
        relief="raised",
        bd=4,
        padx=10, pady=5
    )
    btn_volver_seleccion.pack(pady=10)

def limpiar_ventana():
    for widget in root.winfo_children():
        widget.destroy()

def mostrar_opciones():
    limpiar_ventana()

    btn_cuadrado = tk.Button(
        root,
        text="Área del Cuadrado",
        command=mostrar_cuadrado,
        font=("Helvetica", 12, "bold"),
        bg="#FF6347",
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
        bg="#FF6347",
        fg="white",
        relief="raised",
        bd=4,
        padx=10, pady=5
    )
    btn_triangulo.pack(pady=10)

    btn_rectangulo = tk.Button(
        root,
        text="Área del Rectángulo",
        command=mostrar_rectangulo,
        font=("Helvetica", 12, "bold"),
        bg="#FF6347",
        fg="white",
        relief="raised",
        bd=4,
        padx=10, pady=5
    )
    btn_rectangulo.pack(pady=10)

root = tk.Tk()
root.title("Calculadora de Áreas")
root.geometry("400x400")
root.configure(bg="#40E0D0")

mostrar_opciones()

root.mainloop()
