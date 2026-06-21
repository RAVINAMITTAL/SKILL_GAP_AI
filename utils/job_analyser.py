from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)


def analyze_resume_jd(
    resume_context,
    job_description
):

    prompt = f"""
You are an expert ATS Resume Analyzer.

Analyze the Resume against the Job Description.

Return ONLY in the following format.

ATS_SCORE:
MATCH_PERCENTAGE:

STRENGTHS:
- point

MISSING_SKILLS:
- point

INTERVIEW_QUESTIONS:
1.
2.
3.

LEARNING_ROADMAP:
Week 1:
Week 2:
Week 3:

Resume:
{resume_context}

Job Description:
{job_description}
"""

    response = llm.invoke(prompt)

    return response.content