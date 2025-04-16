import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def read_password():
    try:
        with open("data/password.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def read_user():
    try:
        with open("data/user.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def open_dashboard():
    dashboard = tk.Toplevel()
    dashboard.title("Dashboard")
    dashboard.geometry("500x400")

    tk.Label(dashboard, text="Welcome to the Dashboard", font=("Helvetica", 16, "bold")).pack(pady=20)

    ttk.Button(dashboard, text="View Students", command=lambda: messagebox.showinfo("View Students", "Feature not implemented yet.")).pack(pady=10)
    ttk.Button(dashboard, text="Add Student", command=lambda: messagebox.showinfo("Add Student", "Feature not implemented yet.")).pack(pady=10)
    ttk.Button(dashboard, text="Delete Student", command=lambda: messagebox.showinfo("Delete Student", "Feature not implemented yet.")).pack(pady=10)

    ttk.Button(dashboard, text="Logout", command=dashboard.destroy).pack(pady=20)

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("400x300")
        self.configure(bg="#f0f0f0")

        tk.Label(self, text="Login", font=("Helvetica", 18, "bold"), bg="#f0f0f0").pack(pady=20)

        tk.Label(self, text="User Name:", bg="#f0f0f0").pack(pady=5)
        self.user_entry = tk.Entry(self, width=30)
        self.user_entry.pack(pady=5)

        tk.Label(self, text="Password:", bg="#f0f0f0").pack(pady=5)
        self.password_entry = tk.Entry(self, show="*", width=30)
        self.password_entry.pack(pady=5)

        ttk.Button(self, text="Login", command=self.check_credentials).pack(pady=20)

    def check_credentials(self):
        entered_user = self.user_entry.get()
        entered_password = self.password_entry.get()
        actual_users = read_user()
        actual_password = read_password()

        if not actual_users:
            messagebox.showerror("Error", "User file not found or empty.")
        elif actual_password is None:
            messagebox.showerror("Error", "Password file not found.")
        elif entered_user in actual_users and entered_password == actual_password:
            messagebox.showinfo("Success", "Login successful!")
            self.destroy()  # Close the login window
            open_dashboard()
        else:
            messagebox.showerror("Error", "Incorrect username or password.")

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()