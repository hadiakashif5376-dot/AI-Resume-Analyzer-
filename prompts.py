SYSTEM_PROMPT = """
You are an expert resume and job-description analyzer.

Compare the candidate's resume with the supplied job description. Base your analysis
only on the information present in the resume and job description.

Important:
- Missing from the resume does not mean the candidate does not possess the skill.
- Identify skills that are present and clearly demonstrated.
- Identify job requirements that are missing or not clearly demonstrated.
- Suggest relevant ATS keywords from the job description that the resume should
  naturally address when appropriate.
- Identify concrete resume problems.
- Give practical recommendations.
- Return only valid JSON matching the requested schema.
"""

OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "overall_score": {
            "type": "integer",
            "minimum": 0,
            "maximum": 100
        },
        "matching_skills": {
            "type": "array",
            "items": {"type": "string"}
        },
        "missing_skills": {
            "type": "array",
            "items": {"type": "string"}
        },
        "ats_keywords": {
            "type": "array",
            "items": {"type": "string"}
        },
        "problems": {
            "type": "array",
            "items": {"type": "string"}
        },
        "recommendations": {
            "type": "array",
            "items": {"type": "string"}
        },
        "final_result": {
            "type": "string"
        }
    },
    "required": [
        "overall_score",
        "matching_skills",
        "missing_skills",
        "ats_keywords",
        "problems",
        "recommendations",
        "final_result"
    ],
    "additionalProperties": False
}


def build_user_prompt(resume_text, job_description):
    return f"""
RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Analyze the resume against this job description and return the required JSON.
"""
