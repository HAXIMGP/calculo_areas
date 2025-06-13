
import tkinter as tk
from tkinter import messagebox

def calcular_area():
    try:
        lado = float(entry_lado.get())
        area = lado * lado
        messagebox.showinfo("Resultado", f"El área del cuadrado es: {area}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un valor numérico válido.")

root = tk.Tk()
root.title("Calculadora de Área - Cuadrado")
root.geometry("300x200")
root.configure(bg="#f0f8ff")  # fondo suave

# Etiquetas y entradas
tk.Label(root, text="Lado:", font=("Helvetica", 12), bg="#f0f8ff").pack(pady=5)
entry_lado = tk.Entry(root, font=("Helvetica", 12))
entry_lado.pack(pady=5)

# Botón de cálculo
btn_calcular = tk.Button(
    root,
    text="Calcular Área",
    command=calcular_area,
    font=("Helvetica", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    relief="raised",
    bd=4,
    padx=10, pady=5
)
btn_calcular.pack(pady=15)

root.mainloop()
