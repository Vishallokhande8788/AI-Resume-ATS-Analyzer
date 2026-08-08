# ⚡ Cyber-Onyx ATS Suite

## Enterprise AI Resume Intelligence & ATS Analyzer

Cyber-Onyx ATS Suite is an AI-powered resume analysis platform built
with Python, Streamlit, Gemini Vision, PDF processing, and a modern
dashboard UI.

**Live Demo:** https://ai-resume-analyzer8788.streamlit.app/

------------------------------------------------------------------------

## 📌 Project Overview

The platform analyzes a candidate's uploaded resume against a target Job
Description (JD).

The user provides:

1.  A target Job Description
2.  A Resume PDF

The application converts PDF pages into images and sends the resume
visual content together with the Job Description to Google's Gemini API.
Gemini returns structured JSON, which is rendered in an interactive
Streamlit dashboard.

------------------------------------------------------------------------

## 🎯 Objectives

-   Analyze resume compatibility with a target job.
-   Generate an AI-based ATS match score.
-   Identify relevant and missing skills.
-   Detect weak resume bullet points.
-   Generate stronger, achievement-oriented bullet suggestions.
-   Analyze keyword density.
-   Evaluate resume formatting and readability.
-   Generate contextual interview questions.
-   Provide AI-based salary insights.
-   Export analysis as JSON.
-   Provide a modern dashboard for job seekers and recruiters.

------------------------------------------------------------------------

## ✨ Main Features

### 1. 🎯 ATS Scoring Hub

Provides:

-   ATS Match Index
-   Keyword Density
-   Format Precision
-   Action Verbs Impact
-   Readability Rating

Scores are generated from the uploaded resume and supplied Job
Description.

### 2. ✨ AI Bullet Point Optimizer

Identifies weak or vague resume statements and generates improved
versions using:

-   Strong action verbs
-   Technical scope
-   Quantifiable impact
-   Business value
-   Achievement-oriented wording

### 3. 📊 Skill Gap Analysis

Shows:

-   **Validated Skills:** relevant skills detected in the resume.
-   **Missing Critical Skills:** important skills from the Job
    Description that are not sufficiently demonstrated.

### 4. 💰 Predictive Salary Analytics

Generates AI-based estimates for:

-   Minimum compensation
-   Target compensation
-   Maximum compensation
-   Location adjustment
-   Skills that may increase market value

Salary figures are estimates and are not guaranteed compensation.

### 5. 🎯 Interview Preparation

Generates contextual interview questions based on the resume and target
Job Description, including technical, architecture, database, DevOps,
cloud, and performance topics.

Each question can include an AI-generated answer blueprint.

### 6. 📄 Resume PDF Viewer

Supports:

-   PDF upload
-   Multi-page PDF processing
-   Page preview
-   Page navigation
-   Visual resume rendering
-   AI vision analysis

### 7. 📥 JSON Report Export

The generated ATS analysis can be downloaded as a JSON report.

------------------------------------------------------------------------

## 🧠 AI Workflow

``` text
USER
  │
  ├── Job Description
  │
  └── Resume PDF
          │
          ▼
   Streamlit Application
          │
          ▼
      PDF Processing
          │
          ▼
    PDF Pages → Images
          │
          ▼
      Gemini Vision
          │
          ▼
   Structured JSON Analysis
          │
    ┌─────┼─────┬─────┐
    ▼     ▼     ▼     ▼
   ATS  Skills Bullets Interview
    │     │     │     │
    └─────┴─────┴─────┘
              │
              ▼
       Dashboard Results
              │
              ▼
          JSON Export
```

------------------------------------------------------------------------

## 🏗️ Technology Stack

  Technology                  Purpose
  --------------------------- -----------------------------------
  Python                      Core application logic
  Streamlit                   Web application and dashboard
  Google Gemini API           AI resume and JD analysis
  Google GenAI SDK            Gemini API integration
  pdf2image                   PDF page conversion
  Poppler                     PDF rendering dependency
  Pillow                      Image processing
  python-dotenv               Local environment variables
  HTML/CSS                    Modern dashboard UI
  JSON                        Structured AI response and export
  Git/GitHub                  Version control
  Streamlit Community Cloud   Deployment

------------------------------------------------------------------------

## 📂 Project Structure

``` text
AI-Resume-ATS-Analyzer/
│
├── app.py
├── requirements.txt
├── packages.txt
├── README.md
├── .gitignore
│
├── .env                  # Local only - never commit
└── venv/                 # Local virtual environment - never commit
```

------------------------------------------------------------------------

## ⚙️ Requirements

Recommended Python version:

``` text
Python 3.11
```

### requirements.txt

``` text
streamlit
google-genai
python-dotenv
Pillow
pdf2image
```

### packages.txt

``` text
poppler-utils
```

Poppler is required by `pdf2image` for PDF-to-image conversion on
Streamlit Community Cloud.

------------------------------------------------------------------------

## 🔐 API Key Configuration

### Local Development

Create `.env`:

``` env
GOOGLE_API_KEY=your_gemini_api_key
```

Never commit `.env` to GitHub.

Recommended `.gitignore`:

``` gitignore
.env
venv/
__pycache__/
*.pyc
.streamlit/secrets.toml
```

### Streamlit Community Cloud

Open:

**App → Settings → Secrets**

Add:

``` toml
GOOGLE_API_KEY = "your_gemini_api_key"
```

Do not expose the API key in source code.

------------------------------------------------------------------------

## 🚀 Local Installation

### 1. Clone the repository

``` bash
git clone https://github.com/Vishallokhande8788/AI-Resume-ATS-Analyzer.git
cd AI-Resume-ATS-Analyzer
```

### 2. Create virtual environment

``` bash
python -m venv venv
```

### 3. Activate it

Linux/macOS/Codespaces:

``` bash
source venv/bin/activate
```

Windows:

``` bash
venv\Scripts\activate
```

### 4. Install Python dependencies

``` bash
pip install -r requirements.txt
```

### 5. Install Poppler on Ubuntu/Debian

``` bash
sudo apt-get update
sudo apt-get install -y poppler-utils
```

### 6. Configure API key

Create `.env`:

``` env
GOOGLE_API_KEY=your_gemini_api_key
```

### 7. Run

``` bash
streamlit run app.py
```

------------------------------------------------------------------------

## ☁️ Streamlit Community Cloud Deployment

Deployment configuration:

``` text
Repository: AI-Resume-ATS-Analyzer
Branch: main
Main file: app.py
Python: 3.11
```

The repository root must contain:

``` text
app.py
requirements.txt
packages.txt
```

`packages.txt` must contain:

``` text
poppler-utils
```

This installs Poppler so `pdf2image` can process uploaded PDFs.

------------------------------------------------------------------------

## 🔄 Application Flow

### Step 1 --- Enter Job Description

The user enters the target Job Description.

### Step 2 --- Upload Resume

The user uploads a resume in PDF format.

### Step 3 --- Render PDF

Each PDF page is converted into a JPEG image.

### Step 4 --- Analyze with Gemini

The images and Job Description are sent to Gemini.

### Step 5 --- Receive JSON

Gemini returns structured analysis.

### Step 6 --- Display Dashboard

Streamlit renders the analysis in separate modules.

### Step 7 --- Export

The user can download the final JSON report.

------------------------------------------------------------------------

## 🛡️ Input Validation

The application should require both:

-   Resume PDF
-   Job Description

Candidate-specific analysis should only be displayed after successful
resume analysis.

The application should not display fabricated candidate information when
no resume has been uploaded.

------------------------------------------------------------------------

## 🔒 Security

-   Never commit API keys.
-   Keep `.env` out of Git.
-   Use Streamlit Secrets for cloud deployment.
-   Do not expose API keys in frontend HTML/CSS.
-   Validate uploaded files.
-   Avoid logging sensitive resume content.
-   Treat AI salary information as estimates.
-   Do not use AI output as the sole basis for employment decisions.

------------------------------------------------------------------------

## 🧪 Testing Checklist

-   [ ] Application starts successfully.
-   [ ] Job Description input works.
-   [ ] PDF upload works.
-   [ ] Multi-page PDF works.
-   [ ] PDF preview works.
-   [ ] Gemini API key works.
-   [ ] ATS analysis is generated.
-   [ ] Skill gap analysis works.
-   [ ] Bullet optimization works.
-   [ ] Interview questions are generated.
-   [ ] Salary analytics are displayed.
-   [ ] JSON report downloads.
-   [ ] Missing PDF is handled.
-   [ ] Missing Job Description is handled.
-   [ ] Invalid PDF is handled.
-   [ ] API key is not exposed on GitHub.

------------------------------------------------------------------------

## ⚠️ Important Notes

### Gemini API Quota

Gemini API usage is subject to the quota and rate limits of the
configured Google AI API plan and model. A `429 RESOURCE_EXHAUSTED`
response indicates that an applicable quota or rate limit has been
exceeded.

### AI Accuracy

ATS scores, skill gaps, salary estimates, and interview recommendations
are AI-generated decision-support information and are not guaranteed
results.

### Resume Privacy

Resumes can contain personal and professional information. Users should
upload documents only to services they trust.

------------------------------------------------------------------------

## 📈 Future Enhancements

Possible future improvements:

-   Resume-to-resume comparison
-   Multiple Job Description comparison
-   ATS keyword highlighting
-   Resume section optimization
-   Resume rewrite generation
-   Cover letter generation
-   LinkedIn profile optimization
-   DOCX resume support
-   PDF report generation
-   User authentication
-   Database-backed analysis history
-   Recruiter dashboard
-   Advanced analytics
-   RAG-based recruitment assistant
-   Multi-model AI support

------------------------------------------------------------------------

## 👨‍💻 Author

**Vishal Lokhande**

Full Stack Python Developer

**Skills:** Python • Django • React • REST APIs • AI Integration

------------------------------------------------------------------------

## 📜 License

No open-source license has been specified yet. Until a license is added,
the project should be treated as all rights reserved.

------------------------------------------------------------------------

## ⭐ Project Summary

Cyber-Onyx ATS Suite is a modern AI-powered resume intelligence platform
combining:

``` text
Python
+
Streamlit
+
PDF Processing
+
Gemini Vision AI
+
Structured JSON
+
Modern HTML/CSS UI
+
Cloud Deployment
```

It demonstrates practical AI integration into a Python-based application
for resume analysis, ATS optimization, skill-gap detection, salary
insights, and interview preparation.
