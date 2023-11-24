#!/usr/bin/env python
# coding: utf-8

# In[9]:


import tkinter as tk
import random
import string



def generate_password():
    password_strength = choice.get()
    if password_strength == "Poor":
        characters = string.ascii_letters
    elif password_strength == "Average":
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(int(password_length.get())))


def copy_to_clipboard():
    generated_password = generate_password()
    pyperclip.copy(generated_password)


def update_label():
    generated_password = generate_password()
    password_label.config(text=generated_password)


root = tk.Tk()
root.title("Ayandeep Password Generator")
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg="#3498db")

title_label = tk.Label(
    root,
    text="Ayandeep Password Generator",
    font=("Helvetica", 18, "bold"),
    bg="#3498db",
    fg="white",
)
title_label.pack(pady=10)

strength_label = tk.Label(
    root,
    text="Select Password Strength:",
    font=("Helvetica", 12),
    bg="#3498db",
    fg="white",
)
strength_label.pack()

choice = tk.StringVar()
options = [("Poor"), ("Average"), ("Strong")]
for text in options:
    option = tk.Radiobutton(
        root,
        text=text,
        variable=choice,
        value=text,
        font=("Helvetica", 10),
        bg="#3498db",
        fg="white",
    )
    option.pack(anchor="w", padx=20, pady=5)

len_label = tk.Label(
    root, text="Password Length:", font=("Helvetica", 12), bg="#3498db", fg="white"
)
len_label.pack()

password_length = tk.StringVar()
length_entry = tk.Entry(
    root, textvariable=password_length, font=("Helvetica", 10), width=13
)
length_entry.pack(padx=20, pady=5)

generate_button = tk.Button(
    root,
    text="Generate Password",
    font=("Helvetica", 12),
    bd=3,
    command=update_label,
    bg="#e74c3c",
    fg="white",
)
generate_button.pack(pady=10)

password_label = tk.Label(
    root, text="", font=("Helvetica", 14), bg="#3498db", fg="white"
)
password_label.pack(padx=20, pady=10)

copy_button = tk.Button(
    root,
    text="Copy to Clipboard",
    font=("Helvetica", 12),
    bd=3,
    command=copy_to_clipboard,
    bg="#27ae60",
    fg="white",
)
copy_button.pack()

root.mainloop()


# In[ ]:




