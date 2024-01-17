class AuthState:
    pass

class Authed(AuthState):
    def __init__(self, name):
        self.name = name

class Unauthed(AuthState):
    pass

class AuthPresenter:
    def __init__(self):
        self.state = Unauthed()

    @property
    def is_authed(self):
        return isinstance(self.state, Authed)

    @property
    def user_name(self):
        if isinstance(self.state, Authed):
            return self.state.name
        return "Unknown"

    def login(self, username):
        self.state = Authed(username)

    def logout(self):
        self.state = Unauthed()

if __name__ == "__main__":
    auth_presenter = AuthPresenter()
    print(auth_presenter.is_authed)
    print(auth_presenter.user_name)
    auth_presenter.login("Gleb")
    print(auth_presenter.is_authed)
    print(auth_presenter.user_name)
    auth_presenter.logout()
    print(auth_presenter.is_authed)
    print(auth_presenter.user_name)
