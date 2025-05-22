import os
import fitz  # PyMuPDF
import json
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from smolagents import CodeAgent, InferenceClientModel

# Load Hugging Face token from .env
load_dotenv()
token = os.getenv("HUGGINGFACE_API_TOKEN")

if not token:
    raise EnvironmentError("Missing HUGGINGFACE_API_TOKEN in .env file")

# Setup HF Model with explicit model name
client = InferenceClient(token=token, model="HuggingFaceH4/zephyr-7b-beta")
model = InferenceClientModel(client=client)
agent = CodeAgent(tools=[], model=model)

# PDF Text Extraction
def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

# Field Extraction
def extract_fields(text):
    prompt = f"""
    Extract the following fields from the given CV text:\n\n{text}\n\n
    Fields needed: 
    - Personal details (Name, Email, Phone)\n    - Education (Degrees, Institutions, Dates)\n    - Work Experience (Position, Company, Duration, Responsibilities)\n    - Skills\n    - Certifications\n    - Sentiment (Positive, Neutral, Negative)

    """
    result = agent.run(prompt)
    return result

# Save Result to JSON
def format_and_save_json(extracted_json, output_file):
    try:
        data = json.loads(extracted_json)
    except json.JSONDecodeError as e:
        print("Failed to decode JSON:", e)
        print("Raw output:", extracted_json)
        return

    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)
    print(f" Structured data saved to: {os.path.abspath(output_file)}")

# main 
if __name__ == "__main__":
    pdf_text = extract_text_from_pdf("Resume.pdf")
    extracted_data_json = extract_fields(pdf_text)
    format_and_save_json(extracted_data_json, "cv.json")