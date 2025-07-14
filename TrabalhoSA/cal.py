import tkinter as tk
from calculator import add, subtract, multiply, divide

def calcular():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        op = operacao.get()

        if op == "+":
            resultado = add(a, b)
        elif op == "-":
            resultado = subtract(a, b)
        elif op == "*":
            resultado = multiply(a, b)
        elif op == "/":
            resultado = divide(a, b)
        else:
            resultado = "Operação inválida"

        resultado_label.config(text=f"Resultado: {resultado}")
    except Exception as e:
        resultado_label.config(text=f"Erro: {e}")

app = tk.Tk()
app.title("Calculadora")

entry1 = tk.Entry(app)
entry1.pack()

entry2 = tk.Entry(app)
entry2.pack()

operacao = tk.StringVar(app)
operacao.set("+")

op_menu = tk.OptionMenu(app, operacao, "+", "-", "*", "/")
op_menu.pack()

btn = tk.Button(app, text="Calcular", command=calcular)
btn.pack()

resultado_label = tk.Label(app, text="Resultado:")
resultado_label.pack()

app.mainloop()
