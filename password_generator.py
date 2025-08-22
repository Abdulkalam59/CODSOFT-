import tkinter as tk 
import random 
import string 

def generate_password(): 
    try: 
        length = int(length_entry.get()) 
        if length < 8: 
            password_result.config(text="Password must be at least 8 characters", fg="red") 
        else: 
            characters = string.ascii_letters + string.digits + string.punctuation 
            password = ''.join(random.choice(characters) for _ in range(length)) 
            password_result.config(text=password, fg="green") 
    except ValueError: 
        password_result.config(text="Please enter a valid number", fg="red") 

def reset_password(): 
    name_entry.delete(0, tk.END) 
    email_entry.delete(0, tk.END) 
    username_entry.delete(0, tk.END) 
    length_entry.delete(0, tk.END) 
    password_result.config(text="")

root = tk.Tk() 
root.title("Password Generator")
root.geometry("500x400")

tk.Label(root, text="Name:", font=("Arial", 14)).pack(anchor='w')
name_entry = tk.Entry(root, font=("Arial", 14))
name_entry.pack(fill='x', padx=10)

tk.Label(root, text="Email:", font=("Arial", 14)).pack(anchor='w')
email_entry = tk.Entry(root, font=("Arial", 14))
email_entry.pack(fill='x', padx=10)

tk.Label(root, text="Username:", font=("Arial", 14)).pack(anchor='w')
username_entry = tk.Entry(root, font=("Arial", 14))
username_entry.pack(fill='x', padx=10)

tk.Label(root, text="Password Length:", font=("Arial", 14)).pack(anchor='w')
length_entry = tk.Entry(root, font=("Arial", 14))
length_entry.pack(fill='x', padx=10)

tk.Button(root, text="Generate Password", command=generate_password, bg="#7676ff", fg="white").pack(pady=10)
tk.Button(root, text="Reset", command=reset_password, bg="#ff6262", fg="white").pack(pady=5)

password_result = tk.Label(root, text="", font=("Arial", 14))
password_result.pack(pady=10)

root.mainloop()
