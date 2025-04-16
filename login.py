import tkinter as tk
from tkinter import messagebox

def read_password():
    try:
        with open("data/password.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("400x300")

        tk.Label(self, text="Login", font=("Helvetica", 18, "bold")).pack(pady=20)

        tk.Label(self, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(self, show="*", width=30)
        self.password_entry.pack(pady=5)

        tk.Button(self, text="Login", command=self.check_password).pack(pady=20)

    def check_password(self):
        entered_password = self.password_entry.get()
        actual_password = read_password()

        if actual_password is None:
            messagebox.showerror("Error", "Password file not found.")
        elif entered_password == actual_password:
            messagebox.showinfo("Success", "Login successful!")
            self.destroy()  # Close the login window
        else:
            messagebox.showerror("Error", "Incorrect password.")

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()