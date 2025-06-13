import tkinter as tk
from tkinter import messagebox

# Función para calcular el área del cuadrado
def calcular_area_cuadrado():
    try:
        lado = float(entry_lado.get())
        area_cuadrado = lado * lado
        messagebox.showinfo("Resultado", f"El área del cuadrado es: {area_cuadrado}")
        return area_cuadrado  # Retornamos el área del cuadrado
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un valor numérico válido.")
        return 0

# Función para calcular el área del triángulo
def calcular_area_triangulo():
    try:
        base = float(entry_base.get())
        altura = float(entry_altura.get())
        area_triangulo = (base * altura) / 2
        area_total = calcular_area_cuadrado() + area_triangulo
        messagebox.showinfo("Resultado", f"El área del triángulo es: {area_triangulo}\nÁrea total acumulada: {area_total}")
        return area_total
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un valor numérico válido.")
        return 0

# Función para calcular el área del rectángulo
def calcular_area_rectangulo():
    try:
        ancho = float(entry_ancho.get())
        alto = float(entry_alto.get())
        area_rectangulo = ancho * alto
        area_total = calcular_area_triangulo() + area_rectangulo
        messagebox.showinfo("Resultado", f"El área del rectángulo es: {area_rectangulo}\nÁrea total acumulada: {area_total}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un valor numérico válido.")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Áreas - Cuadrado + Triángulo + Rectángulo")
root.geometry("400x400")
root.configure(bg="#f0f8ff")  # Fondo suave

# Cuadrado
tk.Label(root, text="Lado (Cuadrado):", font=("Helvetica", 12), bg="#f0f8ff").pack(pady=5)
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

# Triángulo
tk.Label(root, text="Base (Triángulo):", font=("Helvetica", 12), bg="#f0f8ff").pack(pady=5)
entry_base = tk.Entry(root, font=("Helvetica", 12))
entry_base.pack(pady=5)

tk.Label(root, text="Altura (Triángulo):", font=("Helvetica", 12), bg="#f0f8ff").pack(pady=5)
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

# Rectángulo
tk.Label(root, text="Ancho (Rectángulo):", font=("Helvetica", 12), bg="#f0f8ff").pack(pady=5)
entry_ancho = tk.Entry(root, font=("Helvetica", 12))
entry_ancho.pack(pady=5)

tk.Label(root, text="Alto (Rectángulo):", font=("Helvetica", 12), bg="#f0f8ff").pack(pady=5)
entry_alto = tk.Entry(root, font=("Helvetica", 12))
entry_alto.pack(pady=5)

btn_calcular_rectangulo = tk.Button(
    root,
    text="Calcular Área del Rectángulo",
    command=calcular_area_rectangulo,
    font=("Helvetica", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    relief="raised",
    bd=4,
    padx=10, pady=5
)
btn_calcular_rectangulo.pack(pady=10)

root.mainloop()
