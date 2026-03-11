from abc import ABC, abstractmethod


class StackInterface(ABC):

    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass


class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None


class Stack(StackInterface):

    def __init__(self):
        self._top = None

    def push_back(self, obj):
        if self._top is None:
            self._top = obj
            return

        cur = self._top
        while cur._next is not None:
            cur = cur._next

        cur._next = obj

    def pop_back(self):
        if self._top is None:
            return None

        # в стеке один элемент
        if self._top._next is None:
            obj = self._top
            self._top = None
            return obj

        prev = self._top
        cur = self._top._next

        while cur._next is not None:
            prev = cur
            cur = cur._next

        prev._next = None
        return cur
