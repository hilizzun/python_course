class ReportWriter:
    def __init__(self, path):
        self._path = path
        self._file = None

    def __enter__(self):
        self._file = open(self._path, "w", encoding="utf-8")
        return self

    def __exit__(self, exc_type, exc, tb):
        if self._file is not None:
            self._file.close()
        return False

    def write(self, line):
        self._file.write(line + "\n")


# использование
with ReportWriter("report.txt") as w:
    w.write("header")
    w.write("body")