import re
from collections import defaultdict

def find_paradoxes(text):
    sentences = re.split(r'[.!?]\s*', text.strip())
    pattern = re.compile(r'\b(?:[Aa]\s)?([a-zA-Z]+)\b\s+is\s+(an?|the)\s+([^\.\!\?]+)', re.IGNORECASE)
    descriptions = defaultdict(set)

    for sentence in sentences:
        match = pattern.search(sentence)
        if match:
            subject = match.group(1).strip().lower() 
            description = match.group(3).strip().lower()
            descriptions[subject].add(description)

    paradoxes = []
    for subject, desc_set in descriptions.items():
        if len(desc_set) > 1:
            paradoxes.append((subject, list(desc_set)))

    return paradoxes

if __name__ == "__main__":
    text = """
    A jaguar is an animal.
    A Jaguar is a car.
    The bat is a mammal.
    The bat is sports equipment.
    A pen is a writing instrument.
    A Pen is an enclosure for animals.
    A ball is a toy.
    A ball is a formal event.
    """

    paradoxes = find_paradoxes(text)

    if paradoxes:
        print("Potential paradoxes found:")
        for subject, descriptions in paradoxes:
            print(f"- {subject.capitalize()} has contradictory descriptions: {', '.join(descriptions)}")
    else:
        print("No paradoxes found.")