import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class TestAddUsers:

    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps['settings[waitForIdleTimeout]'] = 1
        # 客户端与appium服务端建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_addUsers(self):
        # 点击进入【通讯录】
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        # 点击【添加成员】
        self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        # 点击【手动输入添加】
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        # 输入用户名
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/b7m"]').send_keys("test01")
        # 输入电话号
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/fwi"]').send_keys("17509877890")
        # 点击【保存】
        self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()
