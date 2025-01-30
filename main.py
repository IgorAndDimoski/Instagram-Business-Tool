import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from dotenv import load_dotenv

load_dotenv(".env")

SIMILAR_ACCOUNT = "bakkerijwolf"
USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(8)
        accept_cookies_button = self.driver.find_element(By.CLASS_NAME, value="_a9--._ap36._a9_0")
        accept_cookies_button.click()
        time.sleep(5)
        username_entry = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        username_entry.send_keys(USER_NAME)
        password_entry = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        password_entry.send_keys(PASSWORD + Keys.ENTER)
        time.sleep(10)
        not_now_button = self.driver.find_element(By.CLASS_NAME, value="x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz.x6s0dn4.xjyslct.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619.x1ypdohk.x1f6kntn.xwhw2v2.xl56j7k.x17ydfre.x2b8uid.xlyipyv.x87ps6o.x14atkfc.xcdnw81.x1i0vuye.xjbqb8w.xm3z3ea.x1x8b98j.x131883w.x16mih1h.x972fbf.xcfux6l.x1qhh985.xm0m39n.xt0psk2.xt7dq6l.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x1n5bzlp.x173jzuc.x1yc6y37")
        not_now_button.click()
    def find_followers(self):
        self.driver.get("https://www.instagram.com/mumscakesandsweets/followers/")
        time.sleep(5)
        followers_ = self.driver.find_element(By.CLASS_NAME, value="x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x5n08af.x9n4tj2._a6hd")
        followers_.click()
        time.sleep(5)
        scroll_pol = self.driver.find_element(By.CLASS_NAME, value="xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6")
        for i in range(10):
            scroll_pol.send_keys(Keys.END)
            time.sleep(1)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value="div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x16n37ib.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.xs83m0k.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1")
        time.sleep(3)
        for button in all_buttons:
            try:
                # Attempt to click the "Follow" button
                button.click()
                time.sleep(2)

                # Check if an "OK" button appears after clicking "Follow"
                try:
                    OK_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'OK')]")
                    OK_button.click()
                    time.sleep(2)
                except NoSuchElementException:
                    # No "OK" button, continue to the next button
                    pass

            except ElementClickInterceptedException:
                # Handle dialog for already-followed accounts
                try:
                    cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                    cancel_button.click()
                    time.sleep(2)
                except NoSuchElementException:
                    print("Cancel button not found!")


driver = InstaFollower()
time.sleep(3)
driver.login()
time.sleep(3)
driver.find_followers()
time.sleep(3)
driver.follow()

