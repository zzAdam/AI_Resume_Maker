import tkinter as tk
from tkinter import ttk, messagebox
import threading
import os
from resume_generator import generate_resume_content
from utils import compile_latex_to_pdf, update_latex_template_with_resume, pdf_to_text
import time  # Make sure to import time

def simulate_long_process():
    progress_bar['value'] = 0
    app.update_idletasks()
    for _ in range(10):
        progress_bar['value'] += 10
        app.update_idletasks()
        time.sleep(1)  # Simulate a time-consuming task
    progress_bar['value'] = 0

def validate_inputs():
    # Retrieve values from inputs
    job_title = job_title_entry.get().strip()
    company = company_name_entry.get().strip()
    job_description = job_description_text.get("1.0", "end-1c").strip()

    # Check if any field is empty
    if not job_title or not company or not job_description:
        messagebox.showerror("Error", "Please fill in all fields before generating the resume.")
        return False
    return True

def start_resume_generation_thread():
    if validate_inputs():
        threading.Thread(target=generate_resume).start()

def generate_resume():
    job_title = job_title_entry.get().strip()
    company = company_name_entry.get().strip()
    job_description = job_description_text.get("1.0", "end-1c").strip()

    simulate_long_process()

    with open('documents/Initial_resume.txt', 'r') as file:
        resume_info = file.read()
    with open('templates/template.tex', 'r') as file:
        template_content = file.read()
    
    latex_code = generate_resume_content(job_title, company, job_description, resume_info, template_content)
    update_latex_template_with_resume(latex_code, "output/resume.tex")
    compile_latex_to_pdf("output/resume.tex")
    status_label.config(text="Resume Generated Successfully")

app = tk.Tk()
app.title("Resume Generator")

tk.Label(app, text="Job Title:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
job_title_entry = tk.Entry(app)
job_title_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

tk.Label(app, text="Company Name:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
company_name_entry = tk.Entry(app)
company_name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

tk.Label(app, text="Job Description:").grid(row=2, column=0, padx=10, pady=10, sticky="nw")
job_description_text = tk.Text(app, height=10)
job_description_text.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

generate_button = tk.Button(app, text="Generate Resume", command=start_resume_generation_thread)
generate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

status_label = tk.Label(app, text="")
status_label.grid(row=5, column=0, columnspan=2)

progress_bar = ttk.Progressbar(app, orient='horizontal', length=100, mode='determinate')
progress_bar.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

app.grid_columnconfigure(1, weight=1)
app.mainloop()
