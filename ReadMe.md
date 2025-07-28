# 🧠 Adobe India Hackathon - Challenge 1A
Structured PDF Outline & Title Extractor

This project extracts a structured outline (H1-H4) and a meaningful document title from PDF files using a combination of:
-- Table of Contents (TOC) extraction
-- Heuristic-based heading detection
-- Metadata/title inference

The output is saved in a structured JSON format, making it ideal for:
-- Content summarization
-- Semantic search indexing
-- Document analysis pipelines

## 🛠️ Tech Stack
Component	- Tool/Library
Language - Python 3.10+
PDF Parsing -	PyMuPDF (fitz)
Heuristics - Python re module
Output Format -	JSON
Docker Support - ✅ Yes

## 📁 Folder Structure

project/
│
├── main.py                 #Main runner script
├── utils.py                #Heuristic-based title + heading detection
├── extract_outline.py      #TOC-based heading extractor
├── extract_headings.py     #Alternate heading extractor (optional)
├── Dockerfile              #Docker configuration
├── requirements.txt        #Python dependencies
│
├── input/                  #Input PDFs
│   ├── file01.pdf
│   ├── file02.pdf
│   └── ...
│
└── output/                 #Output structured JSONs
    ├── file01.json
    ├── file02.json
    └── ...


## ⚙️ How It Works
1. Each .pdf file in the input/ folder is processed.

2. TOC Parsing:
  -- If a Table of Contents is available, it is extracted via get_toc() from PyMuPDF.

3. Heuristic Parsing (fallback):
  -- If TOC is absent, headings are inferred using:
      -- Font size hierarchy
      -- Capitalization logic
      -- Regular expression patterns

4. Title Extraction:
  -- Extracted from PDF metadata (if available), or
  -- Inferred from the largest-font text on the first page.

5. The result is saved to the output/ directory as a structured .json.

## 📥 Sample Input
Place your PDF files in the input/ folder. Example:
input/
├── file01.pdf
├── file02.pdf

## 📤 Sample Output
Each file will generate a corresponding .json in the output/ directory.

Example: file01.json
{
  "title": "Introduction to Machine Learning",
  "headings": [
    { "level": "H1", "text": "1. Introduction" },
    { "level": "H2", "text": "1.1 Supervised Learning" },
    { "level": "H3", "text": "1.1.1 Regression" },
    { "level": "H3", "text": "1.1.2 Classification" },
    { "level": "H2", "text": "1.2 Unsupervised Learning" },
    { "level": "H1", "text": "2. Applications" }
  ]
}

## 🚀 How to Run the Project
✅ Option 1: Local Setup (Recommended)
Step 1: Create a Virtual Environment
python -m venv venv

Step 2: Activate the Environment
Windows:
  .\venv\Scripts\activate
macOS/Linux:
  source venv/bin/activate

Step 3: Install Dependencies
pip install -r requirements.txt

Step 4: Run the Program
python main.py

🐳 Option 2: Docker (Portable and Easy to Share)
Step 1: Build the Docker Image
docker build -t pdf-outline-extractor .

Step 2: Run the Docker Container
Windows PowerShell:
  docker run --rm -v "${PWD}:/app" pdf-outline-extractor
Windows CMD:
  docker run --rm -v "%cd%:/app" pdf-outline-extractor
Linux/macOS:
  docker run --rm -v "$(pwd):/app" pdf-outline-extractor
  
✅ Outputs will be saved in the /output folder.