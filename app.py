import logging
import os
import openai
import openai.error

import utils


def build_api():
    project_directory = os.path.dirname(os.path.abspath(__file__))
    dot_env_file_path = os.path.join(project_directory, ".env")
    dot_env_file = utils.DotEnvFile(dot_env_file_path)
    open_api_key = dot_env_file.load_open_ai_key()

    openai.api_key = open_api_key.get("api_key")


def generate_text(prompt):
    try:
        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7
        )

        message = completions.choices[0].text
        return message.strip()
    except openai.error.APIError as e:
        return logging.error(e)


def main():
    app = 1

    while app == 1:
        question = input(">> ")

        if question != "quit":
            answer = generate_text(question)
            print(answer)
            continue

        else:
            app = 0


if __name__ == "__main__":
    build_api()
    main()
