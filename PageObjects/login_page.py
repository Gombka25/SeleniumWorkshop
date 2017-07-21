from page_object_example.base_page import BasePage


class LoginPage(BasePage):

    @property
    def user_text_field(self):
        return self.driver.find_element_by_name('uid')

    @property
    def password_text_field(self):
        return self.driver.find_element_by_name('password')

    @property
    def login_button(self):
        return self.driver.find_element_by_name('btnLogin')

    def login_user(self, username, password):
        self.user_text_field.send_keys(username)
        self.password_text_field.send_keys(password)
        self.login_button.click()
