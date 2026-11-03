import json
from repository import IRoleRepository


class FileRoleRepository(IRoleRepository):
    def __init__(self, path):
        self._path = path
        self._links = self._load()

    def _load(self):
        try:
            with open(self._path) as f:
                return [tuple(x) for x in json.load(f)]
        except FileNotFoundError:
            return []

    def _save(self):
        with open(self._path, "w") as f:
            json.dump(self._links, f)

    def is_assigned(self, role, user):
        return (role.id, user.id) in self._links

    def assign(self, role, user):
        self._links.append((role.id, user.id))
        self._save()

    def unassign(self, role, user):
        self._links.remove((role.id, user.id))
        self._save()