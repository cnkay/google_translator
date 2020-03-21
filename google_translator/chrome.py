from selenium.webdriver.chrome.options import Options
class ChromeOptions:
    chrome_options = Options()
    def __init__(self):
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--headless")

    def get(self):
        return self.chrome_options