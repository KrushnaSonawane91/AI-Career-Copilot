# 🤖 AI Career Copilot

AI Career Copilot is an AI-powered web application that analyzes a user's resume against a target career role and provides personalized career guidance.

The application uses **Google Gemini AI** to analyze resume content and generate relevant skills, missing skills, a learning roadmap, and interview questions.

It also provides user authentication and stores previous resume analysis reports in **PostgreSQL**, allowing users to view their analysis history.

---

## ✨ Features

- 🔐 User Signup and Login
- 👤 Personalized user dashboard
- 📄 Upload a resume file
- 📝 Paste resume text directly
- 🎯 Enter a target career role
- 🤖 AI-powered resume analysis using Google Gemini
- 💡 Identify relevant skills
- 📚 Identify missing skills
- 🛣️ Generate a personalized learning roadmap
- 🎤 Generate interview questions
- 🗃️ Store analysis reports in PostgreSQL
- 📜 View previous analysis history
- 🚪 Secure logout
- 🔑 Password hashing
- 🌐 Clean and responsive web interface

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- Jinja2 Templates

### Backend
- Python
- Flask
- SQLAlchemy

### Database
- PostgreSQL
- psycopg2

### AI
- Google Gemini API
- Google GenAI Python SDK

### Resume Processing
- PyPDF2
- python-docx

### Authentication & Configuration
- Werkzeug password hashing
- python-dotenv
- Environment variables

---

## 📸 Application Screens

### 🔐 Login

Users can securely log in to their existing account using their email and password.

### 📝 Signup

New users can create an account by providing:

- Name
- Email
- Password

### 📊 Dashboard

After logging in, users can:

- Paste their resume
- Upload a resume file
- Enter their target career role
- Start the AI analysis

### 📜 History

Users can view their previous resume analysis reports stored in the PostgreSQL database.

---

## 📁 Project Structure

```text
AI_CAREER_COPILOT/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── history.html
│   ├── login.html
│   └── signup.html
│
├── ai.py
├── app.py
├── db.py
├── models.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

---

## 🔄 Application Workflow

```text
User
  │
  ▼
Signup / Login
  │
  ▼
Dashboard
  │
  ├── Enter Target Career Role
  │
  └── Upload / Paste Resume
          │
          ▼
    Resume Text Extraction
          │
          ▼
      Google Gemini AI
          │
          ▼
      Resume Analysis
          │
          ├── Relevant Skills
          ├── Missing Skills
          ├── Learning Roadmap
          └── Interview Questions
          │
          ▼
    Store Report in PostgreSQL
          │
          ▼
        History
```

---

## 🧠 How the AI Analysis Works

The user provides two main inputs:

1. **Resume**
2. **Target career role**

The application processes the resume and sends the relevant information to Google Gemini AI.

The AI analyzes the resume based on the selected career goal and generates personalized career recommendations.

### The analysis includes:

#### 1. 💻 Relevant Skills

The AI identifies the technical skills and knowledge already present in the user's resume.

Examples:

- Python
- SQL
- PostgreSQL
- Pandas
- Power BI

#### 2. 📚 Missing Skills

The AI compares the user's current skills with the requirements of the selected career role and identifies skills that should be developed.

#### 3. 🛣️ Learning Roadmap

The application generates a structured learning roadmap to help the user develop the missing skills required for the target role.

The roadmap can include:

- Recommended topics
- Learning sequence
- Practice areas
- Suggested resources

#### 4. 🎤 Interview Questions

The AI generates interview questions related to the target career role and the skills identified from the resume.

---

## 🗄️ Database

The application uses **PostgreSQL** to store user accounts and resume analysis reports.

### User Data

The application stores:

- User name
- Email
- Hashed password

### Analysis Reports

Previous resume analyses are stored so users can access them later from the **History** page.

Each user's analysis history is associated with their account.

---

## 🔐 Authentication

The application includes a user authentication system.

### Signup

New users create an account using:

- Name
- Email
- Password

Passwords are hashed before being stored in the database.

### Login

Registered users can log in using their email and password.

### Logout

Users can securely log out of their account.

---

## 📄 Resume Input

The application supports two ways of providing a resume.

### Option 1 — Paste Resume

Users can directly paste their resume text into the dashboard.

### Option 2 — Upload Resume

Users can upload a resume file for analysis.

The application extracts the resume content before sending it for AI analysis.

Supported document formats include:

- PDF
- DOCX
## ⚙️ Installation and Setup

Follow the steps below to run AI Career Copilot locally.

### 1. Clone the Repository

```bash
git clone https://github.com/KrushnaSonawane91/AI-Career-Copilot.git
```

Move into the project directory:

```bash
cd AI-Career-Copilot
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
venv\Scripts\activate
```

---

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the project root directory.

Add your secret configuration:

```env
SECRET_KEY=your_secret_key
GEMINI_API_KEY=your_gemini_api_key
```

Add your PostgreSQL database configuration according to your application's database setup.

> **Important:** Never upload your `.env` file to GitHub. It contains private credentials and API keys.

---

### 5. Configure PostgreSQL

Make sure PostgreSQL is installed and running on your system.

Create the required database and configure the database connection used by the application.

The application uses **SQLAlchemy** with **PostgreSQL** for database operations.

---

### 6. Run the Application

Activate the virtual environment and run:

```bash
python app.py
```

The Flask development server will start locally.

Open the URL shown in the terminal, usually:

```text
http://127.0.0.1:5000
```

---

## 📦 Requirements

The main technologies and packages used by this project include:

- Flask
- SQLAlchemy
- PostgreSQL
- psycopg2-binary
- Google GenAI
- PyPDF2
- python-docx
- python-dotenv
- Werkzeug
- OpenAI SDK

The complete dependency list is available in:

```text
requirements.txt
```

---

## 🔑 Environment Variables

The application uses environment variables to protect sensitive configuration.

Example:

```env
SECRET_KEY=your_secret_key
GEMINI_API_KEY=your_gemini_api_key
```

These values should be kept private.

The `.gitignore` file prevents `.env` from being uploaded to GitHub.

---

## 🛡️ Security

The project follows basic security practices including:

- Password hashing
- Environment variables for secrets
- `.gitignore` protection for sensitive files
- User-specific analysis history
- Session-based authentication

Sensitive information such as API keys, database passwords, and secret keys should never be committed to the repository.

---

## 🚀 Future Improvements

Possible future improvements include:

- 📊 Resume scoring system
- 🎯 ATS compatibility score
- 📈 Skill gap visualization
- 📄 Downloadable analysis reports
- 💼 Job recommendation system
- 🔗 Job portal integration
- 👤 User profile management
- 🔄 Password reset functionality
- 🌐 Deployment to a cloud platform
- 📱 Further mobile UI optimization

---

## 🎯 Project Goal

The goal of AI Career Copilot is to help students and job seekers understand their current skills, identify gaps for a target career, create a learning roadmap, and prepare for interviews using AI-powered resume analysis.

---

## 👨‍💻 Author

**Krushna Sonawane**

GitHub:  
https://github.com/KrushnaSonawane91

---

## 📄 License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.

---

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub.
