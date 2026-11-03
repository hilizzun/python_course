class ReportBuilder:

    def __init__(self, header, rows, footer=None):
        self.header = header
        self.rows = rows
        self.footer = footer or (lambda: "")

    def build(self):
        return "".join([self.header(), *self.rows(), self.footer()])


class Sale:
    def __init__(self, date, amount):
        self.date = date
        self.amount = amount


sales = [Sale("2026-01-01", 100), Sale("2026-01-02", 200)]

report = ReportBuilder(
    header=lambda: "sales\n",
    rows=lambda: [f"{s.date}: {s.amount}\n" for s in sales],
)

print(report.build())