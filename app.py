import tkinter as tk
import math

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg="#2c3e50")

# Input field
equation = tk.StringVar()
expression_field = tk.Entry(root, textvariable=equation, font=('Arial', 24), bd=10, insertwidth=4, width=14, justify='right', bg="#ecf0f1")
expression_field.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Function to update the input field
def press(num):
    current_expression = expression_field.get()
    expression_field.delete(0, tk.END)
    expression_field.insert(0, str(current_expression) + str(num))

# Function to clear the input field
def clear():
    expression_field.delete(0, tk.END)

# Function to calculate the result
def equal_press():
    try:
        expression = expression_field.get()
        # Replace mathematical function names with their Python equivalents
        expression = expression.replace("sin(", "math.sin(math.radians(")
        expression = expression.replace("cos(", "math.cos(math.radians(")
        expression = expression.replace("tan(", "math.tan(math.radians(")
        expression = expression.replace("sqrt(", "math.sqrt(")
        
        # Evaluate the expression
        result = str(eval(expression))
        
        # Display the result
        expression_field.delete(0, tk.END)
        expression_field.insert(0, result)
    except Exception as e:
        expression_field.delete(0, tk.END)
        expression_field.insert(0, "Error")

# Function for scientific operations
def scientific_press(op):
    current_expression = expression_field.get()
    expression_field.delete(0, tk.END)
    
    if op == 'sqrt':
        expression_field.insert(0, f"sqrt({current_expression})")
    elif op == 'sin':
        expression_field.insert(0, f"sin({current_expression})")
    elif op == 'cos':
        expression_field.insert(0, f"cos({current_expression})")
    elif op == 'tan':
        expression_field.insert(0, f"tan({current_expression})")
    elif op == '^':
        expression_field.insert(0, current_expression + "")
    elif op == 'log':
        expression_field.insert(0, f"math.log10({current_expression})")

# Button styling
button_style = {
    'font': ('Arial', 18),
    'width': 5,
    'height': 2,
    'bd': 1,
    'relief': 'ridge',
    'bg': '#34495e',
    'fg': '#ecf0f1'
}

# Layout of the buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('sqrt', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('^', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('sin', 4, 4),
    ('(', 5, 0), (')', 5, 1), ('log', 5, 2), ('cos', 5, 3), ('tan', 5, 4)
]

# Create and place the buttons
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, **button_style, bg="#e74c3c", command=equal_press)
    elif text == 'C':
        btn = tk.Button(root, text=text, **button_style, bg="#f39c12", command=clear)
    elif text in ('sqrt', '^', 'sin', 'cos', 'tan', 'log'):
        btn = tk.Button(root, text=text, **button_style, bg="#16a085", command=lambda t=text: scientific_press(t))
    else:
        btn = tk.Button(root, text=text, **button_style, command=lambda t=text: press(t))
    
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Configure grid to make buttons expand
for i in range(5):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

# Start the GUI
root.mainloop()