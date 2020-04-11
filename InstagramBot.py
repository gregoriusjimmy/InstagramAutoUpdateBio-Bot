from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")


class InstagramBot():

    def __init__(self, email, password):
        self.browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        # self.browser = webdriver.Chrome()
        self.email = email
        self.password = password
        self.wait = WebDriverWait(self.browser, 10)

    def signIn(self):
        self.browser.get(
            'https://www.instagram.com/accounts/login/'
        )

        emailInput = self.wait.until(
            EC.visibility_of_element_located((By.NAME, 'username'))
        )

        passwordInput = self.browser.find_element_by_name('password')
        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def editBio(self, bioText):
        self.browser.get("https://www.instagram.com/accounts/edit/")
        bioTextArea = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea')))
        bioTextArea.clear()
        bioTextArea.send_keys(bioText)
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        submitBtn = self.browser.find_elements_by_css_selector('form button')[1]
        submitBtn.click()

    def closeBrowser(self):
        self.browser.quit()
