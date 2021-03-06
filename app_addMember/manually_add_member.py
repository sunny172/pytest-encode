from appium.webdriver.common.mobileby import MobileBy


# 手动添加成员功能类
class ManuallyAddUser:
    def __init__(self, driver):
        self.driver = driver

    def manually_add_user(self):
        # 点击【手动输入添加】
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        # 输入用户名
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/b7m"]').send_keys("test01")
        # 输入电话号
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/fwi"]').send_keys(
            "17509877890")
        # 点击【保存】
        self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()
