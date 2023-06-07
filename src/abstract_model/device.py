from abc import ABC, abstractmethod
import uuid


class Device(ABC):
    uuid = uuid.UUID
