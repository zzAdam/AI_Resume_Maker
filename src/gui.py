import tkinter as tk
from tkinter import messagebox
import threading
from resume_generator import generate_resume_content
from utils import compile_latex_to_pdf, update_latex_template_with_resume
import time

def loading_animation(stop_event):
    # Animation frames
    while not stop_event.is_set():
        for frame in ["", ".", "..", "..."]:
            if stop_event.is_set():
                break
            status_label.config(text="Processing" + frame)
            app.update_idletasks()
            time.sleep(0.5)  # Adjust speed of animation if necessary

def simulate_long_process(stop_event):
    # Show loading animation in a separate thread to keep the UI responsive
    threading.Thread(target=loading_animation, args=(stop_event,)).start()

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

def generate_resume(stop_event):
    job_title = job_title_entry.get().strip()
    company = company_name_entry.get().strip()
    job_description = job_description_text.get("1.0", "end-1c").strip()

    # This function now takes a stop_event argument to control the loading animation
    simulate_long_process(stop_event)

    with open('documents/Initial_resume.txt', 'r') as file:
        resume_info = file.read()
    with open('templates/template.tex', 'r') as file:
        template_content = file.read()

    latex_code = generate_resume_content(job_title, company, job_description, resume_info, template_content)
    update_latex_template_with_resume(latex_code, "output/resume.tex")
    compile_latex_to_pdf("output/resume.tex")
    
    stop_event.set()  # Signal the loading animation to stop
    status_label.config(text="Resume Generated Successfully")

def start_resume_generation_thread():
    if validate_inputs():
        stop_event = threading.Event()
        threading.Thread(target=generate_resume, args=(stop_event,)).start()

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

app.grid_columnconfigure(1, weight=1)
app.mainloop()
