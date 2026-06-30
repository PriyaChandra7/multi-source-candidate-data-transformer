import pandas as pd
import fitz

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
    Reads resume PDF and returns extracted text.
    """

    try:
        doc = fitz.open(resume_path)

        text = ""

        for page in doc:
            text += page.get_text()

        doc.close()

        print("✓ Resume PDF loaded successfully.")

        return text

    except Exception as e:
        print(f"Error reading resume PDF: {e}")
        return None