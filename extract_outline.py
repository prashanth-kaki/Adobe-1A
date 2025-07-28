def extract_outline_from_toc(doc):
    toc = doc.get_toc(simple=True)
    outline = []
    for item in toc:
        level, text, page = item[:3]
        if level > 4:
            continue
        outline.append({
            "level": f"H{level}",
            "text": text.strip(),
            "page": page
        })
    return outline
