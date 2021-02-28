from src.page_objects.login_screen import LoginPage


class LoginSteps(LoginPage):
    def successful_login(self):
        enter_username()
        enter_password()
        submit_form()