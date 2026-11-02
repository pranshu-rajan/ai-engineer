import os
import logging

from dotenv import load_dotenv
from groq import Groq, GroqError

# -------------------- CONFIGURATION --------------------

load_dotenv()

MODEL = "openai/gpt-oss-120b"
REASONING_EFFORT = "medium"
MAX_TOKENS = 2048

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

logger = logging.getLogger(__name__)


# -------------------- CLIENT SETUP --------------------

def create_client() -> Groq:
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. Check your .env file."
        )

    return Groq(
        api_key=api_key,
        timeout=30.0,
        max_retries=2
    )


# -------------------- AI RESPONSE --------------------

def generate_response(
    client: Groq,
    prompt: str,
    system_prompt: str = "You are a helpful AI assistant."
) -> str:

    if not prompt.strip():
        raise ValueError("Prompt cannot be empty.")

    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        reasoning_effort=REASONING_EFFORT,
        reasoning_format="hidden",
        max_completion_tokens=MAX_TOKENS,
        temperature=0.7
    )

    return response.choices[0].message.content or ""


# -------------------- MAIN APPLICATION --------------------

def main() -> None:
    try:
        client = create_client()

        prompt = input("Enter your prompt: ")

        answer = generate_response(
            client=client,
            prompt=prompt
        )

        print("\n" + "=" * 50)
        print("GPT-OSS 120B RESPONSE")
        print("=" * 50)
        print(answer)

    except (GroqError, ValueError) as error:
        logger.error("Request failed: %s", error)


if __name__ == "__main__":
    main()