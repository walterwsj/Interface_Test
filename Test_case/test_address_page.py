from api_page.address_page import AddressPage


class TestAddressPage:
    def setup(self):
        self.address_page = AddressPage()

    def test_get(self):
        message=self.address_page.get_user()
        assert message['errcode'] in [0,60111]

    def test_add(self):
        message=self.address_page.create_user()
        print(message)
        assert message['errcode'] in [0,60111]

