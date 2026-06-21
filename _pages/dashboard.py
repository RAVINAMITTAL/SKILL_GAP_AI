import streamlit as st
import matplotlib.pyplot as plt

from utils.parser import (
    extract_ats_score,
    extract_match_percentage,
    extract_strengths,
    extract_missing_skills
)


def show_dashboard():

    st.title("🚀 SkillGap AI Dashboard")

    st.caption(
        "AI Powered Resume Analysis & Career Guidance"
    )

    # =====================================
    # CHECK ANALYSIS EXISTS
    # =====================================

    if "analysis" not in st.session_state:

        st.info(
            """
            Upload a resume and analyze it first.

            Dashboard will automatically
            generate ATS insights,
            skill gaps,
            job readiness,
            and recommendations.
            """
        )

        return

    analysis = st.session_state["analysis"]

    # =====================================
    # PARSE DATA
    # =====================================

    ats_score = extract_ats_score(
        analysis
    )

    match_percentage = extract_match_percentage(
        analysis
    )

    strengths = extract_strengths(
        analysis
    )

    missing_skills = extract_missing_skills(
        analysis
    )

    # =====================================
    # METRICS
    # =====================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "ATS Score",
            f"{ats_score}%"
        )

    with col2:

        st.metric(
            "Job Match",
            f"{match_percentage}%"
        )

    with col3:

        st.metric(
            "Strengths",
            len(strengths)
        )

    with col4:

        st.metric(
            "Missing Skills",
            len(missing_skills)
        )

    st.divider()

    # =====================================
    # ATS CHART
    # =====================================

    left, right = st.columns(2)

    with left:

        st.subheader(
            "📊 ATS Analysis"
        )

        fig, ax = plt.subplots()

        ax.pie(
            [
                ats_score,
                max(
                    100 - ats_score,
                    0
                )
            ],
            labels=[
                "ATS",
                "Remaining"
            ],
            autopct="%1.1f%%"
        )

        st.pyplot(fig)

    # =====================================
    # JOB MATCH
    # =====================================

    with right:

        st.subheader(
            "🎯 Job Readiness"
        )

        fig, ax = plt.subplots()

        ax.pie(
            [
                match_percentage,
                max(
                    100 - match_percentage,
                    0
                )
            ],
            labels=[
                "Matched",
                "Gap"
            ],
            autopct="%1.1f%%"
        )

        st.pyplot(fig)

    st.divider()

    # =====================================
    # STRENGTHS
    # =====================================

    st.subheader(
        "✅ Strengths"
    )

    if strengths:

        cols = st.columns(3)

        for i, skill in enumerate(
            strengths
        ):

            cols[
                i % 3
            ].success(skill)

    else:

        st.warning(
            "No strengths found"
        )

    st.divider()

    # =====================================
    # MISSING SKILLS
    # =====================================

    st.subheader(
        "⚠ Missing Skills"
    )

    if missing_skills:

        cols = st.columns(3)

        for i, skill in enumerate(
            missing_skills
        ):

            cols[
                i % 3
            ].error(skill)

    else:

        st.success(
            "No skill gaps detected"
        )

    st.divider()

    # =====================================
    # SKILL GAP CHART
    # =====================================

    if missing_skills:

        st.subheader(
            "📈 Skill Gap Analysis"
        )

        values = [
            1
            for _
            in missing_skills
        ]

        fig, ax = plt.subplots(
            figsize=(8, 4)
        )

        ax.barh(
            missing_skills,
            values
        )

        ax.set_title(
            "Missing Skills"
        )

        st.pyplot(fig)

    st.divider()

    # =====================================
    # AI INSIGHT
    # =====================================

    st.subheader(
        "🤖 AI Career Insight"
    )

    if ats_score >= 80:

        st.success(
            """
            Excellent profile.

            You are close to
            interview-ready status.
            """
        )

    elif ats_score >= 60:

        st.warning(
            """
            Good profile.

            Focus on missing skills
            to improve job readiness.
            """
        )

    else:

        st.error(
            """
            Significant improvement needed.

            Complete roadmap and
            strengthen core skills.
            """
        )