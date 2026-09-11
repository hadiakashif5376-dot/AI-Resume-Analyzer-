import json
import os

from dotenv import load_dotenv
from groq import Groq

from prompts import SYSTEM_PROMPT, OUTPUT_SCHEMA, build_user_prompt

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")

if not API_KEY:
    raise RuntimeError(
        "GROQ_API_KEY is not set. Add it to your .env file before running the app."
    )

client = Groq(api_key=API_KEY)


def analyze_resume(resume_text, job_description):
    response = client.chat.completions.create(
        model=MODEL,
        temperature=0.2,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(resume_text, job_description)},
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "resume_analysis",
                "strict": True,
                "schema": OUTPUT_SCHEMA,
            },
        },
    )

    content = response.choices[0].message.content
    if not content:
        raise ValueError("The AI returned an empty response.")

    try:
        result = json.loads(content)
    except json.JSONDecodeError as exc:
        raise ValueError("The AI returned invalid JSON.") from exc

    _validate_result(result)
    return result


def _validate_result(result):
    required = [
        "overall_score",
        "matching_skills",
        "missing_skills",
        "ats_keywords",
        "problems",
        "recommendations",
        "final_result",
    ]

    if not isinstance(result, dict):
        raise ValueError("AI response must be a JSON object.")

    missing = [key for key in required if key not in result]
    if missing:
        raise ValueError(f"AI response is missing fields: {', '.join(missing)}")

    score = result["overall_score"]
    if not isinstance(score, int) or not 0 <= score <= 100:
        raise ValueError("AI returned an invalid match score.")

    list_fields = [
        "matching_skills",
        "missing_skills",
        "ats_keywords",
        "problems",
        "recommendations",
    ]

    for field in list_fields:
        if not isinstance(result[field], list):
            raise ValueError(f"AI field '{field}' must be a list.")

    if not isinstance(result["final_result"], str) or not result["final_result"].strip():
        raise ValueError("AI returned an invalid final result.")
