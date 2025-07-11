import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task.strip():
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        del tasks[selected_task_index]
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def mark_task_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        tasks[selected_task_index] = f"✔️ {task}"
        task_listbox.delete(selected_task_index)
        task_listbox.insert(tk.END, tasks[selected_task_index])
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

def search_task():
    query = task_entry.get().strip()
    if query:
        task_listbox.delete(0, tk.END)
        matches = [task for task in tasks if query.lower() in task.lower()]
        for match in matches:
            task_listbox.insert(tk.END, match)
        if not matches:
            messagebox.showinfo("Search Result", "No tasks match your query.")
    else:
        messagebox.showwarning("Input Error", "Please enter a search term.")

def reset_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("1920x1080")

# Tasks list
tasks = []

# Title Label
title_label = tk.Label(root, text="My To-Do List", font=("Centaur", 24, "bold"), bg="#01F9C6", fg="#4a4a4a")
title_label.pack(pady=10)

# Widgets
frame = tk.Canvas(root, bg="white", width=350, height=50, highlightthickness=0)
frame.pack(pady=10)
circle = frame.create_oval(5, 5, 45, 45, fill="lightblue", outline="lightblue")

task_entry = tk.Entry(frame, width=30, font=("Arial", 14), bg="#ffffff", fg="#4a4a4a", bd=2, relief="groove")
task_entry.pack(side=tk.LEFT, padx=10)

search_button = tk.Button(frame, text="Search", command=search_task, bg="#3EB489", fg="#ffffff", font=("Arial", 12, "bold"), padx=10, pady=5, relief="flat")
search_button.pack(side=tk.LEFT, padx=5)

# Floating Add Task Button
add_task_button = tk.Button(root, text="+", command=add_task, bg="#4caf50", fg="#ffffff", font=("Arial", 18, "bold"), width=3, height=1, relief="flat", cursor="hand2")
add_task_button.place(relx=0.85, rely=0.15)

# Task Listbox
task_listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 14), bg="#ffffff", fg="#4a4a4a", bd=2, relief="sunken", selectbackground="#4caf50", selectforeground="#ffffff")
task_listbox.pack(pady=10)

# Buttons Frame
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=10)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, bg="#22CE83", fg="#ffffff", font=("Boucherie Block", 12, "bold"), padx=10, pady=5, relief="flat")
delete_button.pack(side=tk.LEFT, padx=5)

complete_button = tk.Button(button_frame, text="Mark Completed", command=mark_task_completed, bg="#3CB371", fg="#ffffff", font=("Boucherie Block", 12, "bold"), padx=10, pady=5, relief="flat")
complete_button.pack(side=tk.LEFT, padx=5)

reset_button = tk.Button(button_frame, text="Reset", command=reset_list, bg="#1AA260", fg="#ffffff", font=("Boucherie Block", 12, "bold"), padx=10, pady=5, relief="flat")
reset_button.pack(side=tk.LEFT, padx=5)

# Run the application
root.mainloop()