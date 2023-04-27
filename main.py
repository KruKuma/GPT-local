import os

import openai

import app
import utils

project_directory = os.path.dirname(os.path.abspath(__file__))
dot_env_file_path = os.path.join(project_directory, ".env")
dot_env_file = utils.DotEnvFile(dot_env_file_path)
open_api_key = dot_env_file.load_open_ai_key()
model_code = dot_env_file.load_model_code()

_controller = app.Controller(model_code["chat_model"],
                             model_code["text_completion"])

openai.api_key = open_api_key.get("api_key")

app_option = 1
while app_option != 0:
    try:
        option = int(input("\n===== OPTION ====="
                           "\n1. Chat"
                           "\n2. Text Completion"
                           "\n0. Quit"
                           "\n>>"))

        if option == 1:
            _controller.chat_request()
        elif option == 2:
            _controller.text_completion_request()
        elif option == 0:
            app_option = 0
        else:
            print("\nNot an option")

    except ValueError:
        print("\nNot an integer")
