import streamlit as st
import matplotlib.pyplot as plt

from utils.resume_processor import build_vectorstore
from utils.job_analyser import analyze_resume_jd

from utils.parser import (
    extract_ats_score
)

from utils.skill_parser import (
    extract_missing_skills
)

from utils.video_recommender import VIDEOS


def show_resume_analyzer():

    st.title("📄 Resume Analyzer")

    col1, col2 = st.columns(2)

    with col1:
        resume = st.file_uploader(
            "Upload Resume",
            type=["pdf"]
        )

    with col2:
        jd = st.text_area(
            "Paste Job Description",
            height=300
        )

    analyze = st.button(
        "🚀 Analyze Resume"
    )

    if analyze:

        if resume is None:
            st.error("Please upload a resume.")
            return

        if not jd:
            st.error("Please paste a Job Description.")
            return

        with st.spinner("Analyzing Resume..."):

            # Save uploaded resume
            with open(
                "data/resume.pdf",
                "wb"
            ) as f:
                f.write(
                    resume.getbuffer()
                )

            # Build vector store
            vectorstore = build_vectorstore(
                "data/resume.pdf"
            )

            retriever = vectorstore.as_retriever()

            docs = retriever.invoke(
                "Summarize this resume"
            )

            resume_context = "\n".join(
                [
                    doc.page_content
                    for doc in docs
                ]
            )

            # Gemini Analysis
            result = analyze_resume_jd(
                resume_context,
                jd
            )

            # Save for Dashboard
            st.session_state[
                "analysis"
            ] = result

            st.session_state[
                "retriever"
            ] = retriever

            # ATS Score
            ats_score = extract_ats_score(
                result
            )

            # Missing Skills
            skills = extract_missing_skills(
                result
            )

            # -------------------------
            # ATS SCORE CARD
            # -------------------------

            st.subheader(
                "📊 ATS Score"
            )

            fig, ax = plt.subplots()

            ax.pie(
                [
                    ats_score,
                    max(100 - ats_score, 0)
                ],
                labels=[
                    "ATS",
                    "Remaining"
                ],
                autopct="%1.1f%%"
            )

            ax.set_title(
                f"ATS Score: {ats_score}%"
            )

            st.pyplot(fig)

            # -------------------------
            # MISSING SKILLS
            # -------------------------

            st.subheader(
                "⚠ Missing Skills"
            )

            if skills:

                cols = st.columns(4)

                for i, skill in enumerate(
                    skills
                ):

                    cols[
                        i % 4
                    ].error(skill)

            else:

                st.success(
                    "No Missing Skills Found"
                )

            # -------------------------
            # LEARNING RESOURCES
            # -------------------------

            st.subheader(
                "🎥 Learning Resources"
            )

            found_video = False

            for skill in skills:

                if skill in VIDEOS:

                    found_video = True

                    st.markdown(
                        f"### {skill}"
                    )

                    st.video(
                        VIDEOS[skill]
                    )

            if not found_video:

                st.info(
                    "No learning videos available."
                )

            # -------------------------
            # FULL AI ANALYSIS
            # -------------------------

            st.subheader(
                "🤖 Complete AI Analysis"
            )

            st.write(result)