from selenium.common.exceptions import NoSuchElementException


class BasePage(object):

    def __init__(self, browser, url, timeout=10):
        """Конструктор класса.
        :param WebDriver browser: The browser's driver
        :param url:
        """
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)  # Неявное ожидание со значением по умолчанию 10

    def open(self):
        """метод открывает нужную страницу,
        используя метод get()
        """
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
