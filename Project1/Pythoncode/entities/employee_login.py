class EmployeeLogin:

    def __init__(self, user_id: int, username: str, u_password: str):
        self.user_id = user_id
        self.username = username
        self.u_password = u_password

    def __str__(self):
        return f"user ID: {self.user_id}, username: {self.username}, password: {self.u_password}"


def as_json_dict(self):
    return {
        "userID": self.user_id,
        "username": self.username,
        "uPassword": self.u_password,
    }
