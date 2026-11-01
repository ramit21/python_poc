class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, name, email):
        if name in self.users:
            raise ValueError("User already exists") 
        self.users[name] = email
        return True

    def get_user_email(self, name):
        return self.users.get(name)

