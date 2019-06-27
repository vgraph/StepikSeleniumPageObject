from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    # Заглушка
    # можно просто pass
    def __init__(self, *args, **kwargs):
        """Конструктор вызывает конструктор класса предка и передает ему все те аргументы,
         которые мы передали в конструктор MainPage
        :param args:
        :param kwargs:
        """
        super(MainPage, self).__init__(*args, **kwargs)

    # Методы перенесены в base_page.py
    # def go_to_login_page(self):
    #     login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     login_link.click()
    #
    # def should_be_login_link(self):
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
