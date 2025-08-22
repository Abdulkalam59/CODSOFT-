import tkinter as tk 
from tkinter import font 

def button_click(number): 
    current = display.get() 
    display.delete(0, tk.END) 
    display.insert(0, current + str(number)) 

def button_clear(): 
    display.delete(0, tk.END)

def button_equal(): 
    try: 
        result = eval(display.get()) 
        display.delete(0, tk.END) 
        display.insert(0, str(result)) 
    except: 
        display.delete(0, tk.END) 
        display.insert(0, "Error") 

root = tk.Tk() 
root.title("Simple Calculator") 
root.geometry("400x500") 
root.configure(bg="lightblue") 

font_large = font.Font(family="Arial", size=24, weight="bold") 
font_small = font.Font(family="Arial", size=14) 

display = tk.Entry(root, font=font_large, bd=10, insertwidth=2, width=14, justify='right', bg="white") 
display.grid(row=0, column=0, columnspan=4, pady=20) 

buttons = [ 
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3), 
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3), 
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3), 
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3) 
] 

for (text, row, col) in buttons:
    action = lambda x=text: button_click(x) if x not in ['=', 'C'] else ( 
        button_equal() if x == '=' else button_clear()
    )
    button = tk.Button(root, text=text, padx=20, pady=20, font=font_small, bg="white", command=action)
    button.grid(row=row, column=col, sticky="nsew")

for i in range(5):
    root.rowconfigure(i, weight=1)
    root.columnconfigure(i, weight=1)

root.mainloop() 
