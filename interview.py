import random

# Technical Questions (Category wise)
technical_questions = {
    "Python": [
        "What is the difference between a list and a tuple in Python?",
        "Explain the concept of decorators in Python.",
        "What is the difference between '==' and 'is' in Python?",
        "Explain list comprehension with an example.",
        "What is a generator in Python and how is it different from a list?",
        "Explain the concept of OOP in Python.",
        "What are lambda functions in Python?"
    ],
    "Machine Learning": [
        "Explain the difference between supervised and unsupervised learning.",
        "What is overfitting and how can you prevent it?",
        "Explain the bias-variance tradeoff.",
        "What is cross-validation and why is it important?",
        "Explain the working of a decision tree algorithm.",
        "What is the difference between classification and regression?"
    ],
    "SQL": [
        "What is the difference between INNER JOIN and LEFT JOIN?",
        "Explain the difference between WHERE and HAVING clause.",
        "What is a primary key and foreign key?",
        "Explain the concept of normalization.",
        "What are indexes and how do they improve performance?",
        "What is the difference between DELETE and TRUNCATE?"
    ],
    "Data Science": [
        "Explain the steps in a typical data science project.",
        "What is EDA (Exploratory Data Analysis)?",
        "Explain the difference between correlation and causation.",
        "What is feature engineering?",
        "What is the difference between L1 and L2 regularization?"
    ],
    "General": [
        "Explain the difference between a function and a method.",
        "What is version control and why is it important?",
        "Explain the concept of API.",
        "What is the difference between a stack and a queue?"
    ]
}

# HR Questions
hr_questions = [
    "Tell me about yourself.",
    "What are your strengths and weaknesses?",
    "Why do you want to work at this company?",
    "Where do you see yourself in 5 years?",
    "Describe a challenge you faced and how you overcame it.",
    "Why should we hire you?",
    "Describe a time you worked in a team.",
    "How do you handle stress and pressure?",
    "What is your greatest achievement?",
    "What did you learn from a failure?"
]

def get_random_question(category="Any"):
    """Random question return karein based on category"""
    if category in technical_questions:
        return random.choice(technical_questions[category])
    else:
        # All technical questions mix
        all_questions = []
        for q_list in technical_questions.values():
            all_questions.extend(q_list)
        return random.choice(all_questions)

def get_hr_question():
    """Random HR question return karein"""
    return random.choice(hr_questions)

def evaluate_answer(question, answer):
    """Basic answer evaluation (rule-based)"""
    if not answer or len(answer) < 10:
        return {
            'score': 2,
            'feedback': "⚠️ Answer too short. Please write a detailed answer.",
            'improvements': "Add more details and examples."
        }
    
    # Keywords check
    keywords = question.lower().split()
    answer_lower = answer.lower()
    
    # Count matching words
    matching_words = sum(1 for word in keywords if word in answer_lower)
    word_ratio = len(answer.split())
    
    # Score calculation
    if word_ratio < 20:
        score = 4
        feedback = "📝 Good start! Add more explanation."
        improvements = "Expand your answer with examples and details."
    elif word_ratio < 40:
        score = 6
        feedback = "👍 Good answer! You covered the main points."
        improvements = "Try adding more technical depth."
    elif word_ratio < 60:
        score = 8
        feedback = "🌟 Great answer! Very detailed and well-structured."
        improvements = "Add real-world examples if possible."
    else:
        score = 9
        feedback = "🎉 Excellent answer! Very thorough and detailed."
        improvements = "Consider adding more practical examples."
    
    # Bonus for keywords
    if matching_words > 3:
        score = min(10, score + 1)
    
    return {
        'score': min(10, score),
        'feedback': feedback,
        'improvements': improvements
    }

def get_interview_categories():
    """Available interview categories return karein"""
    return list(technical_questions.keys()) + ["HR Questions"]