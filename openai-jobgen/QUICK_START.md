# Quick Start Guide - Job Description Generator API

## 🚀 Live API Endpoint

**Base URL**: `https://fifahr-494kkh6jv-hass-projects-b72778ab.vercel.app`

## 📋 API Summary

### Endpoint
```
POST /generate-description
```

### Input (Request Body)
```json
{
  "job_title": "Software Engineer",           // REQUIRED
  "company_name": "TechCorp",                 // OPTIONAL
  "seniority": "Senior",                      // OPTIONAL
  "department": "Engineering",                 // OPTIONAL
  "location": "San Francisco, CA",            // OPTIONAL
  "domain": "Technology"                      // OPTIONAL
}
```

### Output (Response)
```json
{
  "result": {
    "job_title": "Software Engineer",
    "enhanced_description": "Detailed job description...",
    "skill_categories": {
      "job_related_skills": ["JavaScript", "React", "Node.js"],
      "general_expertise": ["Software Development", "Web Technologies"],
      "soft_skills": ["Problem Solving", "Communication"]
    },
    "key_responsibilities": [
      "Develop and maintain web applications",
      "Collaborate with cross-functional teams"
    ]
  }
}
```

## 🔧 Implementation Examples

### 1. cURL Test
```bash
curl -X POST https://fifahr-494kkh6jv-hass-projects-b72778ab.vercel.app/generate-description \
  -H "Content-Type: application/json" \
  -d '{"job_title": "Data Scientist", "company_name": "AI Corp"}'
```

### 2. JavaScript/Fetch
```javascript
const response = await fetch('https://fifahr-494kkh6jv-hass-projects-b72778ab.vercel.app/generate-description', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    job_title: 'Frontend Developer',
    company_name: 'TechStart',
    seniority: 'Mid-level',
    location: 'Remote'
  })
});

const data = await response.json();
console.log(data.result);
```

### 3. Python/Requests
```python
import requests

response = requests.post(
    'https://fifahr-494kkh6jv-hass-projects-b72778ab.vercel.app/generate-description',
    json={
        'job_title': 'Product Manager',
        'company_name': 'Innovation Labs',
        'seniority': 'Senior',
        'domain': 'SaaS'
    }
)

result = response.json()
print(result['result'])
```

### 4. React Component
```jsx
import React, { useState } from 'react';

function JobGenerator() {
  const [jobTitle, setJobTitle] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const generateJob = async () => {
    setLoading(true);
    try {
      const response = await fetch('https://fifahr-494kkh6jv-hass-projects-b72778ab.vercel.app/generate-description', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ job_title: jobTitle })
      });
      const data = await response.json();
      setResult(data.result);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <input 
        value={jobTitle} 
        onChange={(e) => setJobTitle(e.target.value)}
        placeholder="Enter job title"
      />
      <button onClick={generateJob} disabled={loading}>
        {loading ? 'Generating...' : 'Generate Job Description'}
      </button>
      {result && (
        <div>
          <h3>{result.job_title}</h3>
          <p>{result.enhanced_description}</p>
          <h4>Skills:</h4>
          <ul>
            {result.skill_categories.job_related_skills.map(skill => (
              <li key={skill}>{skill}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
```

## ⚡ Response Times
- **Typical**: 15-20 seconds
- **Model**: GPT-4
- **Token Limit**: 1000 tokens

## 🛡️ Error Handling
- **400**: Missing required fields
- **500**: Server/OpenAI API errors

## 📊 Field Descriptions

| Field | Required | Example | Description |
|-------|----------|---------|-------------|
| `job_title` | ✅ Yes | "Software Engineer" | The position title |
| `company_name` | ❌ No | "Google" | Hiring company name |
| `seniority` | ❌ No | "Senior" | Junior/Mid/Senior/Lead |
| `department` | ❌ No | "Engineering" | Team/Department |
| `location` | ❌ No | "Remote" | Geographic location |
| `domain` | ❌ No | "Technology" | Industry context |

## 🎯 Use Cases
- HR job posting creation
- Recruitment automation
- Job board integration
- Career site enhancement
- ATS system integration

## 🔗 Full Documentation
See `API_DOCUMENTATION.md` for complete implementation details. 