from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY was not found.")

client = genai.Client(api_key=api_key)


def generate_post(
    topic,
    tone,
    audience,
    language,
    length,
    retrieved_posts
):
    examples = "\n\n".join(
        [
            f"Example {i + 1}:\n{post['text']}"
            for i, post in enumerate(retrieved_posts)
        ]
    )

    prompt = f"""
You are an expert LinkedIn content writer.

Generate an original LinkedIn post.

Topic: {topic}
Tone: {tone}
Target Audience: {audience}
Language: {language}
Length: {length}

REFERENCE POSTS:
{examples}

Use the reference posts only to understand writing patterns,
structure and tone. Do not copy their wording.

Requirements:
- Start with an engaging hook.
- Stay relevant to the topic.
- Match the requested tone.
- Use short, readable paragraphs.
- Do not mention the reference posts.
- Do not invent personal experiences.
- Return only the final LinkedIn post.
"""

    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt
    )

    return interaction.output_text