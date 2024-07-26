class UserDto():

    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    @staticmethod
    def serialize(user):
        return {
            id: user.id,
            name: user.name,
            email: user.email
        }