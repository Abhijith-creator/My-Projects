from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

SIMILAR_ACCOUNT = "_abishai_xavier_"
USERNAME = "sug_kun_roo_"
PASSWORD = "zaqwsxcde"


class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.wait.until(EC.presence_of_element_located((By.NAME, "username")))

        # Handle cookie warning
        try:
            cookie_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Only allow essential cookies')]")
            cookie_button.click()
        except NoSuchElementException:
            pass

        # Login
        username_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")

        username_input.send_keys(USERNAME)
        password_input.send_keys(PASSWORD)
        time.sleep(random.uniform(1.5, 2.5))
        password_input.send_keys(Keys.ENTER)

        # Dismiss save login prompt
        try:
            not_now = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not now')]")))
            not_now.click()
        except Exception:
            pass

        # Dismiss notification prompt
        try:
            not_now2 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]")))
            not_now2.click()
        except Exception:
            pass

    def find_followers(self):
        try:
            self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
            print(f"✅ Loaded profile: {SIMILAR_ACCOUNT}")
            time.sleep(4)

            # Wait and click "followers" link
            followers_link = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@href, '/followers')]")
            ))
            followers_link.click()
            print("✅ Clicked followers link")

            # Wait for modal (scrollable area)
            modal = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//div[@role='dialog']//div[@class='_aano']")
            ))
            print("✅ Followers modal found")

            # Scroll the modal to load more followers
            for i in range(5):
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
                print(f"➡ Scrolled modal {i + 1} times")
                time.sleep(random.uniform(1.8, 2.5))

        except Exception as e:
            print("❌ Failed during find_followers()")
            print(e)

    def follow(self):
        buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button')

        for button in buttons:
            try:
                if button.text == "Follow":
                    button.click()
                    time.sleep(random.uniform(1, 2))
            except ElementClickInterceptedException:
                try:
                    cancel_btn = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
                    cancel_btn.click()
                except NoSuchElementException:
                    pass


# Run the bot
if __name__ == "__main__":
    bot = InstaFollower()
    bot.login()
    bot.find_followers()
    bot.follow()
