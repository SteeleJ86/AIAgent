import os
from dotenv import load_dotenv
from google import genai 

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key == None:
    raise RuntimeError(f"environmental variable ({api_key}): not found")

client = genai.Client(api_key=api_key)

def main():
    print("Hello from aiagent!")

    prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    try:
        query_aimodel(prompt)
    except RuntimeError as rte:
        print(f"RuntimeError when querying ai model.\n{rte}")



def query_aimodel(prompt) -> None:

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )
    
    if response.usage_metadata == None:
        raise RuntimeError("no usage metadata returned") 

    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(response.text)

if __name__ == "__main__":
    main()
