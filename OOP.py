class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = False
user1 = User("Anna Propas", "anna@anna.com")
print user1.name
print user1.logged
print user1.email


user2 = User("Thinh Le", "thinpsn@gmail.com")
bob = User()
print User.name = "new"
