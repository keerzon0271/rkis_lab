class User:
    def __init__(self, login, password):
        self.Login = login
        self.Password = password

    def __repr__(self):
        return f"User(Login='{self.Login}', Password='{self.Password}')"

users = [
    User("admin", "12345"),
    User("vadim", "12223"),
    User("user1", "password"),
    User("test", "test123"),
    User("john", "doe")
]

target_login = "vadim"
target_password = "12223"

found_user = next((user for user in users if user.Login == target_login and user.Password == target_password), None)

print("Найден пользователь:", found_user)
