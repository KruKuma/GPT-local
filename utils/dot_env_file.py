import os

import dotenv


class DotEnvFile:
    def __init__(self, dot_env_file_path):
        self._check_dot_env_file_path(dot_env_file_path)
        self._dot_env_file_content = dotenv.dotenv_values(dot_env_file_path)

    def load_open_ai_key(self):
        open_api_key = self._load_arguments({"api_key": "OPEN_AI_KEY"})

        return open_api_key

    def load_model_code(self):
        model_code = self._load_arguments({"chat_model": "CHAT_MODEL",
                                           "text_completion": "TEXT_COMPLETION_MODEL"})

        return model_code

    @staticmethod
    def _check_dot_env_file_path(dot_env_file_path):
        if not isinstance(dot_env_file_path, str):
            raise TypeError("'dot_env_file_path' must be a str")

        if os.path.basename(dot_env_file_path) != ".env":
            raise ValueError("'dot_env_file_path' is not a .env file")

        if not os.path.exists(dot_env_file_path):
            raise FileNotFoundError(f"'{dot_env_file_path}' does not exist")

        if not os.path.isfile(dot_env_file_path):
            raise IsADirectoryError(f"'{dot_env_file_path}' is not a file")

    def _load_arguments(self, keys_map):
        if not set(keys_map.values()).issubset(self._dot_env_file_content.keys()):
            missing_keys = sorted(set(keys_map.values()).difference(self._dot_env_file_content.keys()))
            raise KeyError(f"Missing keys in .env file: {missing_keys}")

        return {argument_name: self._dot_env_file_content[key_name] for argument_name, key_name in keys_map.items()}
