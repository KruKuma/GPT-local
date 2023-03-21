import abc


class BaseGPT(abc.ABC):
    @abc.abstractmethod
    def gpt_request(self, prompt):
        raise NotImplementedError("override me")
