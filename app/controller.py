import app.text_gpt


class Controller:
    def __init__(self, chat_model, text_completion_model):
        self._chat = app.text_gpt.Chat(chat_model)
        self._completion = app.text_gpt.Completion(text_completion_model)

    def chat_request(self):
        print("Type 'quit' to close")

        conversation_history = [{
            "role": "system",
            "content": "You are a helpful assistant."}]

        run = 1
        while run != 0:
            prompt = input(">>")

            if prompt != "quit":
                response = self._chat.gpt_request(conversation_history, prompt)
                print(f"\n{response}")
            else:
                run = 0

    def text_completion_request(self):
        print("Type 'quit' to close")

        conversation_history = None

        run = 1
        while run != 0:
            prompt = input(">>")

            if prompt != "quit":
                response = self._completion.gpt_request(conversation_history, prompt)
                print(f"\n{response}")
            else:
                run = 0
