from selenium.webdriver.firefox.options import Options
class FirefoxOptions:
    firefox_options=Options()
    def __init__(self):
        self.firefox_options.add_argument("--disable-extensions")
        self.firefox_options.add_argument("--disable-gpu")
        self.firefox_options.add_argument("--headless")
    def get(self):
        return self.firefox_options