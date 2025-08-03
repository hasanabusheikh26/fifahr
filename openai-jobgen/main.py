import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

app = FastAPI()

class JobRequest(BaseModel):
    job_title: str
    company_name: str = ""
    seniority: str = ""
    department: str = ""
    location: str = ""
    domain: str = ""

@app.post("/generate-description")
async def generate_description(data: JobRequest):
    prompt = f"""
You are an expert hiring assistant.

Given the following job context:

- Title: {data.job_title}
- Company: {data.company_name}
- Seniority: {data.seniority}
- Department: {data.department}
- Location: {data.location}
- Domain: {data.domain}

Generate the following output as a structured JSON:

{{
  "job_title": string,
  "enhanced_description": string,
  "skill_categories": {{
    "job_related_skills": [string],
    "general_expertise": [string],
    "soft_skills": [string]
  }},
  "key_responsibilities": [string]
}}

Respond ONLY in valid JSON format. No preamble or explanations.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert hiring assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6,
            max_tokens=1000
        )

        return JSONResponse(content={"result": response.choices[0].message.content})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})