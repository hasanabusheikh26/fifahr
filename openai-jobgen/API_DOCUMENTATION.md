# Job Description Generator API Documentation

## Overview

The Job Description Generator API is a FastAPI-based service that generates comprehensive job descriptions using OpenAI's GPT-4 model. It takes job context information and returns structured job descriptions with enhanced details, skill categories, and key responsibilities.

## Base URL

```
https://fifahr-494kkh6jv-hass-projects-b72778ab.vercel.app
```

## Authentication

This API requires an OpenAI API key to be configured as an environment variable (`OPENAI_API_KEY`).

## Endpoints

### POST /generate-description

Generates a comprehensive job description based on provided job context.

#### Request

**URL**: `/generate-description`

**Method**: `POST`

**Content-Type**: `application/json`

#### Request Body Schema

```json
{
  "job_title": "string (required)",
  "company_name": "string (optional, default: '')",
  "seniority": "string (optional, default: '')",
  "department": "string (optional, default: '')",
  "location": "string (optional, default: '')",
  "domain": "string (optional, default: '')"
}
```

#### Request Body Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `job_title` | string | ✅ Yes | The title of the job position |
| `company_name` | string | ❌ No | Name of the company hiring |
| `seniority` | string | ❌ No | Level of seniority (e.g., "Junior", "Senior", "Lead") |
| `department` | string | ❌ No | Department where the role belongs |
| `location` | string | ❌ No | Geographic location of the position |
| `domain` | string | ❌ No | Industry or domain context |

#### Example Request

```bash
curl -X POST https://fifahr-494kkh6jv-hass-projects-b72778ab.vercel.app/generate-description \
  -H "Content-Type: application/json" \
  -d '{
    "job_title": "Software Engineer",
    "company_name": "TechCorp",
    "seniority": "Mid-level",
    "department": "Engineering",
    "location": "San Francisco, CA",
    "domain": "Technology"
  }'
```

#### Response

**Success Response (200 OK)**

```json
{
  "result": {
    "job_title": "Software Engineer",
    "enhanced_description": "We are seeking a talented Software Engineer to join our dynamic engineering team...",
    "skill_categories": {
      "job_related_skills": [
        "JavaScript",
        "React",
        "Node.js",
        "Python"
      ],
      "general_expertise": [
        "Software Development",
        "Web Technologies",
        "API Design"
      ],
      "soft_skills": [
        "Problem Solving",
        "Communication",
        "Team Collaboration"
      ]
    },
    "key_responsibilities": [
      "Develop and maintain web applications",
      "Collaborate with cross-functional teams",
      "Write clean, maintainable code",
      "Participate in code reviews"
    ]
  }
}
```

**Error Response (400 Bad Request)**

```json
{
  "detail": [
    {
      "loc": ["body", "job_title"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

**Error Response (500 Internal Server Error)**

```json
{
  "error": "OpenAI API error message"
}
```

## Implementation Guide

### 1. Environment Setup

#### Prerequisites
- Python 3.9+
- FastAPI
- OpenAI Python SDK
- Vercel CLI (for deployment)

#### Install Dependencies

```bash
pip install fastapi uvicorn openai pydantic
```

#### Environment Variables

Create a `.env` file:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 2. Project Structure

```
openai-jobgen/
├── main.py              # FastAPI application
├── requirements.txt      # Python dependencies
├── vercel.json          # Vercel deployment config
└── .gitignore          # Git ignore rules
```

### 3. Core Implementation

#### FastAPI Application Setup

```python
import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Create FastAPI app
app = FastAPI()
```

#### Request Model

```python
class JobRequest(BaseModel):
    job_title: str
    company_name: str = ""
    seniority: str = ""
    department: str = ""
    location: str = ""
    domain: str = ""
```

#### API Endpoint

```python
@app.post("/generate-description")
async def generate_description(data: JobRequest):
    # Construct prompt with job context
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
```

### 4. Deployment Configuration

#### Vercel Configuration (vercel.json)

```json
{
  "version": 2,
  "builds": [
    {
      "src": "main.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "main.py"
    }
  ]
}
```

#### Requirements (requirements.txt)

```
fastapi
uvicorn
openai
pydantic
```

### 5. Testing Examples

#### Test with cURL

```bash
# Basic request
curl -X POST https://your-app.vercel.app/generate-description \
  -H "Content-Type: application/json" \
  -d '{"job_title": "Data Scientist"}'

# Full request
curl -X POST https://your-app.vercel.app/generate-description \
  -H "Content-Type: application/json" \
  -d '{
    "job_title": "Product Manager",
    "company_name": "Innovation Labs",
    "seniority": "Senior",
    "department": "Product",
    "location": "New York",
    "domain": "SaaS"
  }'
```

#### Test with JavaScript

```javascript
const response = await fetch('https://your-app.vercel.app/generate-description', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    job_title: 'Frontend Developer',
    company_name: 'TechStart',
    seniority: 'Mid-level',
    department: 'Engineering',
    location: 'Remote',
    domain: 'Web Development'
  })
});

const data = await response.json();
console.log(data);
```

#### Test with Python

```python
import requests

url = "https://your-app.vercel.app/generate-description"
payload = {
    "job_title": "Backend Engineer",
    "company_name": "API Corp",
    "seniority": "Senior",
    "department": "Engineering",
    "location": "Austin, TX",
    "domain": "Technology"
}

response = requests.post(url, json=payload)
print(response.json())
```

### 6. Error Handling

The API includes comprehensive error handling:

- **400 Bad Request**: Invalid request body or missing required fields
- **500 Internal Server Error**: OpenAI API errors or other server issues

### 7. Rate Limits and Performance

- **Response Time**: Typically 15-20 seconds (due to OpenAI API calls)
- **Token Limit**: 1000 max tokens per response
- **Model**: GPT-4 for high-quality outputs

### 8. Security Considerations

- API key is stored as environment variable
- Input validation using Pydantic models
- Error messages don't expose sensitive information

### 9. Monitoring and Logging

For production deployment, consider adding:
- Request/response logging
- Performance monitoring
- Error tracking
- Rate limiting

### 10. Scaling Considerations

- Vercel automatically scales based on demand
- Consider implementing caching for similar requests
- Monitor OpenAI API usage and costs

## Integration Examples

### Frontend Integration (React)

```jsx
import React, { useState } from 'react';

function JobDescriptionGenerator() {
  const [jobData, setJobData] = useState({
    job_title: '',
    company_name: '',
    seniority: '',
    department: '',
    location: '',
    domain: ''
  });
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const generateDescription = async () => {
    setLoading(true);
    try {
      const response = await fetch('/generate-description', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(jobData)
      });
      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      {/* Form inputs */}
      <button onClick={generateDescription} disabled={loading}>
        {loading ? 'Generating...' : 'Generate Description'}
      </button>
      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </div>
  );
}
```

### Mobile App Integration (React Native)

```javascript
const generateJobDescription = async (jobData) => {
  try {
    const response = await fetch('https://your-app.vercel.app/generate-description', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(jobData)
    });
    
    const result = await response.json();
    return result;
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
};
```

This comprehensive documentation provides everything needed to understand, implement, and integrate the Job Description Generator API. 