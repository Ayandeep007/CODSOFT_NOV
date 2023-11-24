#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
from tkinter import messagebox

contacts = []


def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name and phone:
        contact = {"Name": name, "Phone": phone, "Email": email}
        contacts.append(contact)
        update_contact_list()
        clear_fields()


def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)


def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_info = f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}"
        contact_list.insert(tk.END, contact_info)


def search_contact():
    query = search_entry.get()
    results = [contact for contact in contacts if query.lower()
               in contact["Name"].lower()]
    if results:
        contact_list.delete(0, tk.END)
        for contact in results:
            contact_info = f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}"
            contact_list.insert(tk.END, contact_info)
    else:
        messagebox.showinfo("Search Result", "No matching contacts found.")


def update_selected_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        index = selected_index[0]
        contact = contacts[index]
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        if name and phone:
            contact["Name"] = name
            contact["Phone"] = phone
            contact["Email"] = email
            update_contact_list()
            clear_fields()


def delete_selected_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        index = selected_index[0]
        contacts.pop(index)
        update_contact_list()
        clear_fields()


root = tk.Tk()
root.title("Contact Book")
root.geometry("500x400")
root.configure(bg="#FFD700")

name_label = tk.Label(root, text="Name:", bg="#FFD700")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(root, bg="#FFFFE0")
name_entry.grid(row=0, column=1, padx=10, pady=5)

phone_label = tk.Label(root, text="Phone:", bg="#FFD700")
phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
phone_entry = tk.Entry(root, bg="#FFFFE0")
phone_entry.grid(row=1, column=1, padx=10, pady=5)

email_label = tk.Label(root, text="Email:", bg="#FFD700")
email_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
email_entry = tk.Entry(root, bg="#FFFFE0")
email_entry.grid(row=2, column=1, padx=10, pady=5)

add_button = tk.Button(root, text="Add Contact",
                       command=add_contact, bg="#32CD32")
add_button.grid(row=3, column=0, columnspan=2, pady=10)

update_button = tk.Button(root, text="Update Contact",
                          command=update_selected_contact, bg="#FFA500")
update_button.grid(row=4, column=0, columnspan=2, pady=10)

delete_button = tk.Button(root, text="Delete Contact",
                          command=delete_selected_contact, bg="#FF6347")
delete_button.grid(row=5, column=0, columnspan=2, pady=10)

clear_button = tk.Button(root, text="Clear Fields",
                         command=clear_fields, bg="#FF4500")
clear_button.grid(row=6, column=0, columnspan=2, pady=10)

search_label = tk.Label(root, text="Search:", bg="#FFD700")
search_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
search_entry = tk.Entry(root, bg="#FFFFE0")
search_entry.grid(row=7, column=1, padx=10, pady=5)

search_button = tk.Button(
    root, text="Search", command=search_contact, bg="#87CEEB")
search_button.grid(row=8, column=0, columnspan=2, pady=10)

contact_list = tk.Listbox(root, bg="#FFFFE0")
contact_list.grid(row=0, column=2, rowspan=9, padx=10, pady=5, sticky="nsew")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)


root.mainloop()


# In[ ]:




