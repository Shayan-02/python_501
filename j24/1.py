import tkinter as tk
from tkinter import messagebox


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("مدیریت مخاطبین")
        self.contacts = []

        # ویجت‌ها
        self.name_label = tk.Label(root, text="نام:")
        self.name_label.grid(row=0, column=0)

        self.phone_label = tk.Label(root, text="شماره:")
        self.phone_label.grid(row=1, column=0)

        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1)

        self.add_button = tk.Button(root, text="افزودن مخاطب", command=self.add_contact)
        self.add_button.grid(row=2, column=0, columnspan=2)

        self.contact_listbox = tk.Listbox(root)
        self.contact_listbox.grid(row=3, column=0, columnspan=2)

        self.delete_button = tk.Button(
            root, text="حذف مخاطب", command=self.delete_contact
        )
        self.delete_button.grid(row=4, column=0, columnspan=2)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        if name and phone:
            contact = Contact(name, phone)
            self.contacts.append(contact)
            self.update_contact_list()
            self.clear_entries()
        else:
            messagebox.showwarning("خطا", "لطفا تمام فیلدها را پر کنید")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            del self.contacts[selected_index[0]]
            self.update_contact_list()
        else:
            messagebox.showwarning("خطا", "لطفا یک مخاطب را انتخاب کنید")

    def update_contact_list(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact.name} - {contact.phone}")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()
