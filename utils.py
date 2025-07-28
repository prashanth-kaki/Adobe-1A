import re


def detect_headings_no_toc(doc):
    """
    Detect headings from PDF text when no TOC is present.
    Uses font size, uppercase text, and specific keywords.
    """
    all_spans = []

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span.get("text", "").strip()
                    if not text or len(text) > 150 or len(text.split()) < 2:
                        continue

                    # Heading heuristics
                    keyword_pattern = (
                        r"^(Appendix|Chapter|Section|Summary|Background|"
                        r"Timeline|Milestones|Evaluation|Approach|Terms|"
                        r"Membership|Chair|Meetings|Preamble)\b"
                    )
                    numbered_pattern = r"^(?:\d{1,2}[.)])"
                    if (
                        text.isupper()
                        or bool(re.match(keyword_pattern, text, re.I))
                        or bool(re.match(numbered_pattern, text))
                    ):
                        all_spans.append({
                            "text": text,
                            "size": span["size"],
                            "page": page_num
                        })

    if not all_spans:
        return []

    # Map top 4 font sizes to H1–H4
    sizes = sorted({span["size"] for span in all_spans}, reverse=True)
    level_map = {size: f"H{idx+1}" for idx, size in enumerate(sizes[:4])}

    headings = []
    for span in all_spans:
        level = level_map.get(span["size"], "H4")
        headings.append({
            "level": level,
            "text": span["text"],
            "page": span["page"]
        })

    return headings


def extract_title(doc):
    """
    Extract a meaningful title from PDF.
    Returns an empty string if no valid title found.
    """
    meta_title = doc.metadata.get("title", "").strip()
    if (
        meta_title
        and not meta_title.lower().endswith(
            (".pdf", ".cdr", ".doc", ".docx", ".txt")
        )
    ):
        return meta_title

    try:
        page = doc[0]
        spans = []
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span.get("text", "").strip()
                    if (
                        text
                        and len(text) > 10
                        and not text.lower().startswith("page")
                    ):
                        spans.append((span["size"], text))
        if spans:
            return max(spans, key=lambda x: x[0])[1]
    except Exception:
        pass

    return ""
