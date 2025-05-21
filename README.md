# AI CV Analyzer using Smolagent 

This project uses an AI agent powered by [Smolagent](https://huggingface.co/docs/smolagents) and Hugging Face Inference API to extract structured data from CVs (in PDF format). It parses resumes and returns details like personal information, education, work experience, skills, certifications, and sentiment, all formatted in JSON.

## 🔍 Key Features
- 📄 Automatic PDF resume text extraction
- 🧠 AI-powered field extraction via Smolagent + Hugging Face
- 📊 Outputs structured, consistent JSON for further analysis


## 🛠 Technologies Used
- Python
- Smolagent (Hugging Face)
- PyMuPDF
- dotenv

## 📁 Output Example
```json
{
  "personal_details": {"name": "...", "email": "...", "phone": "..."},
  "education": [...],
  "work_experience": [...],
  "skills": [...],
  "certifications": [...],
  "sentiment": "positive"
}
