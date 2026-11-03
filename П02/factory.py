from repository import InMemoryRoleRepository
from file_repository import FileRoleRepository
from sql_repository import SqlRoleRepository


def create_repository(kind, **kwargs):
    if kind == "memory":
        return InMemoryRoleRepository()
    if kind == "file":
        return FileRoleRepository(kwargs["path"])
    if kind == "sql":
        return SqlRoleRepository(kwargs["connection_string"])
    raise ValueError(f"unknown repository: {kind}")