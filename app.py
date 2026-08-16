from flask import Flask, render_template, request, redirect, session
from db import Base, engine, SessionLocal
import models
import PyPDF2
import docx
import json
from ai import analyze_resume
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

Base.metadata.create_all(bind=engine)

#HOME
@app.route("/")
def home():
    if "user" in session:
        return redirect("/dashboard")
    return redirect("/login")

#----SIGNUP
@app.route("/signup", methods=["GET", "POST"])
def signup():
    db =SessionLocal()

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        existing_user = db.query(models.User).filter_by(email=email).first()
        if existing_user:
            return "User already exists"

        hashed_password = generate_password_hash(password)

        user = models.User(name=name, email=email, password=hashed_password)
        db.add(user)
        db.commit()

        return redirect("/login")
    
    return render_template("signup.html")

#LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():

    if "user" in session:
        return redirect("/dashboard")

    db = SessionLocal()

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = db.query(models.User).filter_by(
            email=email
        ).first()

        if user and check_password_hash(user.password, password):

            session["user"] = user.email
            session["name"] = user.name

            return redirect("/dashboard")

        else:
            return "Invalid credentials"

    return render_template("login.html")


#DASHBOARD
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect("/login")

    result = None

    if request.method == "POST":
        user_goal = request.form.get("role")
        resume_text = request.form.get("resume")

        file = request.files.get("file")

        #file handling
        if file and file.filename != "":
            if file.filename.endswith(".pdf"):
                try:
                    pdf_reader = PyPDF2.PdfReader(file)
                    text = ""
                    for page in pdf_reader.pages:
                        text += page.extract_text() or ""
                    resume_text = text
                except Exception as e:
                    result = {"error": f"PDF error: {str(e)}"}

            elif file.filename.endswith(".docx"):
                try:
                    doc = docx.Document(file)
                    text = ""
                    for para in doc.paragraphs:
                        text += para.text +"\n"
                    resume_text = text
                except Exception as e:
                    result = {"error": f"Docx error: {str(e)}"}

        if resume_text and user_goal:
            try:
                result = analyze_resume(resume_text, user_goal)

                #save to db
                db = SessionLocal()
                user = db.query(models.User).filter_by(email=session["user"]).first()

                report = models.Reports(
                    user_id = user.id,
                    resume_text = resume_text,
                    result = json.dumps(result)
                )

                db.add(report)
                db.commit()

            except Exception as e:
                result = {"error": f"AI error: {str(e)}"}
    return render_template(
        "dashboard.html",
        user=session["user"],
        name=session["name"],
        result = result
    )

#history
@app.route("/history")
def history():
    if "user" not in session:
        return redirect("/login")

    db = SessionLocal()
    user = db.query(models.User).filter_by(email=session["user"]).first()

    reports = db.query(models.Reports).filter_by(user_id = user.id).all()

    #convert JSON string > dict
    pasred_reports = []
    for r in reports:
        try:
            pasred_result = json.loads(r.result)
        except:
            pasred_result = []

        pasred_reports.append({
            "resume":r.resume_text,
            "result":pasred_result
        })

    return render_template("history.html", reports=pasred_reports)
    
# logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)  
