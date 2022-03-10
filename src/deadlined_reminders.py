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

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is not DeadlinedReminder:
            return NotImplemented

        def attr_in_hierarchy(attr):
            return any (attr in SuperClass.__dict__ for SuperClass in subclass.__mro__)

        if not all(attr_in_hierarchy(attr) for attr in ('__iter__', 'is_due')):
            return NotImplemented

        return True
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

    