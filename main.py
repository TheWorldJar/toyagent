import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from arguments import Commands


def main():
    """Program entry point."""
    if len(sys.argv) < 2:
        print(
            "Error: please provide a prompt when running this tool: python3 main.py {promt} --{argument}"
        )
        sys.exit(1)
    command = None
    if len(sys.argv) > 2:
        match sys.argv[2]:
            case Commands.VERBOSE.value:
                command = Commands.VERBOSE
            case _:
                print("Error: command not recognized. Valid arguments are:\n")
                for c in Commands:
                    print(c.value)
                sys.exit(1)
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
    match command:
        case Commands.VERBOSE:
            print(
                f"User prompt: {user_prompt}\n"
                f"Prompt tokens: {response.usage_metadata.prompt_token_count}\n"
                f"Response tokens: {response.usage_metadata.candidates_token_count}\n"
            )
        case _:
            pass


if __name__ == "__main__":
    main()
