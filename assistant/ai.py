from openai import OpenAI
import os


# ==========================================
# AI Configuration
# ==========================================

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)


# ==========================================
# Ask AI
# ==========================================

def ask_ai(question):

    try:

        response = client.responses.create(
            model="gpt-5-mini",
            instructions=(
                "You are JARVIS, a helpful desktop AI assistant. "
                "Answer clearly and concisely. "
                "The user is interested in embedded systems, "
                "electronics, programming and engineering."
            ),
            input=question
        )

        return response.output_text

    except Exception as e:

        print(f"AI Error: {e}")

        return "Sorry, I am unable to connect to my AI brain right now."