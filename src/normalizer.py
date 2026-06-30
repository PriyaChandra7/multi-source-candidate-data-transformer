import phonenumbers

def normalize_email(emails):
    """
    Convert all emails to lowercase.
    """

    normalized = []

    for email in emails:
        normalized.append(email.lower())

    return normalized

def normalize_phone(phones):
    """
    Convert phone numbers to E.164 format.
    """

    normalized = []

    for phone in phones:
        try:
            number = phonenumbers.parse(phone, "IN")

            normalized.append(
                phonenumbers.format_number(
                    number,
                    phonenumbers.PhoneNumberFormat.E164
                )
            )

        except:
            continue

    return normalized

def normalize_skills(skills):
    """
    Standardize skill names.
    """

    mapping = {

        "machine learning": "Machine Learning",
        "ml": "Machine Learning",

        "python": "Python",

        "java": "Java",

        "sql": "SQL"

    }

    normalized = []

    for skill in skills:

        key = skill.strip().lower()

        normalized.append(
            mapping.get(key, skill.title())
        )

    return list(set(normalized))

def normalize_profile(profile):

    profile["emails"] = normalize_email(profile["emails"])

    profile["phones"] = normalize_phone(profile["phones"])

    profile["skills"] = normalize_skills(profile["skills"])

    return profile