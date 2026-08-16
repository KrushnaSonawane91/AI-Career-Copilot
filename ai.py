import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def analyze_resume(resume_text, user_goal):

    prompt = f"""
You are a senior software engineer and hiring manager.

Evaluate the resume based on the user's goal.

User goal: "{user_goal}"

STRICT RULES:
- Extract only relevant skills for this goal.
- Remove irrelevant tools and skills.
  Example: Excel may be irrelevant for a Backend Developer role.
- Identify real skill gaps.
- Generate a roadmap only for missing skills.
- Generate interview questions relevant to the user's goal.
- Make the output DIFFERENT based on the user's goal.
- Do not recommend skills that are already present in the resume.

ROADMAP RULES:
- For every important missing skill, create a roadmap item.
- Each roadmap item must contain:
  - skill: name of the missing skill
  - description: explain what the candidate should learn and why it is important
  - resources: practical topics, tools, or project ideas to learn it
- Do not give only the skill name.
- Make the roadmap specific to the target role.

Return ONLY valid JSON in exactly this format:

{{
    "skills": [],
    "missing_skills": [],
    "roadmap": [
        {{
            "skill": "",
            "description": "",
            "resources": []
        }}
    ],
    "interview_questions": []
}}

Resume:
{resume_text}
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        content = response.text.strip()

        # Remove markdown code fences if Gemini adds them
        if content.startswith("```json"):
            content = content[7:]

        elif content.startswith("```"):
            content = content[3:]

        if content.endswith("```"):
            content = content[:-3]

        content = content.strip()

        result = json.loads(content)

        print("\n========== GEMINI RESULT ==========")
        print(json.dumps(result, indent=4))
        print("===================================\n")

        return result

    except Exception as e:

        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": str(e)
        }