import pandas as pd


def read_csv(csv_path):
    """
    Reads recruiter CSV and returns a DataFrame.
    """
    try:
        data = pd.read_csv(csv_path)
        print("✓ CSV file loaded successfully.")
        return data
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return None


def read_resume(resume_path):
    """
    Reads resume text file and returns its content.
    """
    try:
        with open(resume_path, "r", encoding="utf-8") as file:
            text = file.read()

        print("✓ Resume loaded successfully.")
        return text

    except Exception as e:
        print(f"Error reading resume: {e}")
        return None