import tkinter as tk
from tkinter import messagebox

def save_user_name(user_name):
    try:
        with open("data/user.txt", "a") as file:
            file.write(user_name + "\n")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save user name: {e}")

class UserNameEntryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("User Name Entry")
        self.geometry("400x300")

        tk.Label(self, text="Enter User Name", font=("Helvetica", 18, "bold")).pack(pady=20)

        tk.Label(self, text="User Name:").pack(pady=5)
        self.user_name_entry = tk.Entry(self, width=30)
        self.user_name_entry.pack(pady=5)

        tk.Button(self, text="Save", command=self.save_user_name).pack(pady=20)

    def save_user_name(self):
        user_name = self.user_name_entry.get().strip()
        if user_name:
            save_user_name(user_name)
            messagebox.showinfo("Success", "User name saved successfully!")
            self.user_name_entry.delete(0, tk.END)  # Clear the entry field
        else:
            messagebox.showerror("Error", "User name cannot be empty.")

if __name__ == "__main__":
    app = UserNameEntryApp()
    app.mainloop()