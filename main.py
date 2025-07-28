import os
import fitz
import json
from extract_outline import extract_outline_from_toc
from utils import detect_headings_no_toc, extract_title

INPUT_DIR = "./input"
OUTPUT_DIR = "./output"


def process_pdf(pdf_path, output_path):
    doc = fitz.open(pdf_path)
    outline = extract_outline_from_toc(doc)
    if not outline:
        outline = detect_headings_no_toc(doc)
    title = extract_title(doc)
    data = {
        "title": title,
        "outline": outline
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    doc.close()


def main():
    for file in os.listdir(INPUT_DIR):
        if file.lower().endswith(".pdf"):
            input_path = os.path.join(INPUT_DIR, file)
            out_file = file.rsplit(".", 1)[0] + ".json"
            output_path = os.path.join(OUTPUT_DIR, out_file)
            process_pdf(input_path, output_path)


if __name__ == "__main__":
    main()
