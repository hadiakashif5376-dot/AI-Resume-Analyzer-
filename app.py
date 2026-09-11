import streamlit as st
from resume_parser import extract_resume_text, validate_resume
from analyzer import analyze_resume

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")

st.title("📄 AI Resume Analyzer")
st.write("Compare your resume with a job description using AI.")

resume_file = st.file_uploader("Upload your resume", type=["pdf", "docx"])
job_description = st.text_area("Paste the job description", height=260)

if st.button("Analyze Resume", type="primary"):
    if resume_file is None:
        st.error("Please upload a PDF or DOCX resume.")
        st.stop()

    if not job_description.strip():
        st.error("Please paste a job description.")
        st.stop()

    try:
        validate_resume(resume_file)
        with st.spinner("Reading your resume..."):
            resume_text = extract_resume_text(resume_file)

        if not resume_text.strip():
            st.error("No readable text was found in the resume.")
            st.stop()

        with st.spinner("Analyzing your resume..."):
            result = analyze_resume(resume_text, job_description.strip())

        st.success("Analysis complete!")

        col1, col2 = st.columns([1, 2])
        with col1:
            st.metric("Match Score", f"{result['overall_score']}/100")
        with col2:
            st.subheader("Final Result")
            st.write(result["final_result"])

        st.subheader("🎯 Matching Skills")
        st.write(", ".join(result["matching_skills"]) or "None identified.")

        st.subheader("❌ Missing or Not Clearly Demonstrated")
        st.write(", ".join(result["missing_skills"]) or "None identified.")

        st.subheader("🔑 ATS Keywords")
        st.write(", ".join(result["ats_keywords"]) or "None identified.")

        st.subheader("⚠️ Resume Problems")
        for item in result["problems"]:
            st.write(f"- {item}")

        st.subheader("💡 Recommendations")
        for item in result["recommendations"]:
            st.write(f"- {item}")

    except Exception as exc:
        st.error(f"Analysis failed: {exc}")
