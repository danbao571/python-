from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time


class Csdn_spider(object):

    def __init__(self, username, password):
        self.url = 'https://passport.csdn.net/login'
        self.username = username
        self.password = password
        self.track = []

        self.browser = webdriver.Firefox()
        self.wait = WebDriverWait(self.browser, 10, 0.5)
        self.action = ActionChains(self.browser)

    def run(self):
        self.browser.get(self.url)
        try:
            print('sadsa')
            time.sleep(2)
            # 切换到账户密码登录
            self.browser.find_element_by_xpath('//div[@class="main-select"]/ul/li[2]/a').click()
            # 输入账户密码
            time.sleep(2)
            input_username = self.browser.find_element_by_xpath('//input[@id="all"]')
            input_username.send_keys(self.username)
            time.sleep(1)
            input_password = self.browser.find_element_by_xpath('//input[@id="password-number"]')
            input_password.send_keys(self.password)
            # 点击登录
            time.sleep(1)
            logino = self.browser.find_element_by_xpath('//button[@data-type="account"]')
            logino.click()
            # span = self.browser.find_element_by_xpath('//span[@id="nc_1_n1z"]')
            # if span:
            #     self.action.click_and_hold(span).perform()
            #     self.action.reset_actions()
            #     self.action.move_by_offset(180, 0).perform()

        except Exception as e:
            return "登录失败"

    # def get_track(self, distance):
    #     current = 0
    #     mid = distance * 3 / 4
    #     t = 0.2
    #     v = 0
    #     while current < distance:
    #         if current < mid:
    #             a = 2
    #         else:
    #             a = -3
    #         v0 = v
    #         v = v0 + a * t
    #         move = v0 * t + 1 / 2 * a * t * t
    #         current += move
    #         self.track.append(round(move))
    #     return self.track


if __name__ == "__main__":
    username = input("请输入账号：")
    password = input("请输入密码：")
    login = Csdn_spider(username, password)
    login.run()



