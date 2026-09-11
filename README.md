# AI Resume Analyzer

A beginner-friendly Streamlit application that compares a PDF or DOCX resume with a job description using the Groq API and returns a structured AI analysis.

## Features

- PDF resume extraction
- DOCX resume extraction
- Job description input
- Resume/job comparison
- Overall match score (0-100)
- Matching skills
- Missing or not clearly demonstrated skills
- ATS keywords
- Resume problems
- Recommendations
- Final result
- Structured JSON from the AI
- Modular project structure

## Project Structure

```text
ai-resume-analyzer/
├── app.py
├── analyzer.py
├── resume_parser.py
├── prompts.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

### Responsibilities

- `app.py`: Streamlit UI and application workflow.
- `resume_parser.py`: PDF/DOCX validation and text extraction.
- `prompts.py`: AI instructions, JSON schema, and prompt construction.
- `analyzer.py`: Groq communication, JSON parsing, and AI-result validation.
- `requirements.txt`: Python dependencies.
- `.env.example`: Example environment configuration.
- `.gitignore`: Prevents secrets and local files from being committed.
- `README.md`: Setup and usage documentation.

This separation follows Single Responsibility, Separation of Concerns, Loose Coupling, and High Cohesion.

## Requirements

- Python 3.10+
- A Groq API key
- Internet connection

## Setup

### 1. Extract the ZIP

Open a terminal in the project directory.

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Copy `.env.example` to `.env`.

Windows:

```bash
copy .env.example .env
```

macOS/Linux:

```bash
cp .env.example .env
```

Open `.env` and replace the placeholder:

```text
GROQ_API_KEY=your_real_groq_api_key
GROQ_MODEL=openai/gpt-oss-120b
```

Never commit `.env` to GitHub.

## Run the app

```bash
streamlit run app.py
```

Streamlit will provide a local URL, normally:

```text
http://localhost:8501
```

## How it works

```text
User
  ↓
Resume PDF/DOCX + Job Description
  ↓
Python validates input
  ↓
Python extracts resume text
  ↓
Python prepares AI request
  ↓
Groq LLM analyzes resume + job description
  ↓
Python validates structured JSON
  ↓
Streamlit displays results
```

## Python vs AI

### Python handles

- Streamlit interface
- File upload
- PDF/DOCX extraction
- Input validation
- Prompt construction
- Groq API communication
- JSON parsing and validation
- Results display

### AI handles

- Understanding the resume
- Understanding the job description
- Semantic comparison
- Matching skills
- Missing/not clearly demonstrated skills
- ATS keyword identification
- Resume problem identification
- Recommendations
- Final assessment

## Notes

The match score is an AI-generated assessment, not a guarantee that a recruiter or ATS will accept the resume. The analyzer should be used as decision support.

For scanned/image-only PDFs, text extraction may return little or no text because this MVP does not include OCR.

## Troubleshooting

### `GROQ_API_KEY is not set`

Make sure:

1. `.env` exists in the project root.
2. It contains a valid `GROQ_API_KEY`.
3. You restarted Streamlit after changing the environment file.

### No resume text extracted

Try a PDF/DOCX containing selectable text. Image-only/scanned PDFs are not supported by the current MVP.

### AI/API errors

Check your internet connection, API key, model availability, and Groq account/API limits.
