def calculate_confidence(candidate_profile, csv_data, resume_profile):
      confidence = {}
      recruiter = csv_data.iloc[0]
      if recruiter["name"].strip().lower() == resume_profile["full_name"].strip().lower():
        confidence["full_name"] = 0.95
      else:
        confidence["full_name"] = 0.60

      if recruiter["email"].lower() in resume_profile["emails"]:
        confidence["emails"] = 0.95
      else:
        confidence["emails"] = 0.60

      if resume_profile["phones"]:
        confidence["phones"] = 0.85
      else:
        confidence["phones"] = 0.50

      if resume_profile["skills"]:
        confidence["skills"] = 0.85
      else:
        confidence["skills"] = 0.50

      if recruiter["current_company"]:
        confidence["current_company"] = 0.80
      else:
        confidence["current_company"] = 0.50

      if recruiter["title"]:
        confidence["title"] = 0.80
      else:
        confidence["title"] = 0.50

      overall = round(
        sum(confidence.values()) / len(confidence),
        2
      )

      candidate_profile["confidence"] = confidence

      candidate_profile["overall_confidence"] = overall

      return candidate_profile