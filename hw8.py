# Hocam bu program şuan halihazırda verdiğiniz örnek üzerine sonuç üretiyor.
# Farklı inputları test etmek isterseniz 125-127. satırlarda değiştirebilirsiniz.

import re

def detect_format(citation: str) -> str:
    if re.search(r"\(\d{4}\)\.", citation):
        return "APA"
    
    if re.match(r"^[A-Z\s]+,", citation):  # e.g., "HOFSTADTER, Douglas R..."
        return "ISO"
    
    if re.search(r"\.\s*\w+.*,\s*\d{4}\.", citation):
        return "MLA"

    return "UNKNOWN"


def parse_mla(citation: str) -> dict:
    pattern = re.compile(
        r"^(?P<author>[^.]+)\.\s+(?P<title>[^.]+)\.\s+(?P<publisher>.*?),\s+(?P<year>\d{4})\.$"
    )
    match = pattern.match(citation.strip())
    if not match:
        return {}

    author = match.group("author").strip()
    title = match.group("title").strip()
    publisher = match.group("publisher").strip()
    year = match.group("year").strip()

    return {
        "author": author,
        "title": title,
        "publisher": publisher,
        "year": year
    }


def parse_apa(citation: str) -> dict:
    pattern = re.compile(
        r"^(?P<author>.+?)\s*\((?P<year>\d{4})\)\.\s+(?P<title>[^.]+)\.\s+(?P<publisher>[^.]+)\.?$"
    )
    match = pattern.match(citation.strip())
    if not match:
        return {}

    author = match.group("author").strip()
    year = match.group("year").strip()
    title = match.group("title").strip()
    publisher = match.group("publisher").strip()

    return {
        "author": author,
        "title": title,
        "publisher": publisher,
        "year": year
    }


def parse_iso(citation: str) -> dict:
    pattern = re.compile(
        r"^(?P<author>[^.]+)\.\s+(?P<title>[^.]+)\.\s+(?P<publisher>.*?),\s+(?P<year>\d{4})\.$"
    )
    match = pattern.match(citation.strip())
    if not match:
        return {}

    author = match.group("author").strip()
    title = match.group("title").strip()
    publisher = match.group("publisher").strip()
    year = match.group("year").strip()

    return {
        "author": author,
        "title": title,
        "publisher": publisher,
        "year": year
    }


def build_bibtex(reference_info: dict) -> str:
    author = reference_info.get("author", "Unknown Author")

    parts = author.split(",")
    if len(parts) > 1:
        surname = parts[0].strip()
    else:
        surname = author.split()[0] if author else "Unknown"

    year = reference_info.get("year", "XXXX")
    title = reference_info.get("title", "Untitled")
    publisher = reference_info.get("publisher", "Unknown Publisher")
    
    bibkey = f"{surname}_{year}"

    bibtex = f"""@book{{{bibkey},
    author = {{{author}}},
    title = {{{title}}},
    publisher = {{{publisher}}},
    year = {{{year}}}
}}"""
    return bibtex


def convert_reference(citation: str) -> str:
    
    fmt = detect_format(citation)
    if fmt == "MLA":
        data = parse_mla(citation)
    elif fmt == "APA":
        data = parse_apa(citation)
    elif fmt == "ISO":
        data = parse_iso(citation)
    else:
        return f"Error: Could not detect known format (MLA, APA, ISO) for citation:\n{citation}"

    if not data:
        return f"Error: Failed to parse the citation. Please check the format:\n{citation}"

    return build_bibtex(data)


def main():
    mla_ref =  "Hofstadter, Douglas R. Gödel, Escher, Bach: an eternal golden braid. Basic books, 1999."
    apa_ref =  "Hofstadter, D. R. (1999). Gödel, Escher, Bach: an eternal golden braid. Basic books."
    iso_ref =  "HOFSTADTER, Douglas R. Gödel, Escher, Bach: an eternal golden braid. Basic books, 1999."

    for ref in [mla_ref, apa_ref, iso_ref]:
        print("Original citation:")
        print(ref)
        print("BibTeX output:")
        print(convert_reference(ref))
        print("----------------------------------------------------")


if __name__ == "__main__":
    main()