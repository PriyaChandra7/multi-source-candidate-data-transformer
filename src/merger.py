def merge_profiles(csv_data, resume_profile):
      candidate = {}
      recruiter = csv_data.iloc[0]
      candidate["candidate_id"] = "CAND001"

      candidate["full_name"] = (
        resume_profile["full_name"]
        if resume_profile["full_name"]
        else recruiter["name"]
      )

      candidate["emails"] = (
        resume_profile["emails"]
        if resume_profile["emails"]
        else [recruiter["email"]]
      )

      candidate["phones"] = (
        resume_profile["phones"]
        if resume_profile["phones"]
        else [str(recruiter["phone"])]
      )

      candidate["skills"] = resume_profile["skills"]

      candidate["current_company"] = recruiter["current_company"]

      candidate["title"] = recruiter["title"]


      candidate["provenance"] = [
          {"field": "full_name", "source": "Recruiter CSV"},
          {"field": "emails", "source": "Resume"},
          {"field": "phones", "source": "Resume"},
          {"field": "skills", "source": "Resume"},
          {"field": "current_company", "source": "Recruiter CSV"},
          {"field": "title", "source": "Recruiter CSV"}
      ]

      return candidate