import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_file):
    """
    PDF file se text extract karein
    
    Args:
        pdf_file: Uploaded PDF file object
    
    Returns:
        str: Extracted text from PDF
    """
    try:
        # PDF document open karein
        doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
        
        text = ""
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()
        
        doc.close()
        
        # Extra whitespace clean karein
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Agar text bahut chhota hai toh error throw karein
        if len(text) < 100:
            raise Exception("PDF me bahut kam text hai. Ho sakta hai yeh image-based PDF ho.")
        
        return text
        
    except Exception as e:
        raise Exception(f"PDF extraction failed: {str(e)}")

def extract_skills_from_text(text):
    """
    Text se skills extract karein (IMPROVED VERSION)
    
    Args:
        text: Extracted text from resume
    
    Returns:
        list: List of skills found
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
        'data structures', 'algorithms', 'oop',
        
        # Soft Skills (technical context mein)
        'communication', 'leadership', 'teamwork', 'problem solving',
        'critical thinking', 'project management', 'time management',
        'presentation', 'decision making', 'collaboration'
    ]
    
    text_lower = text.lower()
    found_skills = []
    
    for skill in skill_keywords:
        # Word boundary ke sath match karein
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
            found_skills.append(skill.title())
    
    # Duplicates hatao aur sort karo
    found_skills = sorted(list(set(found_skills)))
    
    return found_skills

def generate_resume_feedback(skills):
    """
    Skills ke hisaab se feedback generate karein
    
    Args:
        skills: List of skills found
    
    Returns:
        str: Feedback text
    """
    if len(skills) == 0:
        return """
⚠️ **No technical skills found in your resume.**

**Quick fixes:**
1. Add a dedicated **"Skills"** section with bullet points
2. Mention technologies used in each project
3. Use standard skill names (e.g., "Python" instead of "Python Programming")
4. Include both technical and soft skills
5. Be specific (e.g., "Machine Learning" vs "ML")
"""
    
    feedback = f"✅ **{len(skills)} skills identified** in your resume.\n\n"
    feedback += "**Skills Found:**\n"
    
    # Categorize skills
    tech_skills = []
    other_skills = []
    
    for skill in skills:
        if any(keyword in skill.lower() for keyword in ['python', 'java', 'sql', 'react', 'tensorflow', 'aws', 'docker']):
            tech_skills.append(skill)
        else:
            other_skills.append(skill)
    
    if tech_skills:
        feedback += "\n**🛠️ Technical Skills:**\n"
        for skill in tech_skills[:10]:
            feedback += f"• {skill}\n"
    
    if other_skills:
        feedback += "\n**📋 Other Skills:**\n"
        for skill in other_skills[:5]:
            feedback += f"• {skill}\n"
    
    if len(skills) > 15:
        feedback += f"\n• ... and {len(skills) - 15} more skills\n"
    
    feedback += "\n**💡 Suggestions to improve your resume:**\n"
    feedback += "• Add measurable achievements (e.g., 'Increased sales by 20%')\n"
    feedback += "• Include project details with technologies used\n"
    feedback += "• Highlight your most relevant skills first\n"
    feedback += "• Add certifications if you have any\n"
    feedback += "• Use action verbs (e.g., 'Developed', 'Implemented', 'Designed')"
    
    return feedback