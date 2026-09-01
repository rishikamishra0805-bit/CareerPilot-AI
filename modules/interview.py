import random
import re


# ============================================================
# TECHNICAL INTERVIEW QUESTIONS
# ============================================================

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


# ============================================================
# HR QUESTIONS
# ============================================================

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


# ============================================================
# EXPECTED CONCEPTS FOR TECHNICAL QUESTIONS
# ============================================================

question_evaluation = {

    # ---------------- PYTHON ----------------

    "What is the difference between a list and a tuple in Python?": {
        "keywords": [
            "mutable",
            "immutable",
            "list",
            "tuple"
        ],
        "answer": (
            "A list is mutable, meaning its elements can be changed after "
            "creation. A tuple is immutable, meaning its elements cannot be "
            "changed after creation. Lists use square brackets while tuples "
            "normally use parentheses."
        )
    },

    "Explain the concept of decorators in Python.": {
        "keywords": [
            "function",
            "wrapper",
            "modify",
            "behavior",
            "decorator"
        ],
        "answer": (
            "A decorator is a function that takes another function and "
            "extends or modifies its behavior without changing the original "
            "function's source code. It is commonly implemented using the "
            "@decorator syntax."
        )
    },

    "What is the difference between '==' and 'is' in Python?": {
        "keywords": [
            "equality",
            "identity",
            "value",
            "object",
            "memory"
        ],
        "answer": (
            "The == operator checks whether two objects have equal values, "
            "while the is operator checks whether two references point to "
            "the same object in memory."
        )
    },

    "Explain list comprehension with an example.": {
        "keywords": [
            "list",
            "expression",
            "loop",
            "iterable",
            "condition"
        ],
        "answer": (
            "List comprehension is a concise way to create a list from an "
            "iterable. It can contain an expression, a loop and optionally "
            "a condition. For example, [x * 2 for x in numbers]."
        )
    },

    "What is a generator in Python and how is it different from a list?": {
        "keywords": [
            "generator",
            "yield",
            "lazy",
            "memory",
            "list"
        ],
        "answer": (
            "A generator produces values lazily, usually using the yield "
            "keyword. It does not store all values in memory at once, so it "
            "can be more memory efficient than a list."
        )
    },

    "Explain the concept of OOP in Python.": {
        "keywords": [
            "object",
            "class",
            "encapsulation",
            "inheritance",
            "polymorphism"
        ],
        "answer": (
            "Object-oriented programming organizes software around classes "
            "and objects. Important concepts include encapsulation, "
            "inheritance, polymorphism and abstraction."
        )
    },

    "What are lambda functions in Python?": {
        "keywords": [
            "lambda",
            "anonymous",
            "function",
            "expression"
        ],
        "answer": (
            "A lambda function is a small anonymous function written as a "
            "single expression. It can accept arguments and return a value "
            "without defining a normal function using def."
        )
    },

    # ---------------- MACHINE LEARNING ----------------

    "Explain the difference between supervised and unsupervised learning.": {
        "keywords": [
            "supervised",
            "unsupervised",
            "labeled",
            "unlabeled",
            "classification",
            "clustering"
        ],
        "answer": (
            "Supervised learning uses labeled training data and learns to "
            "predict a target, such as classification or regression. "
            "Unsupervised learning uses unlabeled data to discover patterns, "
            "such as clusters."
        )
    },

    "What is overfitting and how can you prevent it?": {
        "keywords": [
            "overfitting",
            "training",
            "unseen",
            "generalization",
            "regularization",
            "cross-validation"
        ],
        "answer": (
            "Overfitting happens when a model learns the training data too "
            "closely and performs poorly on unseen data. It can be reduced "
            "using regularization, cross-validation, simpler models, "
            "more data or early stopping."
        )
    },

    "Explain the bias-variance tradeoff.": {
        "keywords": [
            "bias",
            "variance",
            "underfitting",
            "overfitting",
            "generalization"
        ],
        "answer": (
            "Bias represents error caused by overly simple assumptions and "
            "can lead to underfitting. Variance represents sensitivity to "
            "training data and can lead to overfitting. A good model balances "
            "bias and variance to generalize well."
        )
    },

    "What is cross-validation and why is it important?": {
        "keywords": [
            "cross-validation",
            "training",
            "validation",
            "fold",
            "model",
            "performance"
        ],
        "answer": (
            "Cross-validation evaluates a model by dividing the data into "
            "multiple folds. The model is trained on some folds and validated "
            "on another fold repeatedly. It provides a more reliable estimate "
            "of model performance."
        )
    },

    "Explain the working of a decision tree algorithm.": {
        "keywords": [
            "decision tree",
            "node",
            "split",
            "feature",
            "leaf",
            "prediction"
        ],
        "answer": (
            "A decision tree repeatedly splits data based on features to "
            "create groups with similar target values. Internal nodes "
            "represent decisions, branches represent outcomes and leaf nodes "
            "provide the final prediction."
        )
    },

    "What is the difference between classification and regression?": {
        "keywords": [
            "classification",
            "regression",
            "categorical",
            "continuous",
            "prediction"
        ],
        "answer": (
            "Classification predicts categorical classes, such as spam or "
            "not spam. Regression predicts continuous numerical values, "
            "such as salary or house price."
        )
    },

    # ---------------- SQL ----------------

    "What is the difference between INNER JOIN and LEFT JOIN?": {
        "keywords": [
            "inner join",
            "left join",
            "matching",
            "rows",
            "table"
        ],
        "answer": (
            "INNER JOIN returns only rows that have matching values in both "
            "tables. LEFT JOIN returns all rows from the left table and "
            "matching rows from the right table; unmatched right-side values "
            "are represented as NULL."
        )
    },

    "Explain the difference between WHERE and HAVING clause.": {
        "keywords": [
            "where",
            "having",
            "filter",
            "rows",
            "group",
            "aggregate"
        ],
        "answer": (
            "WHERE filters rows before grouping and aggregation. HAVING "
            "filters groups after GROUP BY and is commonly used with "
            "aggregate functions such as COUNT or SUM."
        )
    },

    "What is a primary key and foreign key?": {
        "keywords": [
            "primary key",
            "foreign key",
            "unique",
            "identify",
            "relationship",
            "table"
        ],
        "answer": (
            "A primary key uniquely identifies each row in a table. A foreign "
            "key is a column that references a key in another table and is "
            "used to establish relationships between tables."
        )
    },

    "Explain the concept of normalization.": {
        "keywords": [
            "normalization",
            "duplicate",
            "redundancy",
            "data",
            "tables",
            "integrity"
        ],
        "answer": (
            "Database normalization organizes data into related tables to "
            "reduce redundancy and improve data integrity. Normal forms such "
            "as 1NF, 2NF and 3NF define increasingly structured designs."
        )
    },

    "What are indexes and how do they improve performance?": {
        "keywords": [
            "index",
            "search",
            "query",
            "faster",
            "database"
        ],
        "answer": (
            "An index is a data structure that helps the database find rows "
            "more efficiently. It can make searches and queries faster, but "
            "indexes also require storage and can increase the cost of inserts "
            "and updates."
        )
    },

    "What is the difference between DELETE and TRUNCATE?": {
        "keywords": [
            "delete",
            "truncate",
            "rows",
            "table",
            "transaction"
        ],
        "answer": (
            "DELETE removes rows and can use a WHERE condition. TRUNCATE "
            "removes all rows from a table and is generally used when the "
            "entire table data needs to be cleared."
        )
    },

    # ---------------- DATA SCIENCE ----------------

    "Explain the steps in a typical data science project.": {
        "keywords": [
            "data",
            "cleaning",
            "exploration",
            "eda",
            "feature",
            "model",
            "evaluation"
        ],
        "answer": (
            "A typical data science project includes defining the problem, "
            "collecting data, cleaning data, performing EDA, feature "
            "engineering, training a model, evaluating it and deploying or "
            "communicating the results."
        )
    },

    "What is EDA (Exploratory Data Analysis)?": {
        "keywords": [
            "eda",
            "exploratory",
            "data",
            "patterns",
            "visualization",
            "missing"
        ],
        "answer": (
            "EDA is the process of exploring and understanding a dataset "
            "before modeling. It includes checking distributions, missing "
            "values, outliers, relationships and patterns using statistics "
            "and visualizations."
        )
    },

    "Explain the difference between correlation and causation.": {
        "keywords": [
            "correlation",
            "causation",
            "relationship",
            "cause",
            "effect"
        ],
        "answer": (
            "Correlation means two variables are associated or change "
            "together. Causation means a change in one variable directly "
            "produces a change in another. Correlation alone does not prove "
            "causation."
        )
    },

    "What is feature engineering?": {
        "keywords": [
            "feature",
            "data",
            "transformation",
            "model",
            "performance"
        ],
        "answer": (
            "Feature engineering is the process of creating, transforming or "
            "selecting input features so that machine learning models can "
            "learn useful patterns more effectively."
        )
    },

    "What is the difference between L1 and L2 regularization?": {
        "keywords": [
            "l1",
            "l2",
            "regularization",
            "weights",
            "lasso",
            "ridge"
        ],
        "answer": (
            "L1 regularization adds the absolute values of model weights to "
            "the loss and can produce sparse models with zero coefficients. "
            "L2 regularization adds squared weights and generally shrinks "
            "weights without forcing as many to zero."
        )
    },

    # ---------------- GENERAL ----------------

    "Explain the difference between a function and a method.": {
        "keywords": [
            "function",
            "method",
            "object",
            "class",
            "call"
        ],
        "answer": (
            "A function is a reusable block of code that can be called "
            "independently. A method is a function associated with an object "
            "or class and is normally called through that object or class."
        )
    },

    "What is version control and why is it important?": {
        "keywords": [
            "version control",
            "changes",
            "history",
            "collaboration",
            "git"
        ],
        "answer": (
            "Version control tracks changes to files and source code over "
            "time. It helps developers maintain history, collaborate safely, "
            "create branches and restore previous versions. Git is a popular "
            "version control system."
        )
    },

    "Explain the concept of API.": {
        "keywords": [
            "api",
            "application",
            "interface",
            "communication",
            "request",
            "response"
        ],
        "answer": (
            "An API, or Application Programming Interface, defines how "
            "different software systems communicate. A client can send a "
            "request to an API and receive a response according to the API's "
            "defined rules."
        )
    },

    "What is the difference between a stack and a queue?": {
        "keywords": [
            "stack",
            "queue",
            "lifo",
            "fifo"
        ],
        "answer": (
            "A stack follows LIFO, meaning the last item added is the first "
            "one removed. A queue follows FIFO, meaning the first item added "
            "is the first one removed."
        )
    }
}


# ============================================================
# QUESTION GENERATION
# ============================================================

def get_random_question(category="Any"):
    """Return a random technical interview question."""

    if category in technical_questions:
        return random.choice(technical_questions[category])

    all_questions = []

    for question_list in technical_questions.values():
        all_questions.extend(question_list)

    return random.choice(all_questions)


def get_hr_question():
    """Return a random HR interview question."""
    return random.choice(hr_questions)


# ============================================================
# TEXT NORMALIZATION
# ============================================================

def normalize_text(text):
    """Normalize text for evaluation."""

    text = text.lower()

    # Remove punctuation
    text = re.sub(r"[^a-z0-9+#. ]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


# ============================================================
# TECHNICAL ANSWER EVALUATION
# ============================================================

def evaluate_technical_answer(question, answer):
    """
    Evaluate technical answer using expected concepts.

    Returns:
        dict containing score, feedback and improvements.
    """

    answer_clean = normalize_text(answer)

    evaluation = question_evaluation.get(question)

    if not evaluation:
        return {
            "score": 5,
            "feedback": "⚠️ This question does not have a detailed evaluation rule yet.",
            "improvements": "Add more explanation and a practical example."
        }

    expected_keywords = evaluation["keywords"]
    reference_answer = evaluation["answer"]

    matched_keywords = []

    for keyword in expected_keywords:

        keyword_clean = normalize_text(keyword)

        if keyword_clean in answer_clean:
            matched_keywords.append(keyword)

    keyword_count = len(expected_keywords)

    if keyword_count > 0:
        concept_score = (
            len(matched_keywords) / keyword_count
        ) * 10
    else:
        concept_score = 0

    word_count = len(answer.split())

    # Very short answers
    if word_count < 8:
        return {
            "score": 1,
            "feedback": "❌ Your answer is too short to demonstrate understanding.",
            "improvements": (
                f"Explain the concept in more detail. "
                f"A good answer should cover: {', '.join(expected_keywords)}."
            )
        }

    # Detect extremely weak/nonsense answers
    weak_phrases = [
        "i dont know",
        "dont know",
        "no idea",
        "nothing",
        "yes",
        "no",
        "maybe",
        "i think so",
        "asdf",
        "abc",
        "xyz"
    ]

    if any(phrase in answer_clean for phrase in weak_phrases):
        return {
            "score": 1,
            "feedback": "❌ The answer does not demonstrate knowledge of the question.",
            "improvements": (
                f"Study these important concepts: "
                f"{', '.join(expected_keywords)}."
            )
        }

    # Score based on concepts, NOT just answer length
    score = round(concept_score)

    # Give small bonus for reasonable explanation
    if word_count >= 20 and len(matched_keywords) >= 2:
        score += 1

    score = max(1, min(10, score))

    # Feedback
    if score <= 3:
        feedback = (
            "❌ Your answer appears incorrect or does not cover the "
            "important concepts required for this question."
        )

    elif score <= 5:
        feedback = (
            "⚠️ Your answer shows some understanding, but several important "
            "concepts are missing or unclear."
        )

    elif score <= 7:
        feedback = (
            "👍 Your answer is partially correct and covers some important "
            "concepts."
        )

    elif score <= 9:
        feedback = (
            "🌟 Good answer. You covered most of the important concepts."
        )

    else:
        feedback = (
            "🎉 Excellent answer. You covered the key concepts expected "
            "for this question."
        )

    missing_keywords = [
        keyword
        for keyword in expected_keywords
        if keyword not in matched_keywords
    ]

    improvements = ""

    if missing_keywords:
        improvements += (
            "Important concepts missing: "
            + ", ".join(missing_keywords)
            + ". "
        )

    improvements += (
        "A strong answer should explain the concept clearly and, "
        "where possible, include a simple example."
    )

    return {
        "score": score,
        "feedback": feedback,
        "improvements": improvements,
        "correct_answer": reference_answer
    }


# ============================================================
# HR ANSWER EVALUATION
# ============================================================

def evaluate_hr_answer(question, answer):
    """
    HR answers do not have one fixed correct answer.
    Evaluate relevance, structure and completeness.
    """

    answer_clean = normalize_text(answer)
    word_count = len(answer.split())

    if word_count < 8:
        return {
            "score": 2,
            "feedback": "❌ Your HR answer is too short.",
            "improvements": (
                "Give a specific answer with an example from your "
                "education, project or experience."
            )
        }

    # Generic HR quality indicators
    quality_words = [
        "experience",
        "project",
        "team",
        "learn",
        "challenge",
        "result",
        "skill",
        "goal",
        "achievement",
        "improve",
        "responsibility",
        "example"
    ]

    matched = [
        word for word in quality_words
        if word in answer_clean
    ]

    # Base score
    if word_count < 20:
        score = 4
    elif word_count < 40:
        score = 6
    elif word_count < 70:
        score = 8
    else:
        score = 9

    # Relevance bonus
    if len(matched) >= 3:
        score += 1

    score = min(10, score)

    if score <= 4:
        feedback = (
            "⚠️ Your answer needs more specific details and examples."
        )
    elif score <= 6:
        feedback = (
            "👍 Good start, but your answer could be more specific."
        )
    elif score <= 8:
        feedback = (
            "🌟 Good HR answer with reasonable detail."
        )
    else:
        feedback = (
            "🎉 Strong HR answer with good detail and structure."
        )

    return {
        "score": score,
        "feedback": feedback,
        "improvements": (
            "Use a clear structure, give a real example, "
            "and explain the result or what you learned."
        )
    }


# ============================================================
# MAIN ANSWER EVALUATOR
# ============================================================

def evaluate_answer(question, answer):
    """
    Main interview answer evaluator.

    Technical questions:
        Evaluate expected concepts.

    HR questions:
        Evaluate relevance and answer quality.
    """

    if not answer or not answer.strip():
        return {
            "score": 0,
            "feedback": "❌ No answer was provided.",
            "improvements": "Please write an answer before submitting."
        }

    # HR question
    if question in hr_questions:
        return evaluate_hr_answer(question, answer)

    # Technical question
    return evaluate_technical_answer(question, answer)


# ============================================================
# INTERVIEW CATEGORIES
# ============================================================

def get_interview_categories():
    """Return available interview categories."""

    return list(technical_questions.keys()) + ["HR Questions"]