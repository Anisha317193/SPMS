import tkinter as tk
from tkinter import messagebox
from admin_dashboard import AdminDashboard
from student_dashboard import StudentDashboard

PASSWORD_FILE = "data/password.txt"

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login - student Management system")
        self.geometry("300x200")
        self.resizable(False, False)

        tk.Label(self, text="Student Management system", font=("Helvetica", 16, "bold")).pack(pady=15)

        tk.Label(self, text="Username / Student ID").pack()
        self.username_entry = tk.Entry(self, width=30)
        self.username_entry.pack(pady=5)

        tk.Label(self, text="Password").pack()
        self.password_entry = tk.Entry(self, show="*", width=30)
        self.password_entry.pack(pady=5)

        self.role_var = tk.StringVar(value="student")
        role_frame = tk.Frame(self)
        role_frame.pack(pady=10)

        tk.Radiobutton(role_frame, text="Admin", variable=self.role_var, value="admin").pack(side="left", padx=10)
        tk.Radiobutton(role_frame, text="Student", variable=self.role_var, value="student").pack(side="left", padx=10)

        tk.Button(self,text="Login", width=15, command=self.login).pack(pady=15)

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        selected_role  = self.role_var.get()

        if not username or not password:
            messagebox.showwarning("Input Error", "please fill in all fields.")
            return
            
        try:
            with open(PASSWORD_FILE, "r") as f:
                for line in f:
                    stored_user, stored_pass, stored_role = line.strip().split(",")
                    if username == stored_user and password == stored_pass and selected_role == stored_role:
                       self.destroy()
                       if stored_role == "admin":
                          AdminDashboard().mainloop()
                       else:
                        StudentDashboard(student_id=username).mainloop()
                       return
            messagebox.showerror("Login Failed", "Invalid username,password, or role.")
        except FileNotFoundError:
            messagebox.showerror("File Error", "Password file not found.")

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()                        

