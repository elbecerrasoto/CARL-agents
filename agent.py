from abc import ABC, abstractmethod

class Agent(ABC):

    # Main Attributes
    @abstractmethod
    def act(self, obs):
        raise NotImplementedError

    @abstractmethod
    def learn(self, env, steps):
        raise NotImplementedError

    # Secondary Attributes
    @property
    @abstractmethod
    def status(self):
        raise NotImplementedError

    @abstractmethod
    def forget(self):
        raise NotImplementedError

    @abstractmethod
    def save(self):
        raise NotImplementedError

    @abstractmethod
    def load(self):
        raise NotImplementedError
