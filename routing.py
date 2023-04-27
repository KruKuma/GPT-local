import os

import flask
import flask_caching
import openai

import app
import utils


class Router:
    def __init__(self, application):
        if not isinstance(application, flask.Flask):
            raise TypeError("'application' is not a flask.Flask")

        self._application = application

        self._cache = flask_caching.Cache(application)
        project_directory = os.path.dirname(os.path.abspath(__file__))
        dot_env_file_path = os.path.join(project_directory, ".env")
        dot_env_file = utils.DotEnvFile(dot_env_file_path)
        open_api_key = dot_env_file.load_open_ai_key()
        model_code = dot_env_file.load_model_code()

        self._server = app.Server(model_code["chat_model"],
                                  model_code["text_completion"])

        openai.api_key = open_api_key.get("api_key")

    def define_routing(self):
        application = self._application

        application.add_url_rule("/", view_func=self._home)
        application.add_url_rule("/chat", view_func=self._chat)
        application.add_url_rule("/textcompletion", view_func=self._text_completion)

    @staticmethod
    def _home():
        return "OpenAI GPT on Flask"

    def _chat(self):
        self._server.chat_request()
        return flask.jsonify(success=True)

    def _text_completion(self):
        self._server.text_completion_request()
        return flask.jsonify(success=True)
