import google.generativeai as genai
import os
from utils import load_env_variables, timing

@timing
def main():
    load_env_variables('env.list')
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("Write a story about a magic backpack.")
    print(response.text)

if __name__ == "__main__":
    main()