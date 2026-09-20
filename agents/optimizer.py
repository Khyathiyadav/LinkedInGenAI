import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY was not found.")

client = genai.Client(api_key=api_key)


def optimizer_agent(
    post,
    feedback,
    topic,
    tone,
    audience,
    language,
    length
):
    """Improve a LinkedIn post based on critic feedback."""

    prompt = f"""
You are an expert LinkedIn content optimizer.

Improve the following LinkedIn post using the critic's feedback.

USER REQUIREMENTS
Topic: {topic}
Tone: {tone}
Target Audience: {audience}
Language: {language}
Length: {length}

CURRENT POST
----------------
{post}
----------------

CRITIC FEEDBACK
----------------
{feedback}
----------------

INSTRUCTIONS
1. Preserve the core topic and useful ideas.
2. Address every issue mentioned in the critic feedback.
3. Improve the opening hook.
4. Make the content more specific and original.
5. Keep the requested tone.
6. Keep it appropriate for LinkedIn.
7. Do not invent personal experiences or facts.
8. Use readable paragraphs.
9. Do not mention the critic or this optimization process.
10. Return ONLY the improved LinkedIn post.
"""

    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt
    )

    return interaction.output_text.strip()