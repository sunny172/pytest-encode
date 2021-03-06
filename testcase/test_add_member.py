from app_addMember.menu_page import MenuPage


class TestAddMember:
    # 测试手动添加成员功能
    def test_addMember(self):
        mp = MenuPage()
        mp.address_page().add_user().manually_add_user()
