import app.text_gpt


class Server:
    def __init__(self, chat_model, text_completion_model):
        self._chat = app.text_gpt.Chat(chat_model)
        self._completion = app.text_gpt.Completion(text_completion_model)

    def chat_request(self):
        pass

    def text_completion_request(self):
        pass
