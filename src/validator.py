def validate_profile(profile):

    required_fields = [
        "full_name",
        "primary_email",
        "phone",
        "skills"
    ]

    for field in required_fields:
        if field not in profile:
            raise ValueError(f"Missing required field: {field}")

    return True