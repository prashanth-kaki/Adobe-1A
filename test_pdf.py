import fitz

doc = fitz.open("input/file04.pdf")
print(f"Number of pages: {len(doc)}")
