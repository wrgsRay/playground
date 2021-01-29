class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

    def block(self, user):
        if user == self.username:
            raise InvalidInput(f"Cannot block yourself")
        print(f"{user} is blocked")


user_1 = User('001', 'angela')
user_2 = User('002', 'jack')

user_1.follow(user_2)


class InvalidInput(Exception):
    pass


user_1.block('angela')