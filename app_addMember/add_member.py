from appium.webdriver.common.mobileby import MobileBy

from app_addMember.manually_add_member import ManuallyAddUser


# 添加成员功能类
class AddMember:
    def __init__(self, driver):
        self.driver = driver

    def add_user(self):
        # 点击【添加成员】
        self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        return ManuallyAddUser(self.driver)
