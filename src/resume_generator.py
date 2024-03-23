from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

def clean_latex_response(latex_response):
    start_delimiter = "```latex"
    end_delimiter = "```"
    cleaned_response = latex_response.replace(start_delimiter, "").replace(end_delimiter, "")
    return cleaned_response.strip()

def generate_resume_content(job_title, company, job_description, resume_info, template_content):
    prompt_text = f"""

Given the job title "{job_title}", the company "{company}", and a comprehensive job description, utilize the provided standard resume content and a LaTeX template to generate a customized resume. This resume must:

Showcase skills and experiences most relevant to the job and company, aligning with the job description's requirements and preferences.
Prioritize information that emphasizes the applicant's suitability for the role, focusing on:
Technical skills and relevant projects.
Professional experiences, with a preference for internships over personal projects when space is limited.
Education details, which must always be included, along with any notable certifications.
Be exactly one page, efficiently utilizing space to include as much relevant information as possible, with slight modifications to the template's spacing allowed for fitting content.
Variables:

Job Title: {job_title}
Company: {company}
Job Description: {job_description}
Standard Resume Content: {resume_info}
LaTeX Resume Template: {template_content}
Generate a professional LaTeX resume document, ensuring it is precisely tailored to demonstrate why the applicant is an excellent match for the job at this specific company. The content should be arranged to reflect the priorities based on the job offer, the company's profile, and the role's demands within the tech domain.
    """
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system","content": "You are a highly skilled AI, specialized in crafting professional resumes exclusively in LaTeX format. Your task is to synthesize provided details into a concise, one-page resume that aligns with the specific demands of a job in the tech industry, ranging from data science to AI product management and development roles. The output must be clean LaTeX code, ready for direct conversion into PDF, without any extraneous comments, TODOs, or elements outside of the LaTeX code."},
            {"role": "user", "content": prompt_text}
        ]
    )
    
    
    latex_code = clean_latex_response(response.choices[0].message.content)
    return latex_code
