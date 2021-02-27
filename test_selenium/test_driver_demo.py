import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:
    def setup(self):
        chrome_org = webdriver.ChromeOptions()
        chrome_org.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_org)
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_login(self):
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element(By.XPATH, "//*[@class='index_top_operation_loginBtn']").click()
        sleep(5)

    def test_login_tmp(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()

    def test_login_cookie(self):
        # 写入cookie
        # cookies = self.driver.get_cookies()
        # with open('tmp.txt', 'w', encoding='utf-8') as f:
        #     json.dump(cookies, f)

        # 读取 cookie
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        with open("tmp.txt", "r", encoding="utf-8") as f:
            # 序列化
            cookies = json.load(f)
        for i in cookies:
            self.driver.add_cookie(i)
        self.driver.refresh()
        sleep(6)