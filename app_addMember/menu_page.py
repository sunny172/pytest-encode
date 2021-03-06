from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

# 菜单类
from app_addMember.add_member import AddMember


class MenuPage:

    def __init__(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"  # adb connect 127.0.0.1:7555    adb devices
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"  # APP不进行再次设置，默认FALSE（每次都会初始化APP）,会保留一些设置，缓存信息等
        caps['settings[waitForIdleTimeout]'] = 1  # 控制动态页面的等待时长
        caps['dontStopAppOnReset'] = 'true'  # 直接在APP启动的情况下操作，不重新打开APP，与drive.back()配合使用
        # 客户端与appium服务端建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    # 【消息】菜单
    def message_page(self):
        pass

    # 【通讯录】菜单
    def address_page(self):
        # 点击进入【通讯录】菜单
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        return AddMember(self.driver)

    # 【工作台】菜单
    def work_page(self):
        pass

    # 【我】菜单
    def me_page(self):
        pass
