import re

def extract_email(text):
    """
    Extract all email addresses from resume.
    """

    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    emails = re.findall(pattern, text)

    return list(set(emails))

def extract_phone(text):
    """
    Extract phone numbers from resume.
    """

    pattern = r"(\+?\d[\d\s-]{8,}\d)"

    phones = re.findall(pattern, text)

    return list(set(phones))

def extract_name(text):
    """
    Assume first non-empty line is candidate name.
    """

    lines = text.split("\n")

    for line in lines:
        if line.strip():
            return line.strip()

    return None


def extract_skills(text):
    """
    Extract skills listed after 'Skills:' section.
    """

    skills = []

    if "Skills:" in text:

        section = text.split("Skills:")[1]

        lines = section.strip().split("\n")

        for line in lines:

            line = line.strip()

            if line == "" or ":" in line:
                break

            skills.append(line)

    return skills

def extract_resume_fields(text):

    profile = {

        "full_name": extract_name(text),

        "emails": extract_email(text),

        "phones": extract_phone(text),

        "skills": extract_skills(text)

    }

    return profile