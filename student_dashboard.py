import tkinter as tk
from tkinter import ttk

class StudentDashboard(tk.Tk):
    def __init__(self, student_id="S001"):
        super().__init__()
        self.title("student Dashboard - student Management System")
        self.geometry("600x400")
        self.student_id = student_id

        tk.Label(self, text="Student Dashboard", font=("Helvetica", 18, "bold")).pack(pady=10)
        tk.Label(self, text=f"student ID: {self.student_id}", font=("Helvetica", 12)).pack(pady=5)

        self.details_frame = tk.Frame(self)
        self.details_frame.pack(pady=20)

        self.name_label = tk.Label(self.details_frame, text="Name:", font=("Helvetica",12))
        self.age_label = tk.Label(self.details_frame, text="Age:",font=("Helvetica",12))
        self.grade_label = tk.Label(self.details_frame, text="Grade:", font=("Helvetica", 12))

        self.name_label.pack(anchor="w", padx=20)
        self.age_label.pack(anchor="w", padx=20)

        tk.Button(self, text="Logout", command=self.destroy).pack(pady=10)

        def load_student_data(self):
            pass
        if __name__ == "__main__":
            app = StudentDashboard()
            app.mainloop()
