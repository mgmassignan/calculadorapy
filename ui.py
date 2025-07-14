import tkinter as tk

class CalculatorUI:
    def __init__(self, master, calculator):
        self.master = master
        self.calculator = calculator
        master.title("Calculadora Apple")
        master.geometry("320x520")
        master.resizable(False, False)
        master.configure(bg="black")

        # Display
        self.display_frame = tk.Frame(master, bg="black")
        self.display_frame.pack(expand=True, fill="both", padx=10, pady=10)

        self.display_var = tk.StringVar()
        self.display_var.set("0")

        self.display_label = tk.Label(
            self.display_frame,
            textvariable=self.display_var,
            font=("Helvetica Neue", 48, "bold"),
            fg="white",
            bg="black",
            anchor="e",
            padx=10
        )
        self.display_label.pack(expand=True, fill="both")

        # Buttons
        self.buttons_frame = tk.Frame(master, bg="black")
        self.buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Configure grid weights for responsive buttons
        for i in range(5):
            self.buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.buttons_frame.grid_columnconfigure(i, weight=1)

        buttons = [
            ("AC", 1, 0, "#a6a6a6", "black", self.clear_display),
            ("±", 1, 1, "#a6a6a6", "black", self.toggle_sign),
            ("%", 1, 2, "#a6a6a6", "black", self.percentage),
            ("÷", 1, 3, "#ff9500", "white", lambda: self.handle_operation("/")),

            ("7", 2, 0, "#333333", "white", lambda: self.add_to_display("7")),
            ("8", 2, 1, "#333333", "white", lambda: self.add_to_display("8")),
            ("9", 2, 2, "#333333", "white", lambda: self.add_to_display("9")),
            ("×", 2, 3, "#ff9500", "white", lambda: self.handle_operation("*")),

            ("4", 3, 0, "#333333", "white", lambda: self.add_to_display("4")),
            ("5", 3, 1, "#333333", "white", lambda: self.add_to_display("5")),
            ("6", 3, 2, "#333333", "white", lambda: self.add_to_display("6")),
            ("−", 3, 3, "#ff9500", "white", lambda: self.handle_operation("-")),

            ("1", 4, 0, "#333333", "white", lambda: self.add_to_display("1")),
            ("2", 4, 1, "#333333", "white", lambda: self.add_to_display("2")),
            ("3", 4, 2, "#333333", "white", lambda: self.add_to_display("3")),
            ("+", 4, 3, "#ff9500", "white", lambda: self.handle_operation("+")),

            ("0", 5, 0, "#333333", "white", lambda: self.add_to_display("0")),
            (".", 5, 2, "#333333", "white", self.add_decimal),
            ("=", 5, 3, "#ff9500", "white", self.calculate_expression)
        ]

        for (text, row, col, bg, fg, command) in buttons:
            if text == "0":
                button = tk.Button(
                    self.buttons_frame,
                    text=text,
                    font=("Helvetica Neue", 24),
                    bg=bg,
                    fg=fg,
                    command=command,
                    width=6,
                    height=2,
                    relief="flat",
                    borderwidth=0,
                    highlightbackground="black",
                    highlightthickness=0,
                    activebackground=bg,
                    activeforeground=fg
                )
                button.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=5, pady=5)
            else:
                button = tk.Button(
                    self.buttons_frame,
                    text=text,
                    font=("Helvetica Neue", 24),
                    bg=bg,
                    fg=fg,
                    command=command,
                    width=3,
                    height=2,
                    relief="flat",
                    borderwidth=0,
                    highlightbackground="black",
                    highlightthickness=0,
                    activebackground=bg,
                    activeforeground=fg
                )
                button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

    def add_to_display(self, value):
        current_display = self.display_var.get()
        if current_display == "0" or self.calculator.new_input_required:
            self.display_var.set(value)
            self.calculator.new_input_required = False
        else:
            self.display_var.set(current_display + value)

    def add_decimal(self):
        current_display = self.display_var.get()
        if self.calculator.new_input_required:
            self.display_var.set("0.")
            self.calculator.new_input_required = False
        elif "." not in current_display:
            self.display_var.set(current_display + ".")

    def clear_display(self):
        self.display_var.set("0")
        self.calculator.clear()

    def toggle_sign(self):
        current_value = self.display_var.get()
        if current_value != "0":
            if current_value.startswith("-"):
                self.display_var.set(current_value[1:])
            else:
                self.display_var.set("-" + current_value)

    def percentage(self):
        try:
            value = float(self.display_var.get())
            self.display_var.set(str(value / 100))
            self.calculator.new_input_required = True
        except ValueError:
            self.display_var.set("Error")
            self.calculator.clear()

    def handle_operation(self, op):
        try:
            current_value = float(self.display_var.get())
            self.calculator.set_current_value(current_value)
            self.calculator.set_operation(op)
            self.calculator.new_input_required = True
        except ValueError:
            self.display_var.set("Error")
            self.calculator.clear()

    def calculate_expression(self):
        try:
            current_value = float(self.display_var.get())
            result = self.calculator.calculate(current_value)
            self.display_var.set(str(result))
            self.calculator.new_input_required = True
        except Exception as e:
            self.display_var.set("Error")
            self.calculator.clear()


