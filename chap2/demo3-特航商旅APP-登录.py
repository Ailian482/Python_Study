from appium import webdriver
import time
import unittest

class TeHangLogin(unittest.TestCase):
    def setUp(self) -> None:
        desired_caps ={}
        desired_caps['platformName'] = "Android"
        desired_caps['platformVersion'] = "10"
        desired_caps['deviceName'] = "f71c5b6c"
        desired_caps['noReset'] = "True"
        desired_caps['appPackage'] = "com.tehang.TMC"
        desired_caps['appActivity'] = "com.tehang.TMC.MainActivity"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def tearDown(self) -> None:
        pass

    def test_001_login(self):
        self.driver.implicitly_wait(60)
        # 定位账号输入框
        account_ele = self.driver.find_element_by_xpath("//android.widget.EditText[@elementId='d799271b-7010-4fb2-8f67-700ac38e0ec3']")
        # account_ele = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[3]/android.view.View/android.widget.EditText")
        # 输入账号
        account_ele.send_keys('13632296609')
        # 定位密码输入框
        passwd_ele = self.driver.find_element_by_xpath("//android.widget.EditText[@elementId='d799271b-7010-4fb2-8f67-700ac38e0ec3']")

        # passwd_ele = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[4]/android.view.View/android.widget.EditText")
        # passwd_ele = self.driver.find_element_by_id("d2bc69f0-f373-42ee-b8b4-ddc08a184c67")
        # 输入密码
        passwd_ele.click()
        passwd_ele.send_keys('@12345678')
        # 定位登录按钮
        login_ele = self.driver.find_element_by_xpath("//android.widget.Button[1]")
        # 点击登录
        login_ele.click()



if __name__ == "__main__":
    unittest.main()