import os
import subprocess
from openai import OpenAI
from dotenv import load_dotenv
import fitz  # PyMuPDF
from pdflatex import PDFLaTeX

load_dotenv()
client = OpenAI()

def get_job_application_details():
    job_title = input("Enter the job title: ")
    company = input("Enter the company name: ")
    with open('job_description.txt', 'r') as file:
        job_description = file.read()
    return job_title, company, job_description

def clean_latex_response(latex_response):
    # Define the start and end delimiters for Markdown code blocks
    start_delimiter = "```latex"
    end_delimiter = "```"

    # Remove the delimiters
    cleaned_response = latex_response.replace(start_delimiter, "").replace(end_delimiter, "")

    return cleaned_response.strip()


def generate_resume_content(job_title, company, job_description, resume_info, template_content):
    prompt_text = f"""
    Given the job title "{job_title}", the company "{company}", and the following job description:
    {job_description} along with the standard resume info below and a LaTeX template, generate a customized version of the resume in LaTeX format. The revised resume should emphasize the skills and experiences most relevant to the job and company, aligning with the requirements and preferences mentioned in the job description. Make sure to prioritize information that showcases the applicant's qualifications for this specific role, focusing on technical skills, relevant projects, and past work experiences that demonstrate a fit for the company culture and the responsibilities of the position.

    - **Standard Resume Content:**
    {resume_info}

    - **LaTeX Resume Template:**
    {template_content}

    Generate a professional LaTeX resume document that covers exactly one full page, incorporating the customized resume content, adhering to the format specified in the provided template. The goal is to highlight why the applicant is an excellent match for this job at this company, based on the information provided. 
    """
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system","content": "You are a highly skilled AI, trained to assist with creating professional resumes. You can only return Latex code, without anything else"},
            {"role": "user", "content": prompt_text}
        ]
    )
    
    
    latex_code = clean_latex_response(response.choices[0].message.content)
    return latex_code



def update_latex_template_with_resume(content, output_path="resume.tex"):
    with open(output_path, 'w') as file:
        file.write(content)

def compile_latex_to_pdf(latex_file='resume.tex'):
    pdfl = PDFLaTeX.from_texfile(latex_file)
    pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=True)
    print("PDF compilation complete.")

def pdf_to_text(pdf_path, txt_path):
    with fitz.open(pdf_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
        with open(txt_path, "w") as txt_file:
            txt_file.write(text)

def main():
    pdf_path = "Initial_resume.pdf"
    txt_path = "Initial_resume.txt"
    pdf_to_text(pdf_path, txt_path)
    
    with open('Initial_resume.txt', 'r') as file:
        resume_info = file.read()
    with open('template.tex', 'r') as file:
        template_content = file.read()

    job_title, company, job_description = get_job_application_details()
    resume_content = generate_resume_content(job_title, company, job_description, resume_info, template_content)
    update_latex_template_with_resume(resume_content)
    compile_latex_to_pdf('resume.tex')

if __name__ == "__main__":
    main()