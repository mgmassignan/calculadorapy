import tkinter as tk
from calculator import Calculator
from ui import CalculatorUI

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator()
    app = CalculatorUI(root, calculator)
    root.mainloop()
