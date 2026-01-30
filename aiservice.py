from google import genai
from google.genai import types
import os
"""
Do what needs to be done according to team; these are just recommendations!
Finalize production-ready GPT prompt templates for:
Major recommendations
Career paths
University matching

Optimize prompts for:
Consistent JSON outputs
Minimal hallucination
Realistic academic advice

Stress-test prompts with:
Different GPAs
Diverse interests and goals

Partner with Backend to:
Tune system + user prompts
Ensure alignment with FastAPI response schema

"""

class AIService:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set")
        
        self.client = genai.Client(api_key=api_key)
        # Use the correct model name for google-genai package
        self.model = "gemini-3-flash-preview"
    
    #temperature controls how creative the ai, 0=no creative, 1 = very creative
    def generate_response(self, prompt: str, temperature: float = 0.7):
        """Generate AI response from prompt"""
        boiler_plate = """Major recommendation
Based on this student profile:
- Interests: [e.g., science, helping people, technology]
- Strengths: [e.g., math, communication, problem-solving]
- Career Goals: [e.g., high salary, work-life balance, creativity]
- GPA: [X.XX]

Task: Recommend 3-5 college majors that align with their profile. For each major, provide:
1. Major name
2. Brief description (2-3 sentences)
3. Why it matches their profile
4. Typical career paths
5. General difficulty level (considering their GPA)

Format your response in a conversational but organized way. Be encouraging and specific.
Career Path recommendation
Student Profile:
- Major of Interest: [if selected]
- Interests: [list]
- Priorities: [salary, job growth, work-life balance, impact, etc.]
- GPA: [X.XX]

Available Data Context:
[Insert relevant career data: job titles, average salaries, growth outlook, degree requirements]

Task: Suggest 3-5 career paths. For each career, include:
1. Job title
2. What the job involves (2-3 sentences)
3. Average salary range
4. Job growth outlook (next 10 years)
5. Required education level
6. Why it matches the student's profile

Be realistic about competitiveness while remaining encouraging.

University Matching

D. University Matching
Student Profile:
- GPA: [X.XX]
- SAT/ACT: [if provided]
- Major Interest: [field of study]
- Location Preference: [region/state]
- School Size Preference: [small/medium/large or no preference]
- Budget: [consideration level]

Available University Data:
[Insert dataset: school names, average admitted GPA, acceptance rates, locations, strengths]

Task: Categorize and recommend universities in three tiers:

**Reach Schools** (2-3 schools)
- Schools where the student's stats are below average but within reach
- Include: Name, location, why it's a good fit, admission tips

**Match Schools** (3-4 schools)
- Schools where the student's stats align well with admitted student averages
- Include: Name, location, why it's a good fit, what makes them stand out

**Safety Schools** (2-3 schools)
- Schools where the student's stats exceed typical admits
- Include: Name, location, why it's still a great option, unique opportunities

Be specific about why each school matches their interests and goals. Include application tips where relevant.
"""
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt+"\n"+(boiler_plate),
                config={"temperature": temperature}
            )
            return response.text
        except Exception as e:
            raise Exception(f"AI generation failed: {str(e)}")
    
    #Combines history with users message and calls prompting func
    def chat(self, message: str, history: list = None):
        """Chat with conversation history"""
        if history:
            context = "\n".join(history)
            prompt = f"{context}\n\nUser: {message}"
        else:
            prompt = message
        
        return self.generate_response(prompt)
