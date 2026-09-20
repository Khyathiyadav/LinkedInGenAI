from agents.critic import critic_agent


post = """
Learning Python taught me that programming is not about
memorizing syntax. It is about learning how to solve problems.

When I started, even simple errors felt frustrating.
But every debugging session taught me something new.

The biggest lesson I learned is simple:

Don't just watch tutorials. Build something.

A small project that you actually understand can teach you
more than hours of passive learning.

For students learning Python, focus on consistency,
practice, and solving real problems.

What was the first Python project you built?
"""


evaluation = critic_agent(
    post=post,
    topic="Learning Python",
    tone="Professional",
    audience="Students and aspiring developers"
)


print("\n" + "=" * 60)
print("CRITIC EVALUATION")
print("=" * 60)

for key, value in evaluation.items():
    print(f"{key}: {value}")