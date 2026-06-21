import re


def extract_ats_score(text):

    match = re.search(
        r"ATS_SCORE:\s*(\d+)",
        text
    )

    if match:
        return int(match.group(1))

    return 0


def extract_match_percentage(text):

    match = re.search(
        r"MATCH_PERCENTAGE:\s*(\d+)",
        text
    )

    if match:
        return int(match.group(1))

    return 0


def extract_section(text, section_name):

    lines = text.splitlines()

    result = []

    capture = False

    for line in lines:

        if section_name in line:
            capture = True
            continue

        if capture:

            if line.strip() == "":
                continue

            if ":" in line and not line.startswith("-"):
                break

            result.append(line.strip())

    return result


def extract_strengths(text):
    return extract_section(text, "STRENGTHS")


def extract_missing_skills(text):
    return extract_section(text, "MISSING_SKILLS")