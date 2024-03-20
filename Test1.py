import os
import subprocess
import openai
from dotenv import load_dotenv

# Function to prompt user for job application details
def get_job_application_details():
    job_title = input("Enter the job title: ")
    company = input("Enter the company name: ")
    job_description = input("Enter the job description: ")
    return job_title, company, job_description

# Function to generate resume content using ChatGPT
def generate_resume_content(job_title, company, job_description):
    # Load environment variables and set API key
    load_dotenv()
    openai.api_key = os.getenv('OPENAI_API_KEY')

    response = openai.Completion.create(
        model="gpt-4",
        prompt=f"""
        Given the job title "{job_title}", the company "{company}", and the following job description:
        {job_description}

        Generate a professional resume that covers exactly one full page, tailored to this job application.
        """,
        temperature=0.5,
        max_tokens=1024
    )
    return response.choices[0].text

# Function to update LaTeX template with generated resume content
def update_latex_template_with_resume(content, template_path="template.tex", output_path="resume.tex"):
    with open(template_path, 'r') as file:
        template = file.read()

    # Assuming your LaTeX template has a placeholder for the resume content
    resume_latex = template.replace('%RESUME_CONTENT%', content)

    with open(output_path, 'w') as file:
        file.write(resume_latex)

# Function to compile LaTeX document to PDF
def compile_latex_to_pdf(latex_file="resume.tex"):
    # Change the command if necessary depending on your LaTeX installation
    command = ["pdflatex", "-interaction=nonstopmode", latex_file]
    subprocess.run(command, check=True)

    print("PDF compilation complete.")

def main():
    job_title, company, job_description = get_job_application_details()
    resume_content = generate_resume_content(job_title, company, job_description)
    update_latex_template_with_resume(resume_content)
    compile_latex_to_pdf()

if __name__ == "__main__":
    main()
