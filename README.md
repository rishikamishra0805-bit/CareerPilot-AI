# CareerPilot-AI 🚀

**AI-Powered Career & Placement Assistant**

CareerPilot-AI is an intelligent web application designed to help students and job seekers navigate their career paths. It utilizes Artificial Intelligence to analyze resumes, match job descriptions, conduct mock interviews, and generate personalized career roadmaps.

## ✨ Key Features

- **📄 Resume Analysis:** Upload your resume, and the AI will scan it to identify strengths, weaknesses, missing keywords, and formatting issues.
- **💼 Job Match:** Paste a Job Description (JD), and the AI will compare it with your profile/skills to give you a percentage match score and suggestions on how to improve.
- **🎤 AI Mock Interview:** An interactive AI interviewer that asks relevant technical and HR questions, listens to your answers, and provides detailed feedback.
- **🗺️ Career Roadmap:** Based on your current skills, education, and interests, the AI generates a step-by-step roadmap for your desired career path.

## 🛠️ Tech Stack

- **Language:** Python
- **Backend Framework:** Flask (or mention FastAPI if you used it)
- **Frontend:** HTML, CSS, JavaScript (or mention React if used)
- **AI Integration:** OpenAI API / Google Gemini API
- **PDF Processing:** PyPDF2 / pdfplumber
- **Environment:** Virtual Environment (venv)

## 🚀 Installation & Setup

Follow these steps to run the project locally on your machine:

**1. Clone the repository:**
```bash
git clone https://github.com/rishikamishra0805-bit/CareerPilot-AI.git
cd CareerPilot-AI
2. Create a virtual environment (Recommended):

bash
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
# Activate on macOS/Linux:
source venv/bin/activate
3. Install the required dependencies:

bash
pip install -r requirements.txt
4. Set up your API Key:

Create a .env file in the root directory.

Add your OpenAI/Gemini API key inside it: API_KEY=your_api_key_here

5. Run the application:

bash
python app.py
Open your browser and go to http://127.0.0.1:5000 (or the port shown in the terminal).

📂 Project Structure
text
CareerPilot-AI/
│
├── app.py                 # Main Flask application entry point
├── pdf_parser.py          # Handles PDF text extraction from resumes
├── resume_analyzer.py     # AI logic for analyzing resumes (if you have this file)
├── job_matcher.py         # AI logic for matching JDs with profiles
├── interview.py           # AI logic for conducting mock interviews
├── roadmap.py             # AI logic for generating career roadmaps
├── requirements.txt       # List of Python dependencies
├── .gitignore             # Files to ignore in Git
└── README.md              # Project documentation
📝 Usage Guide
Analyze Resume: Upload your PDF resume via the web interface.

Match Job: Paste the job description you want to apply for.

Interview: Click on the "Interview" tab and start answering the AI's questions.

Roadmap: Enter your target job role and current skills to see your personalized roadmap.

🤝 Contributing
Contributions are welcome! If you have ideas to improve this project, feel free to fork the repository, make your changes, and submit a pull request.

📄 License
This project is open-source and available under the MIT License.

Created by [Your Name]

text

**Note:** I noticed in your previous screenshot that you have `debug_pdf.py` and `pyvenv.cfg`. I have included the structure based on the main files I saw (`app.py`, `job_matcher.py`, `interview.py`, `roadmap.py`, `pdf_parser.py`). You can edit the "Project Structure" section in the README to perfectly match your actual files if there are any differences.
