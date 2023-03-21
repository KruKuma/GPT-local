import logging
import os
import openai
import openai.error

import utils


class Application:
    def __init__(self):
        project_directory = os.path.dirname(os.path.abspath(__file__))
        dot_env_file_path = os.path.join(project_directory, ".env")
        dot_env_file = utils.DotEnvFile(dot_env_file_path)
        open_api_key = dot_env_file.load_open_ai_key()
        model_code = dot_env_file.load_model_code()
        self._model = model_code.get("model")

        openai.api_key = open_api_key.get("api_key")

    def generate_text(self, prompt):
        self.check_prompt(prompt)

        try:
            completions = openai.Completion.create(
                engine=self._model,
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.7
            )

            message = completions.choices[0].text.strip()
            if not message:
                return "Could not generate response"

            return message
        except openai.error.APIError as e:
            logging.error(f"OpenAI API returned an API Error: {e}")
            return "API Error"
        except openai.error.APIConnectionError as e:
            logging.error(f"Failed to connect to OpenAI API: {e}")
            return "Connection Error"
        except openai.error.RateLimitError as e:
            logging.error(f"OpenAI API request exceeded rate limit: {e}")
            return "Rate Limit Exceeded"

    @staticmethod
    def check_prompt(prompt):
        if not isinstance(prompt, str) or len(prompt) == 0:
            raise ValueError("Invalid prompt")