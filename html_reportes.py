from selenium import webdriver
import pytest
class TestOrm:
    @pytest.fixture()
    def setup(self):
        self.drivers=webdriver.Chrome(executable_path=r"C:\Users\Ram\Desktop\Drivers\chromedriver.exe")
        #self.drivers.maximize_window()
    def test_url(self,setup):
        self.drivers.get("https://opensource-demo.orangehrmlive.com/")
        assert self.drivers.title=="OrangeHRM"
    def test_login(self,setup):
        self.drivers.get("https://opensource-demo.orangehrmlive.com/")
        self.drivers.find_element_by_id("txtUsername").send_keys("Admin")
        self.drivers.find_element_by_id("txtPassword").send_keys("admin123")
        self.drivers.find_element_by_xpath("//*[@id='btnLogin']").click()


