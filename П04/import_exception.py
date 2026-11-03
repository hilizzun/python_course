import errno
import os


class ImportException(Exception):
    pass


def parse(lines):
    return [line.rstrip("\n") for line in lines if line.strip()]


def retry(path, attempts=3):
    if attempts <= 0:
        raise ImportException(f"cannot read {path}: retries exhausted")
    return import_file(path, _attempt=attempts - 1)


def _is_sharing_violation(e: OSError) -> bool:
    if getattr(e, "winerror", None) == 32:
        return True
    return e.errno in (errno.EBUSY, errno.EAGAIN)


def import_file(path, _attempt=3):
    try:
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
        return parse(lines)
    except OSError as e:
        if _is_sharing_violation(e):
            return retry(path, _attempt)   # файл занят — пробуем ещё раз
        raise ImportException(f"cannot read {path}") from e