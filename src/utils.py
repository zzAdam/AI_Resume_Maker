import subprocess
import fitz  # PyMuPDF
from pdflatex import PDFLaTeX
import os

def update_latex_template_with_resume(content, output_path="output/resume.tex"):
    with open(output_path, 'w') as file:
        file.write(content)


def compile_latex_to_pdf(latex_file='output/resume.tex'):
    # Ensure the output directory exists
    output_dir = os.path.dirname(latex_file)
    os.makedirs(output_dir, exist_ok=True)

    # Construct the command to call pdflatex
    command = ["pdflatex", "-interaction=nonstopmode", f"-output-directory={output_dir}", latex_file]

    try:
        # Execute the pdflatex command
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print("PDF compilation complete.")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        # Print any errors from the pdflatex command
        print(f"Failed to compile LaTeX file. Error: {e.stderr}")


def pdf_to_text(pdf_path="documents/Initial_resume.pdf", txt_path="documents/Initial_resume.txt"):
    with fitz.open(pdf_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
        with open(txt_path, "w") as txt_file:
            txt_file.write(text)
