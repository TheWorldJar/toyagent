import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    if sys.argv[1] is None:
        print(
            "Error: please provide a prompt when running this tool: python3 main.py {promt} --{argument}"
        )
        sys.exit(1)
    be_verbose = False
    if len(sys.argv) > 2 and sys.argv[2] != "--verbose":
        print("Error: invalid argument: python3 main.py {promt} --{argument}")
        sys.exit(1)
    elif len(sys.argv) > 2 and sys.argv[2] == "--verbose":
        be_verbose = True
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    user_prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    print(f"{response.text}\n")
    if be_verbose:
        print(
            f"User prompt: {user_prompt}"
            f"Prompt tokens: {response.usage_metadata.prompt_token_count}\n"
            f"Response tokens: {response.usage_metadata.candidates_token_count}\n"
        )


if __name__ == "__main__":
    main()
