import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_study_plan(performance_data):

    prompt = f"""
    A student completed an adaptive GRE test.

    Weak topics:
    {performance_data}

    Generate a short 3-step study plan to improve their performance.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content