# import streamlit as st

# from utils.resume_processor import build_vectorstore
# from utils.job_analyser import analyze_resume_jd
# from utils.chat_engine import ask_resume_question

# # ==========================================
# # PAGE CONFIG
# # ==========================================

# st.set_page_config(
#     page_title="SkillGap AI",
#     page_icon="🚀",
#     layout="wide"
# )

# # ==========================================
# # CUSTOM CSS
# # ==========================================

# st.markdown("""
# <style>

# .main {
#     padding-top: 1rem;
# }

# .stButton button {
#     width: 100%;
#     height: 3rem;
#     font-size: 18px;
#     border-radius: 10px;
# }

# .metric-card {
#     background-color: #1e1e1e;
#     padding: 15px;
#     border-radius: 10px;
# }

# </style>
# """, unsafe_allow_html=True)

# # ==========================================
# # HEADER
# # ==========================================

# st.title("🚀 SkillGap AI")

# st.subheader(
#     "AI Powered Resume & Job Description Analyzer"
# )

# # ==========================================
# # HERO SECTION
# # ==========================================

# st.markdown("""
# ### 🎯 Get Instant Resume Insights

# Upload your Resume and Job Description.

# The system will provide:

# ✅ ATS Analysis

# ✅ Skill Match %

# ✅ Missing Skills

# ✅ Interview Questions

# ✅ Learning Roadmap

# ✅ Resume Chatbot
# """)

# # ==========================================
# # VIDEO SECTION
# # ==========================================

# with st.expander("🎥 How SkillGap AI Works"):

#     st.video(
#         "https://www.youtube.com/watch?v=aircAruvnKk"
#     )

# # ==========================================
# # INPUT SECTION
# # ==========================================

# col1, col2 = st.columns(2)

# with col1:

#     st.header("📄 Upload Resume")

#     resume = st.file_uploader(
#         "Choose Resume PDF",
#         type=["pdf"]
#     )

# with col2:

#     st.header("📝 Job Description")

#     jd = st.text_area(
#         "Paste Job Description Here",
#         height=300
#     )

# # ==========================================
# # ANALYZE BUTTON
# # ==========================================

# analyze = st.button(
#     "🚀 Analyze Resume"
# )

# # ==========================================
# # ANALYSIS
# # ==========================================

# if analyze:

#     if resume is None:

#         st.error(
#             "Please upload a resume."
#         )

#     elif not jd:

#         st.error(
#             "Please paste a Job Description."
#         )

#     else:

#         with st.spinner(
#             "Analyzing Resume..."
#         ):

#             # Save uploaded resume

#             with open(
#                 "data/resume.pdf",
#                 "wb"
#             ) as f:

#                 f.write(
#                     resume.getbuffer()
#                 )

#             # Build FAISS

#             vectorstore = build_vectorstore(
#                 "data/resume.pdf"
#             )

#             retriever = vectorstore.as_retriever()

#             # Save retriever for chatbot

#             st.session_state["retriever"] = retriever

#             # Get Resume Context

#             docs = retriever.invoke(
#                 "Summarize this resume"
#             )

#             resume_context = "\n".join(
#                 [doc.page_content for doc in docs]
#             )

#             # Gemini Analysis

#             analysis = analyze_resume_jd(
#                 resume_context,
#                 jd
#             )

#             # Save analysis

#             st.session_state["analysis"] = analysis

#         st.success(
#             "Analysis Completed Successfully!"
#         )

# # ==========================================
# # RESULTS
# # ==========================================

# if "analysis" in st.session_state:

#     st.divider()

#     st.header("📊 Analysis Result")

#     col1, col2, col3 = st.columns(3)

#     col1.metric(
#         "ATS Score",
#         "AI Generated"
#     )

#     col2.metric(
#         "Skill Match",
#         "AI Generated"
#     )

#     col3.metric(
#         "Missing Skills",
#         "AI Generated"
#     )

#     st.markdown(
#         st.session_state["analysis"]
#     )

# # ==========================================
# # TABS
# # ==========================================

# tab1, tab2, tab3, tab4 = st.tabs(
#     [
#         "🎯 Strengths",
#         "⚠ Missing Skills",
#         "🎤 Interview Questions",
#         "🛣 Learning Roadmap"
#     ]
# )

# with tab1:

#     st.info(
#         "Strengths will appear here from Gemini Analysis."
#     )

# with tab2:

#     st.warning(
#         "Missing Skills will appear here."
#     )

# with tab3:

#     st.success(
#         "Interview Questions will appear here."
#     )

# with tab4:

#     st.write(
#         "Learning Roadmap will appear here."
#     )

# # ==========================================
# # CHATBOT
# # ==========================================

# st.divider()

# st.header(
#     "💬 Chat With Resume"
# )

# question = st.text_input(
#     "Ask anything about the uploaded resume"
# )

# if question:

#     if "retriever" not in st.session_state:

#         st.warning(
#             "Please Analyze Resume first."
#         )

#     else:

#         with st.spinner(
#             "Thinking..."
#         ):

#             answer = ask_resume_question(
#                 st.session_state["retriever"],
#                 question
#             )

#             st.write(answer)

# # ==========================================
# # FOOTER
# # ==========================================

# st.divider()

# st.caption(
#     "🚀 Built with Streamlit + LangChain + FAISS + Gemini"
# )
import streamlit as st

from _pages.dashboard import show_dashboard
from _pages.resume_analzer import show_resume_analyzer
from _pages.ai_chat import show_chat #we have changed the folder pages name to _pages because streamlit automatically cretses the sidebar of the file inside pages folder 
def load_css():

    with open(
        "assets/styles.css"
    ) as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
st.set_page_config(
    page_title="SkillGap AI",
    page_icon="🚀",
    layout="wide"
)
load_css()

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.title("🚀 SkillGap AI")

    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "📄 Resume Analyzer",
            "🤖 AI Chat"
        ]
    )

    st.markdown("---")

    st.info(
        "AI Powered Career Copilot"
    )

# ==========================================
# ROUTING
# ==========================================

if page == "🏠 Dashboard":
    show_dashboard()

elif page == "📄 Resume Analyzer":
    show_resume_analyzer()

elif page == "🤖 AI Chat":
    show_chat()