import re
from difflib import SequenceMatcher

def extract_skills_from_jd(text):
    """
    Job Description se skills extract karein
    
    Args:
        text: Job Description text
    
    Returns:
        list: List of skills found in JD
    """
    # Common tech skills ki list
    skill_keywords = [
        # Programming Languages
        'python', 'java', 'c++', 'c#', 'javascript', 'typescript', 'ruby', 'go', 'rust',
        'php', 'swift', 'kotlin', 'scala', 'r', 'sql', 'html', 'css', 'c',
        'perl', 'lua', 'dart', 'elixir', 'erlang', 'haskell',
        
        # Frameworks & Libraries
        'react', 'angular', 'vue', 'node.js', 'nodejs', 'django', 'flask', 'spring',
        'tensorflow', 'pytorch', 'scikit-learn', 'pandas', 'numpy',
        'matplotlib', 'seaborn', 'plotly', 'opencv', 'nltk', 'scipy',
        'keras', 'fastapi', 'bootstrap', 'jquery', 'express',
        'hibernate', 'struts', 'play', 'rails',
        
        # Databases
        'mysql', 'postgresql', 'mongodb', 'redis', 'elasticsearch',
        'cassandra', 'dynamodb', 'sqlite', 'oracle', 'mssql',
        'db2', 'firebase', 'couchdb', 'neo4j',
        
        # Cloud & DevOps
        'aws', 'azure', 'gcp', 'google cloud', 'docker', 'kubernetes', 'jenkins',
        'git', 'github', 'gitlab', 'ci/cd', 'terraform', 'ansible',
        'puppet', 'chef', 'prometheus', 'grafana', 'elk',
        
        # Machine Learning & AI
        'machine learning', 'deep learning', 'nlp', 'computer vision',
        'data science', 'artificial intelligence', 'ai', 'ml',
        'data analysis', 'data visualization', 'statistics',
        'neural networks', 'llm', 'rag', 'gpt',
        'data mining', 'big data', 'hadoop', 'spark',
        
        # Tools
        'tableau', 'power bi', 'excel', 'spss', 'matlab',
        'jupyter', 'pycharm', 'vscode', 'postman', 'figma',
        'photoshop', 'illustrator', 'autocad', 'solidworks',
        'unity', 'unreal', 'blender',
        
        # Concepts
        'agile', 'scrum', 'devops', 'microservices', 'rest api',
        'graphql', 'websocket', 'oauth', 'jwt', 'cloud computing',
        'tdd', 'bdd', 'design patterns', 'solid', 'clean code',
        'data structures', 'algorithms', 'oop'
    ]
    
    text_lower = text.lower()
    found_skills = []
    
    for skill in skill_keywords:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
            found_skills.append(skill.title())
    
    return sorted(list(set(found_skills)))

def calculate_match_score(resume_skills, jd_skills):
    """
    Resume skills aur JD skills ke beech match score calculate karein
    
    Args:
        resume_skills: List of skills from resume
        jd_skills: List of skills from job description
    
    Returns:
        dict: Match score and details
    """
    # Normalize skills (lowercase)
    resume_skills_lower = [s.lower() for s in resume_skills]
    jd_skills_lower = [s.lower() for s in jd_skills]
    
    # Common skills find karein
    matched_skills = []
    matched_skills_lower = []
    
    for skill in resume_skills_lower:
        for jd_skill in jd_skills_lower:
            if skill == jd_skill or skill in jd_skill or jd_skill in skill:
                matched_skills.append(skill.title())
                matched_skills_lower.append(skill)
                break
    
    # Missing skills (JD mein hain but resume mein nahi)
    missing_skills_lower = [s for s in jd_skills_lower if s not in matched_skills_lower]
    missing_skills = [s.title() for s in missing_skills_lower]
    
    # Score calculate karein
    if len(jd_skills) > 0:
        score = (len(matched_skills) / len(jd_skills)) * 100
        score = round(score, 1)
    else:
        score = 0
    
    # Recommendation message
    if score >= 80:
        message = "🌟 Excellent match! You're a strong candidate for this role."
    elif score >= 60:
        message = "👏 Good match! Consider upskilling in missing areas."
    elif score >= 40:
        message = "📚 Fair match. Focus on learning the missing skills."
    else:
        message = "💪 Need significant skill development. Check the missing skills list."
    
    return {
        'score': score,
        'matched_skills': matched_skills,
        'missing_skills': missing_skills,
        'total_jd_skills': len(jd_skills),
        'total_resume_skills': len(resume_skills),
        'message': message
    }

def generate_learning_recommendations(missing_skills):
    """
    Missing skills ke hisaab se learning recommendations generate karein
    
    Args:
        missing_skills: List of missing skills
    
    Returns:
        str: Learning recommendations
    """
    if not missing_skills:
        return "🎉 You have all the required skills! You're ready for this role."
    
    recommendations = "📚 **Learning Recommendations:**\n\n"
    
    # Course suggestions
    course_suggestions = {
        'python': 'Python for Everybody (Coursera)',
        'java': 'Java Programming Masterclass (Udemy)',
        'javascript': 'The Complete JavaScript Course (Udemy)',
        'react': 'React - The Complete Guide (Udemy)',
        'angular': 'Angular - The Complete Guide (Udemy)',
        'django': 'Django for Beginners (Django Project)',
        'flask': 'Flask Mega-Tutorial (Miguel Grinberg)',
        'tensorflow': 'TensorFlow Developer Certificate (Coursera)',
        'pytorch': 'PyTorch for Deep Learning (Coursera)',
        'aws': 'AWS Certified Developer (AWS Training)',
        'docker': 'Docker Mastery (Udemy)',
        'kubernetes': 'Kubernetes for Beginners (KodeKloud)',
        'sql': 'SQL for Data Science (Coursera)',
        'mongodb': 'MongoDB University (Free Course)',
        'git': 'Git and GitHub Masterclass (Udemy)',
        'machine learning': 'Machine Learning A-Z (Udemy)',
        'deep learning': 'Deep Learning Specialization (Coursera)',
        'data science': 'Data Science Professional Certificate (IBM)',
        'excel': 'Excel Skills for Business (Coursera)',
        'tableau': 'Tableau Data Visualization (Tableau Training)',
        'power bi': 'Power BI Skills (Microsoft Learn)',
        'agile': 'Agile Project Management (Coursera)'
    }
    
    for skill in missing_skills[:5]:
        skill_lower = skill.lower()
        if skill_lower in course_suggestions:
            recommendations += f"• **{skill}**: {course_suggestions[skill_lower]}\n"
        else:
            recommendations += f"• **{skill}**: Learn through YouTube tutorials and practice projects\n"
    
    if len(missing_skills) > 5:
        recommendations += f"\n• ... and {len(missing_skills) - 5} more skills to learn"
    
    return recommendations