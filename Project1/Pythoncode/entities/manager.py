class Manager:

    def __init__(self, manager_id: int, first_name: str, last_name: str):
        self.manager_id = manager_id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"manager ID: {self.manager_id}, first name: {self.first_name}, last name: {self.last_name}"

    def as_json_dict(self):
        return {
            "managerID": self.manager_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
        }
