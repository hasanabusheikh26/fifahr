from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class JobInput(BaseModel):
    job_title: str
    company_type: str
    location: str

@app.post("/generate-description/")
async def generate_description(input: JobInput):
    try:
        prompt = f"""
You are an expert HR job card generator that creates high-precision job listings for hiring managers.

Your task is to break down the following job title into a comprehensive, execution-focused AI profile card.

Structure:
1. **Enhanced Job Description**
2. **Job-Related (Technical/Domain) Skills**
3. **General Role Skills**
4. **Soft Skills**
5. **Key Responsibilities**
6. **Rating Breakdown** (5 key metrics + definitions for evaluation)

Job Title: {input.job_title}  
Company Type: {input.company_type}  
Location: {input.location}
        """
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1200
        )
        return { "output": response.choices[0].message["content"] }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))