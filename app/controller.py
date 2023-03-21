import text_gpt


class Controller:
    def __init__(self, chat_model, text_completion_model):
        self._chat = text_gpt.Chat(chat_model)
        self._completion = text_gpt.Completion(text_completion_model)

    def chat_request(self):
        prompt = input(">>")
        response = self._chat.gpt_request(prompt)

        print(f"\n{response}")

    def text_completion_request(self):
        prompt = input(">>")
        response = self._completion.gpt_request(prompt)

        print(f"\n{response}")
