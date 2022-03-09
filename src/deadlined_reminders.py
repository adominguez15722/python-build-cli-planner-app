from abc import ABCMeta, abstractmethod
from collections.abc import Iterable
from abc import ABC
from dateutil.parser import parse
from datetime import datetime

class DeadlinedMetaReminder(Iterable, metaclass = ABCMeta):
    def __init__(self):
        self.Iterable = Iterable

    @abstractmethod
    def is_due(self):
        pass


class DeadlinedReminder(Iterable, ABC):
    def __init__(self):
        self.Iterable = Iterable
        self.ABC = ABC

    @abstractmethod
    def is_due(self):
        pass


class DateReminder(DeadlinedReminder):
    def __init__(self, text, date):
        self.text = text
        self.date = parse(date, dayfirst = True)


    def is_due(self, date):
        self.date <= datetime.now()


    