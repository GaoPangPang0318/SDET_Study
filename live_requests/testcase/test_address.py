import pytest

from live_requests.wework.address import Address


class TestAddress:
    def setup(self):
        self.address = Address()
        self.user_id = "zhangsan00123"  # 声明usr_id的变量
        self.name = "张三"
        self.mobile = "+86 13812300000"
        self.department = [1]

    @pytest.mark.parametrize("user_id, mobile",[("zhangsan00123", "13812301091"),
                                                ("zhangsan00124", "13812312092"),
                                                ("zhangsan00125", "13812323093"),
                                                ("zhangsan00126", "13812334094"),
                                                ("zhangsan00127", "13812345095"),
                                                ("zhangsan00128", "13812356096"),
                                                ("zhangsan00129", "13812367097"),
                                                ("zhangsan00122", "13812378098")])
    def test_create_member(self, user_id, mobile):
        # 利用删除接口进行数据清理
        self.address.delete_member(user_id)
        r = self.address.create_member(user_id, self.name, mobile, self.department)
        assert r.get('errmsg', "network error") == "created"  #get操作可获取dict的内容
        r = self.address.get_member_information(user_id)
        self.address.delete_member(user_id)  #为什么断言之前删除？如果断言不通过删除就不会被调用。注意数据前后的操作
        assert r.get("name") == self.name # 再次使用断言确保操作确实成功


    def test_get_member_information(self):
        self.address.create_member(self.user_id, self.name, self.mobile, self.department)
        r = self.address.get_member_information(self.user_id)
        assert r.get("errmsg") == "ok"
        assert r.get("name") == self.name

    def test_delete_member(self):
        self.address.create_member(self.user_id, self.name, self.mobile, self.department)
        r = self.address.delete_member(self.user_id)
        assert r.get("errmsg") == "deleted"
        r = self.address.get_member_information(self.user_id)
        assert r.get("errcode") == 60111

    def test_update(self):
        # 保证，成员一定是新添加的
        self.address.delete_member(self.user_id)
        self.address.create_member(self.user_id, self.name, self.mobile, self.department)
        new_name = self.name + "tmp"
        r = self.address.update_member(self.user_id, new_name, self.mobile)
        assert r.get("errmsg") == "updated"
        r = self.address.get_member_information(self.user_id)
        assert r.get("name") == new_name
