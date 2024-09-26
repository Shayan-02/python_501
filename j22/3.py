import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo App")
        self.tasks = []

        # Task list
        self.task_list = tk.Listbox(self.root, width=40, height=10)
        self.task_list.pack(padx=10, pady=10)

        # New task entry
        self.new_task_entry = tk.Entry(self.root, width=40)
        self.new_task_entry.pack(padx=10, pady=10)

        # Add task button
        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(padx=10, pady=10)

        # Delete task button
        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(padx=10, pady=10)

    def add_task(self):
        task = self.new_task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.new_task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
            self.tasks.pop(task_index)
        except:
            messagebox.showwarning("Warning", "Select a task to delete")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()