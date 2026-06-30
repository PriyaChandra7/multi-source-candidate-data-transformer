print("Main file started")

import argparse
from validator import validate_profile
from file_parser import read_csv, read_resume
from extractor import extract_resume_fields
from normalizer import normalize_profile
from merger import merge_profiles
from confidence import calculate_confidence
from projector import load_config, project_profile
import json
import os


def get_arguments():
    parser = argparse.ArgumentParser(
        description="Multi-Source Candidate Data Transformer"
    )

    parser.add_argument(
        "--csv",
        default="../input/recruiter.csv",
        help="Path to recruiter CSV"
    )

    parser.add_argument(
        "--resume",
        default="../input/resume.pdf",
        help="Path to resume PDF"
    )

    parser.add_argument(
        "--config",
        default="../config/default.json",
        help="Path to configuration JSON"
    )

    return parser.parse_args()

def main():

  args = get_arguments()
  # Step 1: Read input files
  csv_data = read_csv(args.csv)
  resume_text = read_resume(args.resume)

  if resume_text is None:
    print("Resume could not be loaded. Exiting pipeline.")
    return

  # Step 2: Extract fields
  resume_profile = extract_resume_fields(resume_text)

  # Step 3: Normalize
  normalized_profile = normalize_profile(resume_profile)

  # Step 4: Merge
  candidate_profile = merge_profiles(csv_data, normalized_profile)

  # Step 5: Calculate confidence
  candidate_profile = calculate_confidence(
      candidate_profile,
      csv_data,
      normalized_profile
  )

  # Step 6: Load configuration
  config = load_config(args.config)

  # Step 7: Project output
  final_output = project_profile(candidate_profile, config)

  validate_profile(final_output)

  # Step 8: Create output folder if it doesn't exist
  os.makedirs("../output", exist_ok=True)

  # Step 9: Save Canonical Profile
  with open("../output/canonical_profile.json", "w") as file:
      json.dump(candidate_profile, file, indent=4)

  # Step 10: Save Final Output
  with open("../output/final_output.json", "w") as file:
      json.dump(final_output, file, indent=4)

  print("\n✅ Pipeline executed successfully!")
  print("Canonical profile saved in output/canonical_profile.json")
  print("Final projected output saved in output/final_output.json")

if __name__ == "__main__":
  main()