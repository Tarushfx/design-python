class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def send_welcome_email(self):
        pass

    def validate_password(self, password):
        pass

    def change_password(self, new_password):
        pass

    def update_profile(self, new_name, new_email):
        pass

    def show_profile(self):
        pass


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class EmailService:
    def send_welcome_email(self, user):
        pass


class AuthenticationService:
    def validate_password(self, user, password):
        pass

    def change_password(self, user, new_password):
        pass


class ProfileService:
    def update_profile(self, user, new_name, new_email):
        pass

    def show_profile(self, user):
        pass


user = User("John Doe", "johndoe@example.com", "password123")
email_service = EmailService()
profile_service = ProfileService()

email_service.send_welcome_email(user)

auth_service = AuthenticationService()
auth_service.validate_password(user, "password123")

profile_service.update_profile(user, "Jane Doe", "janedoe@example.com")
profile_service.show_profile(user)
