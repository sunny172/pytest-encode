from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDaka:

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

    def test_daka(self):
        # 点击【工作台】
        self.driver.find_element(MobileBy.XPATH, '//*[@text="工作台"]').click()
        # 向下滑动两次，再向上查找，直到找到元素
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("打卡").instance(0));').click()
        # 找到【外出打卡】页面
        self.driver.find_element(MobileBy.XPATH, '//*[@text="外出打卡"]').click()
        # 点击【打卡】
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "次外出")]').click()
        # 打印页面结构
        print(self.driver.page_source)
        # 检测是否打开成功
        self.driver.find_element(MobileBy.XPATH, '//*[@text="外出打卡成功"]')

