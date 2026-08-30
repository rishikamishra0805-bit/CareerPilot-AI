import streamlit as st
from utils.pdf_parser import extract_text_from_pdf, extract_skills_from_text, generate_resume_feedback
from modules.job_matcher import extract_skills_from_jd, calculate_match_score, generate_learning_recommendations
from modules.interview import (
    get_random_question, get_hr_question, 
    evaluate_answer, get_interview_categories
)
from modules.roadmap import generate_roadmap, get_career_paths, get_recommended_path

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

# Session state init
if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"
if "resume_skills" not in st.session_state:
    st.session_state.resume_skills = []
if "current_question" not in st.session_state:
    st.session_state.current_question = ""
if "question_type" not in st.session_state:
    st.session_state.question_type = ""
if "answer_submitted" not in st.session_state:
    st.session_state.answer_submitted = False
if "result" not in st.session_state:
    st.session_state.result = None

# Sidebar navigation
st.sidebar.title("🚀 CareerPilot AI")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Select Feature",
    ["🏠 Home", "📄 Resume Analysis", "🎯 Job Match", "💬 AI Interview", "🗺️ Career Roadmap"]
)
st.session_state.page = page

st.sidebar.markdown("---")
st.sidebar.caption("Made with ❤️ for Career Growth")

# ============ HOME ============
if page == "🏠 Home":
    st.title("🚀 CareerPilot AI")
    st.subheader("Your AI-Powered Career & Placement Copilot")
    st.markdown("---")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("📄 Resume Analysis", use_container_width=True):
            st.session_state.page = "📄 Resume Analysis"
            st.rerun()
    with col2:
        if st.button("🎯 Job Match", use_container_width=True):
            st.session_state.page = "🎯 Job Match"
            st.rerun()
    with col3:
        if st.button("💬 AI Interview", use_container_width=True):
            st.session_state.page = "💬 AI Interview"
            st.rerun()
    with col4:
        if st.button("🗺️ Career Roadmap", use_container_width=True):
            st.session_state.page = "🗺️ Career Roadmap"
            st.rerun()
    
    st.markdown("---")
    st.info("💡 Select a feature from the sidebar to get started!")

# ============ RESUME ANALYSIS ============
elif page == "📄 Resume Analysis":
    st.title("📄 Resume Analysis")
    st.markdown("Upload your resume (PDF) and get AI-powered feedback")
    st.markdown("---")
    
    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=['pdf'],
        help="Upload your resume in PDF format"
    )
    
    if uploaded_file is not None:
        with st.spinner("Analyzing your resume..."):
            try:
                text = extract_text_from_pdf(uploaded_file)
                skills = extract_skills_from_text(text)
                
                if len(skills) == 0 or len(text) < 200:
                    st.warning("⚠️ Automatic extraction failed. Enter skills manually.")
                    
                    st.subheader("✏️ Enter your skills")
                    skills_text = st.text_area(
                        "Skills (one per line or comma separated)",
                        value="Python\nMachine Learning\nSQL\nFlask\nTensorFlow\nPandas\nNumPy",
                        height=150
                    )
                    
                    if st.button("🔍 Analyze Manually", type="primary"):
                        if ',' in skills_text:
                            skills = [s.strip() for s in skills_text.split(',') if s.strip()]
                        else:
                            skills = [s.strip() for s in skills_text.split('\n') if s.strip()]
                        
                        if skills:
                            st.session_state.resume_skills = skills
                            feedback = generate_resume_feedback(skills)
                            st.success("✅ Manual analysis complete!")
                            
                            col1, col2 = st.columns(2)
                            with col1:
                                st.subheader("📊 Your Skills")
                                for skill in skills:
                                    st.write(f"• {skill}")
                            with col2:
                                st.subheader("💡 Feedback")
                                st.write(feedback)
                else:
                    st.session_state.resume_skills = skills
                    feedback = generate_resume_feedback(skills)
                    st.success("✅ Resume analyzed successfully!")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.subheader("📊 Extracted Skills")
                        for skill in skills:
                            st.write(f"• {skill}")
                    with col2:
                        st.subheader("💡 Feedback")
                        st.write(feedback)
                    
                    with st.expander("📄 View Extracted Text"):
                        st.text(text[:1000] + "..." if len(text) > 1000 else text)
                    
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.info("Try manual mode below:")
                
                skills_text = st.text_area(
                    "Enter your skills (comma separated)",
                    value="Python, Machine Learning, SQL, Flask",
                    height=100
                )
                if st.button("Analyze Manually"):
                    skills = [s.strip() for s in skills_text.split(',') if s.strip()]
                    if skills:
                        st.session_state.resume_skills = skills
                        feedback = generate_resume_feedback(skills)
                        st.success("✅ Analysis complete!")
                        for skill in skills:
                            st.write(f"• {skill}")
                        st.write(feedback)
    else:
        st.info("👆 Upload your resume PDF to get started")

# ============ JOB MATCH ============
elif page == "🎯 Job Match":
    st.title("🎯 Job Description Matching")
    st.markdown("Upload resume and paste job description to check compatibility")
    st.markdown("---")
    
    if st.session_state.resume_skills:
        st.success(f"✅ {len(st.session_state.resume_skills)} skills loaded")
        with st.expander("View skills"):
            for skill in st.session_state.resume_skills[:10]:
                st.write(f"• {skill}")
    else:
        st.warning("⚠️ No skills found. First analyze your resume in 'Resume Analysis' tab.")
    
    st.markdown("---")
    st.subheader("📝 Job Description")
    
    jd_text = st.text_area(
        "Paste Job Description here",
        height=200,
        placeholder="Paste the complete job description from LinkedIn, company website, etc."
    )
    
    if st.button("🚀 Analyze Match", type="primary"):
        if not st.session_state.resume_skills:
            st.warning("⚠️ Please analyze your resume first in the Resume Analysis tab")
        elif not jd_text:
            st.warning("⚠️ Please paste a job description")
        else:
            with st.spinner("Analyzing match..."):
                try:
                    jd_skills = extract_skills_from_jd(jd_text)
                    result = calculate_match_score(st.session_state.resume_skills, jd_skills)
                    
                    st.success("✅ Match analysis complete!")
                    st.markdown("---")
                    
                    col1, col2, col3 = st.columns([1, 2, 1])
                    with col2:
                        st.metric("🎯 Match Score", f"{result['score']}%")
                        st.progress(result['score'] / 100)
                    
                    st.markdown("---")
                    st.info(result['message'])
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.subheader("✅ Matched Skills")
                        if result['matched_skills']:
                            for skill in result['matched_skills'][:10]:
                                st.success(f"✓ {skill}")
                        else:
                            st.warning("No matching skills found")
                    
                    with col2:
                        st.subheader("❌ Missing Skills")
                        if result['missing_skills']:
                            for skill in result['missing_skills'][:10]:
                                st.error(f"✗ {skill}")
                            if len(result['missing_skills']) > 10:
                                st.caption(f"and {len(result['missing_skills']) - 10} more...")
                        else:
                            st.success("🎉 No missing skills!")
                    
                    if result['missing_skills']:
                        st.markdown("---")
                        st.subheader("📚 Learning Recommendations")
                        rec = generate_learning_recommendations(result['missing_skills'])
                        st.markdown(rec)
                    
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

# ============ AI INTERVIEW ============
elif page == "💬 AI Interview":
    st.title("💬 AI Interview Practice")
    st.markdown("Practice technical and HR interview questions")
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        question_type = st.selectbox(
            "Select question category",
            ["Technical"] + get_interview_categories(),
            help="Choose the type of interview questions"
        )
    
    with col2:
        if st.button("🎯 New Question", type="primary"):
            if question_type == "HR Questions":
                st.session_state.current_question = get_hr_question()
                st.session_state.question_type = "HR"
            else:
                category = question_type if question_type != "Technical" else "Any"
                st.session_state.current_question = get_random_question(category)
                st.session_state.question_type = "Technical"
            st.session_state.answer_submitted = False
            st.session_state.result = None
    
    if st.session_state.current_question:
        st.markdown("---")
        st.subheader(f"📝 {st.session_state.question_type} Question")
        st.info(f"**{st.session_state.current_question}**")
        
        answer = st.text_area(
            "Write your answer here",
            height=200,
            placeholder="Type your answer in detail...",
            key="interview_answer"
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📤 Submit Answer", type="primary"):
                if answer and len(answer) > 10:
                    st.session_state.result = evaluate_answer(
                        st.session_state.current_question, 
                        answer
                    )
                    st.session_state.answer_submitted = True
                else:
                    st.warning("⚠️ Please write a detailed answer (minimum 10 characters)")
        
        with col2:
            if st.button("🔄 Skip Question"):
                st.session_state.current_question = ""
                st.session_state.answer_submitted = False
                st.session_state.result = None
                st.rerun()
        
        if st.session_state.answer_submitted and st.session_state.result:
            st.markdown("---")
            st.subheader("📊 Evaluation")
            
            result = st.session_state.result
            
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                st.metric("🎯 Score", f"{result['score']}/10")
            
            st.info(f"**Feedback:** {result['feedback']}")
            st.success(f"**💡 Suggestions for improvement:** {result['improvements']}")
    
    else:
        st.info("👆 Click 'New Question' to start your interview practice!")
    
    with st.expander("💡 Interview Tips"):
        st.markdown("""
        **How to write a good answer:**
        1. Be specific - Use examples from your experience
        2. Explain concepts clearly - Show your understanding
        3. Use proper terminology - Demonstrate technical knowledge
        4. Structure your answer - Introduction, body, conclusion
        5. Be concise - Keep it focused and to the point
        """)

# ============ CAREER ROADMAP ============
elif page == "🗺️ Career Roadmap":
    st.title("🗺️ Career Roadmap")
    st.markdown("Get personalized learning roadmap based on your skills")
    st.markdown("---")
    
    if not st.session_state.resume_skills:
        st.warning("⚠️ No skills found. Please analyze your resume first in 'Resume Analysis' tab.")
        st.info("💡 Go to Resume Analysis, upload your PDF or enter skills manually.")
    else:
        st.subheader("📋 Your Current Skills")
        for skill in st.session_state.resume_skills:
            st.write(f"• {skill}")
        
        st.markdown("---")
        
        st.subheader("🎯 Select Target Career")
        col1, col2 = st.columns([2, 1])
        
        with col1:
            career_path = st.selectbox(
                "Choose your target career path:",
                get_career_paths()
            )
        
        with col2:
            recommended = get_recommended_path(st.session_state.resume_skills)
            if recommended:
                st.info(f"💡 Recommended: **{recommended}**")
        
        if st.button("🚀 Generate Roadmap", type="primary"):
            with st.spinner("Generating personalized roadmap..."):
                result = generate_roadmap(st.session_state.resume_skills, career_path)
                
                st.success("✅ Roadmap generated!")
                st.markdown("---")
                
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    st.metric("📊 Skills Match", f"{result['progress']}%")
                    st.progress(result['progress'] / 100)
                    st.info(result['status'])
                
                st.markdown("---")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("✅ Skills You Have")
                    if result['matched_skills']:
                        for skill in result['matched_skills'][:10]:
                            st.success(f"✓ {skill}")
                    else:
                        st.warning("No matching skills found")
                    st.caption(f"{len(result['matched_skills'])} skills matched")
                
                with col2:
                    st.subheader("📚 Skills to Learn")
                    if result['missing_skills']:
                        for skill in result['missing_skills'][:10]:
                            st.error(f"✗ {skill}")
                        if len(result['missing_skills']) > 10:
                            st.caption(f"and {len(result['missing_skills']) - 10} more...")
                    else:
                        st.success("🎉 You have all required skills!")
                    st.caption(f"{len(result['missing_skills'])} skills to learn")
                
                st.markdown("---")
                st.subheader("🗺️ Learning Roadmap")
                st.caption(f"Step-by-step roadmap for {result['target']}")
                st.markdown("---")
                
                for step in result['roadmap']:
                    st.markdown(f"{step}")
                    st.markdown("---")
                
                if result['missing_skills']:
                    st.subheader("📚 Recommended Learning Resources")
                    st.markdown("""
                    **Beginner:** YouTube tutorials, Coursera/edX, W3Schools
                    **Intermediate:** Udemy courses, Kaggle, LeetCode
                    **Advanced:** Hands-on projects, Open source, Certifications
                    """)
    
    with st.expander("💡 Career Tips"):
        st.markdown("""
        **How to use this roadmap:**
        1. Start with the first step and practice daily
        2. Build projects as you learn
        3. Practice coding on platforms like LeetCode
        4. Network with professionals in your target field
        5. Update your skills regularly
        """)