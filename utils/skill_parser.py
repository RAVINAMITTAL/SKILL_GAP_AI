def extract_missing_skills(
        text):

    skills = []

    capture = False

    for line in text.splitlines():

        if "MISSING_SKILLS" in line:

            capture = True

            continue

        if (
            "INTERVIEW_QUESTIONS"
            in line
        ):
            break

        if capture:

            if "-" in line:

                skills.append(
                    line.replace(
                        "-",
                        ""
                    ).strip()
                )

    return skills