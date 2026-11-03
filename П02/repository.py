from abc import ABC, abstractmethod


class IRoleRepository(ABC):
    @abstractmethod
    def is_assigned(self, role, user): ...
    @abstractmethod
    def assign(self, role, user): ...
    @abstractmethod
    def unassign(self, role, user): ...


class InMemoryRoleRepository(IRoleRepository):
    def __init__(self):
        self._links = []

    def is_assigned(self, role, user):
        return (role.id, user.id) in self._links

    def assign(self, role, user):
        self._links.append((role.id, user.id))

    def unassign(self, role, user):
        self._links.remove((role.id, user.id))