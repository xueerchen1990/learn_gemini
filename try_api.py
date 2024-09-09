import google.generativeai as genai
import os
from utils import load_env_variables, timing

@timing
def main():
    load_env_variables('env.list')
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    model = genai.GenerativeModel("gemini-1.5-flash")

    # Count input tokens
    prompt = "Write a story about a magic backpack."
    token_count = model.count_tokens(prompt)
    print(f"Input tokens: {token_count.total_tokens}")

    # Generate content and count output tokens
    output_tokens = 0
    for chunk in model.generate_content(prompt, stream=True):
        print(chunk.text, end="")
        output_tokens += model.count_tokens(chunk.text).total_tokens

    print(f"\n\nOutput tokens: {output_tokens}")
    print(f"Total tokens: {token_count.total_tokens + output_tokens}")

if __name__ == "__main__":
    main()