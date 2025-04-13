import tkinter as tk
from tkinter import ttk

class AdminDashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Admin Dashboard-student Management system")
        self.geometry("800x500")

        tk.Label(self, text="Admin Dashboard", font=("Helvetica",18, "bold")).pack(pady=10)

        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Grade"), show="headings")
        for col in ("ID", "Name", "Age", "Grade"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        self.tree.pack(pady=20, fill="x", padx=20)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Student",width=15, command=self.add_student).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="Update Student", width=15, command=self.update_student).grid(row=0,column=1, padx=10)
        tk.Button(button_frame, text="Delete Student", width=15, command=self.delete_student).grid(row=0, column=2, padx=10)
        tk.Button(button_frame, text="Refresh", width=15, command=self.refresh_table).grid(row=0, column=3, padx=10)

    def add_student(self):
        pass
    def update_student(self):
        pass
    def delete_student(self):
        pass
    def refresh_table(self):
        pass
if __name__ == "__main__":
    app = AdminDashboard()
    app.mainloop()