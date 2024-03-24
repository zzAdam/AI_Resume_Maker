# AIAutoResume

## Overview

AIAutoResume is a Python-based application designed to automatically generate tailored resumes for specific job applications using OpenAI's GPT models. By inputting a job title, company name, and job description, users can generate a resume that highlights relevant skills and experiences, aligning with the job's requirements. The application utilizes LaTeX for professional formatting, ensuring the final document is visually appealing and ready for submission.

## Features

- Custom resume generation based on job descriptions.
- Utilizes OpenAI GPT models for content creation.
- Professional formatting with LaTeX.
- Simple GUI for easy interaction.

## Installation

1. **Clone the repository**:
    ```
    git clone https://github.com/zzAdam/AI_Resume_Maker.git
    ```

2. **Navigate to the project directory**:
    ```
    cd AIAutoResume
    ```

3. **Create and activate a virtual environment** (optional but recommended):
   - On macOS/Linux:
     ```
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - On Windows:
     ```
     python -m venv .venv
     .\.venv\Scripts\activate
     ```

4. **Install the required dependencies**:
    ```
    pip install -r requirements.txt
    ```


## Configuration

Before using AIAutoResume, you must set up a few configurations:

- **OpenAI API Key**: Obtain an API key from [OpenAI](https://openai.com/api-keys/). This key is required to interact with OpenAI's GPT models for generating the resume content.
- **.env File**: Create a `.env` file in the root directory of the project and add your OpenAI API key as follows:

    ```
    OPENAI_API_KEY=your_api_key_here
    ```

This file is already included in the `.gitignore` to ensure your API key remains private.

## Usage

To start AIAutoResume, run the `main.py` script from your terminal or command prompt:

  ```
python src/main.py
  ```




This will launch the GUI, where you can enter the job title, company name, and job description. After filling in these fields, click the "Generate Resume" button to start the resume generation process. The application will create a customized resume based on the inputted information and save it in the `output` directory as a LaTeX file and a PDF document.

### Files and Directories

- **Documents**: Place your initial resume (PDF format) in the `documents` directory. This is used as the basis for customization.
- **Templates**: LaTeX templates should be stored in the `templates` directory. The application uses these templates to format the generated resume content.

## Platform Compatibility

AIAutoResume is compatible with macOS, Linux, and Windows operating systems. Ensure you have Python 3.6 or later installed on your system to run the application.

## Contributing

Contributions to AIAutoResume are welcome! If you have suggestions for improvements or bug fixes, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

For more information or help with AIAutoResume, please open an issue on this repository or contact me via my info you can find on my Website.
