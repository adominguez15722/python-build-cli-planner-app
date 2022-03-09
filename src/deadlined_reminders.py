from abc import ABCMeta, abstractmethod
from collections.abc import Iterable
from abc import ABC
from dateutil.parser from parse

class DeadlinedMetaReminder(Iterable, ABCMeta):
    @abstractmethod
    def is_due():
        pass

class DeadlinedReminder(Iterable, ABC):
    @abstractmethod
    def is_due():
        pass


class DateReminder(DeadlinedReminder):
    def __init__(self, text, date):
        self.text = text
        self.date = parse(date, dayfirst = True)

    