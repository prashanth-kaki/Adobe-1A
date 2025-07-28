import fitz  # PyMuPDF
import re
import json


def classify_heading(size, fontname):
    if size > 16:
        return "H1"
    elif size > 13:
        return "H2"
    elif size > 11:
        return "H3"
    else:
        return None


def is_heading(text):
    text = text.strip()
    if not text or len(text) < 3:
        return False
    return (
        bool(re.match(
            r'^(Appendix|Chapter|Section|Figure|Table)\b',
            text,
            re.I
        )) or bool(re.match(r'^(?:[0-9]+\.){1,3}', text)) or text.isupper()
    )


def extract_headings(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span["text"].strip()
                    size = span["size"]
                    font = span["font"]
                    if is_heading(text):
                        level = classify_heading(size, font)
                        if level:
                            outline.append({
                                "level": level,
                                "text": text,
                                "page": page_num
                            })

    return {
        "title": doc.metadata.get("title", "Untitled"),
        "outline": outline
    }


if __name__ == "__main__":
    pdf_file = "input/file03.pdf"  # Replace with your actual file name
    result = extract_headings(pdf_file)

    # Save as JSON
    with open("output/file03_extracted.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

    print("✅ Headings extracted and saved to output/file03_extracted.json")
