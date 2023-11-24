#!/usr/bin/env python
# coding: utf-8

# In[7]:


import tkinter as tk


def add_task():
    task_text = entry_task.get()
    if task_text:
        task_listbox.insert(tk.END, task_text)
        entry_task.delete(0, tk.END)


def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        pass


def complete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_text = task_listbox.get(selected_task_index)
        if task_text.startswith("✔ "):
            return
        task_text = "✔ " + task_text
        task_listbox.delete(selected_task_index)
        task_listbox.insert(tk.END, task_text)
    except IndexError:
        pass


root = tk.Tk()
root.title("Ayandeep To_do_list")

root.configure(bg="#3498db")
input_frame = tk.Frame(root, bg="#3498db")
input_frame.pack(pady=10)

entry_task = tk.Entry(input_frame, font=("Arial", 14))
entry_task.grid(row=0, column=0, padx=10)

add_button = tk.Button(
    input_frame,
    text="Add Task",
    command=add_task,
    font=("Arial", 12),
    bg="#2ecc71",
    fg="white",
)
add_button.grid(row=0, column=1, padx=10)

delete_button = tk.Button(
    input_frame,
    text="Delete Task",
    command=delete_task,
    font=("Arial", 12),
    bg="#e74c3c",
    fg="white",
)
delete_button.grid(row=0, column=2, padx=10)

complete_button = tk.Button(
    input_frame,
    text="Complete Task",
    command=complete_task,
    font=("Arial", 12),
    bg="#f39c12",
    fg="white",
)
complete_button.grid(row=0, column=3, padx=10)

task_listbox = tk.Listbox(
    root, selectmode=tk.SINGLE, font=("Arial", 14), width=40, height=10
)
task_listbox.pack(padx=10, pady=10)

root.mainloop()


# In[ ]:





# In[ ]:




