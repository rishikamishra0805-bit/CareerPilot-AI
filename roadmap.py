# Career paths mapping based on skills
career_paths = {
    "Data Scientist": {
        "required_skills": [
            "Python", "Machine Learning", "SQL", "Data Science", 
            "Statistics", "Pandas", "NumPy", "Scikit-learn", 
            "Deep Learning", "NLP", "Data Visualization"
        ],
        "roadmap": [
            "1. Master Python Programming",
            "2. Learn Data Structures & Algorithms",
            "3. Master SQL for Data Analysis",
            "4. Learn Statistics & Probability",
            "5. Master Pandas & NumPy",
            "6. Learn Data Visualization (Matplotlib, Seaborn, Tableau)",
            "7. Master Machine Learning (Scikit-learn)",
            "8. Learn Deep Learning (TensorFlow/PyTorch)",
            "9. Learn NLP or Computer Vision",
            "10. Build a Portfolio of Projects",
            "11. Learn Deployment (Docker, AWS)",
            "12. Prepare for Interviews"
        ]
    },
    "Data Analyst": {
        "required_skills": [
            "Python", "SQL", "Data Analysis", "Excel", 
            "Statistics", "Data Visualization", "Pandas", 
            "Power BI", "Tableau"
        ],
        "roadmap": [
            "1. Learn Python Fundamentals",
            "2. Master SQL Queries",
            "3. Learn Statistics & Probability",
            "4. Master Excel Advanced Features",
            "5. Learn Data Cleaning with Pandas",
            "6. Learn Data Visualization",
            "7. Master Power BI or Tableau",
            "8. Learn Dashboard Creation",
            "9. Build Portfolio Projects",
            "10. Prepare for Interviews"
        ]
    },
    "Software Engineer": {
        "required_skills": [
            "Python", "Java", "SQL", "JavaScript", 
            "HTML", "CSS", "React", "Node.js", 
            "Git", "Docker", "AWS"
        ],
        "roadmap": [
            "1. Master Programming Fundamentals",
            "2. Learn Data Structures & Algorithms",
            "3. Master Git & GitHub",
            "4. Learn Frontend (HTML, CSS, JavaScript)",
            "5. Learn a Frontend Framework (React/Angular)",
            "6. Learn Backend (Python/Java + SQL)",
            "7. Learn REST APIs & GraphQL",
            "8. Learn Docker & Containerization",
            "9. Learn Cloud (AWS/Azure/GCP)",
            "10. Build Full-Stack Projects",
            "11. Learn CI/CD",
            "12. Prepare for Interviews"
        ]
    },
    "Machine Learning Engineer": {
        "required_skills": [
            "Python", "Machine Learning", "SQL", "Deep Learning", 
            "TensorFlow", "PyTorch", "Docker", "AWS", 
            "Data Science", "Git", "MLOps"
        ],
        "roadmap": [
            "1. Master Python & OOP",
            "2. Learn Data Structures & Algorithms",
            "3. Master SQL",
            "4. Learn Mathematics (Linear Algebra, Calculus)",
            "5. Master Machine Learning (Scikit-learn)",
            "6. Learn Deep Learning (TensorFlow/PyTorch)",
            "7. Learn MLOps (Docker, Kubernetes)",
            "8. Learn Cloud Deployment (AWS)",
            "9. Build ML Projects",
            "10. Contribute to Open Source",
            "11. Prepare for Interviews"
        ]
    }
}

# Default career path suggestions
default_careers = ["Data Scientist", "Data Analyst", "Software Engineer", "Machine Learning Engineer"]

def generate_roadmap(skills, career_path="Data Scientist"):
    """
    Skills ke hisaab se personalized roadmap generate karein
    
    Args:
        skills: List of current skills
        career_path: Target career path
    
    Returns:
        dict: Roadmap with skills analysis and recommendations
    """
    if career_path not in career_paths:
        career_path = "Data Scientist"  # Default
    
    target_skills = career_paths[career_path]["required_skills"]
    roadmap_steps = career_paths[career_path]["roadmap"]
    
    # Normalize skills
    skills_lower = [s.lower() for s in skills]
    target_skills_lower = [s.lower() for s in target_skills]
    
    # Match and missing skills
    matched_skills = []
    missing_skills = []
    
    for target in target_skills_lower:
        found = False
        for skill in skills_lower:
            if target in skill or skill in target:
                matched_skills.append(target.title())
                found = True
                break
        if not found:
            missing_skills.append(target.title())
    
    # Calculate progress
    if len(target_skills) > 0:
        progress = (len(matched_skills) / len(target_skills)) * 100
        progress = round(progress, 1)
    else:
        progress = 0
    
    # Skill assessment
    if progress >= 70:
        status = "🟢 Good Progress! You're on the right track."
    elif progress >= 40:
        status = "🟡 Moderate Progress. Focus on missing skills."
    else:
        status = "🔴 Focus on fundamentals. Start with the roadmap."
    
    return {
        "target": career_path,
        "target_skills": target_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "progress": progress,
        "status": status,
        "roadmap": roadmap_steps
    }

def get_career_paths():
    """Available career paths return karein"""
    return list(career_paths.keys())

def get_recommended_path(skills):
    """
    Skills ke hisaab se best career path recommend karein
    
    Args:
        skills: List of skills
    
    Returns:
        str: Recommended career path
    """
    best_match = None
    best_score = 0
    
    for career in career_paths:
        target_skills = career_paths[career]["required_skills"]
        matched = 0
        for skill in skills:
            for target in target_skills:
                if skill.lower() in target.lower() or target.lower() in skill.lower():
                    matched += 1
                    break
        
        if len(target_skills) > 0:
            score = (matched / len(target_skills)) * 100
            if score > best_score:
                best_score = score
                best_match = career
    
    return best_match