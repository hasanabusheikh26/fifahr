# Lovable Integration Guide - Job Description Generator API

## 🚀 API Information for Lovable

### Base URL
```
https://fifahr-494kkh6jv-hass-projects-b72778ab.vercel.app
```

### Endpoint
```
POST /generate-description
```

## 📋 API Configuration for Lovable

### 1. **API Name**: Job Description Generator

### 2. **Request Configuration**
- **Method**: POST
- **URL**: `https://fifahr-494kkh6jv-hass-projects-b72778ab.vercel.app/generate-description`
- **Content-Type**: `application/json`

### 3. **Request Body Schema**
```json
{
  "job_title": "string (required)",
  "company_name": "string (optional)",
  "seniority": "string (optional)",
  "department": "string (optional)",
  "location": "string (optional)",
  "domain": "string (optional)"
}
```

### 4. **Response Schema**
```json
{
  "result": {
    "job_title": "string",
    "enhanced_description": "string",
    "skill_categories": {
      "job_related_skills": ["string"],
      "general_expertise": ["string"],
      "soft_skills": ["string"]
    },
    "key_responsibilities": ["string"]
  }
}
```

## 🔧 Lovable Setup Steps

### Step 1: Add API to Lovable
1. Go to your Lovable dashboard
2. Navigate to "Integrations" or "APIs"
3. Click "Add New API"
4. Enter the following details:

**API Details:**
- **Name**: Job Description Generator
- **Base URL**: `https://fifahr-494kkh6jv-hass-projects-b72778ab.vercel.app`
- **Description**: Generate comprehensive job descriptions using AI

### Step 2: Configure Endpoint
**Endpoint Configuration:**
- **Path**: `/generate-description`
- **Method**: POST
- **Headers**: 
  ```
  Content-Type: application/json
  ```

### Step 3: Define Request Parameters
**Required Parameters:**
- `job_title` (string) - The job position title

**Optional Parameters:**
- `company_name` (string) - Company name
- `seniority` (string) - Junior/Mid/Senior/Lead
- `department` (string) - Department name
- `location` (string) - Geographic location
- `domain` (string) - Industry domain

### Step 4: Test the Connection
Use this test payload in Lovable:
```json
{
  "job_title": "Software Engineer",
  "company_name": "TechCorp",
  "seniority": "Mid-level",
  "department": "Engineering",
  "location": "Remote",
  "domain": "Technology"
}
```

## 🛠️ Troubleshooting Connection Issues

### If you get "Connection Error - Debug Info":

1. **Check CORS Settings**: ✅ Fixed - CORS headers are now enabled
2. **Verify URL**: Make sure the URL is exactly: `https://fifahr-494kkh6jv-hass-projects-b72778ab.vercel.app/generate-description`
3. **Test Health Endpoint**: Try `GET https://fifahr-494kkh6jv-hass-projects-b72778ab.vercel.app/health`
4. **Check Method**: Ensure it's set to POST, not GET
5. **Verify Headers**: Content-Type should be `application/json`

### Manual Test Commands:
```bash
# Test health endpoint
curl https://fifahr-494kkh6jv-hass-projects-b72778ab.vercel.app/health

# Test main endpoint
curl -X POST https://fifahr-494kkh6jv-hass-projects-b72778ab.vercel.app/generate-description \
  -H "Content-Type: application/json" \
  -d '{"job_title": "Data Scientist"}'
```

## 📊 Expected Response Format

**Success Response (200):**
```json
{
  "result": {
    "job_title": "Data Scientist",
    "enhanced_description": "We are seeking a talented Data Scientist to join our team...",
    "skill_categories": {
      "job_related_skills": ["Python", "Machine Learning", "SQL"],
      "general_expertise": ["Data Analysis", "Statistical Modeling"],
      "soft_skills": ["Problem Solving", "Communication"]
    },
    "key_responsibilities": [
      "Analyze large datasets to identify trends",
      "Develop predictive models",
      "Present findings to stakeholders"
    ]
  }
}
```

**Error Response (400/500):**
```json
{
  "error": "Error message here"
}
```

## 🎯 Use Cases in Lovable

### 1. **HR Job Posting Creation**
- Input: Job title and company details
- Output: Complete job description with skills and responsibilities

### 2. **Recruitment Automation**
- Automatically generate job descriptions for new positions
- Standardize job posting format across company

### 3. **Job Board Integration**
- Generate descriptions for job board postings
- Ensure consistent quality and format

## ⚡ Performance Notes
- **Response Time**: 15-20 seconds (due to OpenAI API)
- **Rate Limits**: No strict limits, but consider OpenAI API costs
- **Availability**: 24/7 via Vercel

## 🔗 Support
If you continue to have connection issues:
1. Check if the API is accessible from your network
2. Verify Lovable's network settings
3. Try the health endpoint first: `/health`
4. Contact support with the specific error message

The API is now configured with CORS support and should work seamlessly with Lovable! 🚀 