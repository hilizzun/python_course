from abc import ABC, abstractmethod


class Report(ABC):
    def build(self):
        return "".join([self.header(), *self.rows(), self.footer()])

    @abstractmethod
    def header(self): ...

    @abstractmethod
    def rows(self): ...

    def footer(self):
        return ""


class SalesReport(Report):
    def __init__(self, rows):
        self._rows = rows

    def header(self):
        return "sales\n"

    def rows(self):
        return [f"{r.date}: {r.amount}\n" for r in self._rows]