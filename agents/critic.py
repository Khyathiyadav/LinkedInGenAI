import json
import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY was not found.")

client = genai.Client(api_key=api_key)


def critic_agent(post, topic, tone, audience):
    """Evaluate a generated LinkedIn post."""

    prompt = f"""
You are a LinkedIn content quality evaluator.

Evaluate the following generated LinkedIn post.

USER REQUIREMENTS
Topic: {topic}
Tone: {tone}
Target Audience: {audience}

GENERATED POST
----------------
{post}
----------------

Evaluate these dimensions from 1 to 10:

1. relevance
2. clarity
3. tone_consistency
4. hook_quality
5. readability
6. originality
7. linkedin_suitability

Calculate an overall_score from 1 to 10.

Also provide concise improvement_feedback.

Return ONLY valid JSON in exactly this structure:

{{
    "overall_score": 0,
    "relevance": 0,
    "clarity": 0,
    "tone_consistency": 0,
    "hook_quality": 0,
    "readability": 0,
    "originality": 0,
    "linkedin_suitability": 0,
    "improvement_feedback": ""
}}
"""

    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt
    )

    result = interaction.output_text.strip()

    # Remove markdown code fences if the model adds them
    if result.startswith("```"):
        result = result.replace("```json", "")
        result = result.replace("```", "")
        result = result.strip()

    try:
        evaluation = json.loads(result)
    except json.JSONDecodeError:
        raise ValueError(
            f"Critic returned invalid JSON:\n{result}"
        )

    return evaluation