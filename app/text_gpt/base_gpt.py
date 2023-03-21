import abc


class BaseGPT(abc.ABC):
    @abc.abstractmethod
    def gpt_request(self, conversation_history, prompt):
        raise NotImplementedError("override me")
