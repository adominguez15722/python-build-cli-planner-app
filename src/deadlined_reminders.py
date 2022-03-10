from abc import ABCMeta, abstractmethod
from cgitb import text
from collections.abc import Iterable
from abc import ABC
from xmlrpc.client import _iso8601_format
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

    # def __iter__(self, text, date):
    #     self.text = text
    #     self.date = self.date.isoformat()


class DateReminder(DeadlinedReminder):
    def __init__(self, text, date):
        self.text = text
        self.date = parse(date, dayfirst = True)


    def is_due(self):
        return self.date <= datetime.now()

    def __iter__(self):
        return iter([self.text, self.date.isoformat()])

    