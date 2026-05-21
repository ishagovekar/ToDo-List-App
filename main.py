from tkinter import *

# ---------------- WINDOW ---------------- #

root = Tk()
root.title("To-Do List App")
root.geometry("500x600")
root.config(bg="#f0f0f0")

# ---------------- FUNCTIONS ---------------- #

def add_task():
    task = task_entry.get()

    if task != "":
        task_listbox.insert(END, "📝 " + task)
        task_entry.delete(0, END)

def delete_task():
    selected_task = task_listbox.curselection()

    if selected_task:
        task_listbox.delete(selected_task)

def mark_complete():
    selected_task = task_listbox.curselection()

    if selected_task:
        task = task_listbox.get(selected_task)

        if "✅" not in task:
            updated_task = "✅ " + task
            task_listbox.delete(selected_task)
            task_listbox.insert(selected_task, updated_task)

# ---------------- HEADING ---------------- #

title_label = Label(
    root,
    text="To-Do List App",
    font=("Arial", 24, "bold"),
    bg="#f0f0f0",
    fg="black"
)

title_label.pack(pady=20)

# ---------------- ENTRY ---------------- #

task_entry = Entry(
    root,
    font=("Arial", 16),
    width=25
)

task_entry.pack(pady=10)

# ---------------- BUTTONS ---------------- #

add_button = Button(
    root,
    text="Add Task",
    font=("Arial", 14, "bold"),
    bg="green",
    fg="white",
    padx=10,
    pady=5,
    command=add_task
)

add_button.pack(pady=5)

complete_button = Button(
    root,
    text="Mark Complete",
    font=("Arial", 14, "bold"),
    bg="blue",
    fg="white",
    padx=10,
    pady=5,
    command=mark_complete
)

complete_button.pack(pady=5)

delete_button = Button(
    root,
    text="Delete Task",
    font=("Arial", 14, "bold"),
    bg="red",
    fg="white",
    padx=10,
    pady=5,
    command=delete_task
)

delete_button.pack(pady=5)

# ---------------- LISTBOX ---------------- #

task_listbox = Listbox(
    root,
    font=("Arial", 14),
    width=35,
    height=15,
    selectbackground="lightblue"
)

task_listbox.pack(pady=20)

# ---------------- RUN WINDOW ---------------- #

root.mainloop()