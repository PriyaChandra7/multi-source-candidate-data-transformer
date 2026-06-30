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
    Extract technical skills using keyword matching.
    Works with different resume formats.
    """

    skill_keywords = [
        "Python", "C", "C++", "Java", "SQL", "MySQL",
        "HTML", "CSS", "JavaScript",
        "Machine Learning", "Deep Learning", "TensorFlow",
        "OpenCV", "MediaPipe", "Flask", "Bootstrap",
        "Git", "GitHub", "VS Code",
        "DBMS", "OOP", "DSA"
    ]

    skills = []

    text_lower = text.lower()

    for skill in skill_keywords:
        if skill.lower() in text_lower:
            skills.append(skill)

    return skills

def extract_resume_fields(text):

    profile = {

        "full_name": extract_name(text),

        "emails": extract_email(text),

        "phones": extract_phone(text),

        "skills": extract_skills(text)

    }

    return profile