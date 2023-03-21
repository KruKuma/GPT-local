
import logging
import openai

from app.text_gpt.base_gpt import BaseGPT


class Chat(BaseGPT):
    def __init__(self, model):
        self._model = model

    def gpt_request(self, prompt):
        self.check_prompt(prompt)

        try:
            completions = openai.ChatCompletion.create(
                model=self._model,
                messages=[{"role": "user", "content": prompt}]
            )

            message = completions.choices[0].message.content
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
