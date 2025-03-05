
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [{
                "id": self._generateId(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # Genera un ID único para cada miembro
    def _generateId(self):
        return randint(0, 99999999)

    # Agrega un nuevo miembro a la lista
    def add_member(self, member):
        if "id" not in member:
            member["id"] = self._generateId()  # Genera un ID si no existe
        member["last_name"] = self.last_name  # Asegura que el apellido sea "Jackson"
        self._members.append(member)
        return member

    # Elimina un miembro de la lista por su ID
    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True
        return False

    # Obtiene un miembro de la lista por su ID
    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    # Actualiza un miembro de la lista por su ID
    def update_member(self, id, updated_member):
        for i, member in enumerate(self._members):
            if member["id"] == id:
                updated_member["id"] = id  # Mantiene el mismo ID
                updated_member["last_name"] = self.last_name  # Asegura el apellido
                self._members[i] = updated_member
                return True
        return False

    # Devuelve todos los miembros de la familia
    def get_all_members(self):
        return self._members