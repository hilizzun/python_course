from repository import IRoleRepository


class SqlRoleRepository(IRoleRepository):

    def __init__(self, connection_string):
        self._connection_string = connection_string

    def is_assigned(self, role, user):
        # /* запрос к БД */ return false
        return False

    def assign(self, role, user):
        # /* INSERT */
        pass

    def unassign(self, role, user):
        # /* DELETE */
        pass