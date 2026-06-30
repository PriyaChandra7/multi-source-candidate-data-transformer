from file_parser import read_csv, read_resume


def main():
    # Read CSV
    csv_data = read_csv("../input/recruiter.csv")

    # Read Resume
    resume_data = read_resume("../input/resume.txt")

    # Print results
    print("\n----- CSV DATA -----")
    print(csv_data)

    print("\n----- RESUME DATA -----")
    print(resume_data)


if __name__ == "__main__":
    main()