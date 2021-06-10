from appium import webdriver
import time
import unittest

class WeiXin(unittest.TestCase):
    def setUp(self) -> None:
        desired_caps = {}
        desired_caps["platformName"] = "Android"  # 平台名称，苹果用 iSO 表示
        desired_caps["platformVersion"] = "10"  # 手机版本号与用来测试的手机的版本号要一致
        desired_caps["deviceName"] = "f71c5b6c"  # 设备名称，没有强行验证，有这个参数和值就行了
        desired_caps["noReset"] = "True"  # 不重置APP的数据，即每次跑完退出不重置数据，不用重新进入欢迎导航或者选择页面，直接进入App界面

        # 特航商旅
        # desired_caps["appPackage"] = "com.tehang.TMC"  # app包名，是手机用来区分APP的唯一标志
        # desired_caps["appActivity"] = "com.tehang.TMC.MainActivity"  # 界面，一个Activity就是一个界面

        # 微信
        desired_caps["appPackage"] = "com.tencent.mm"  # app包名，是手机用来区分APP的唯一标志
        desired_caps["appActivity"] = "com.tencent.mm.ui.LauncherUI"  # 界面，一个Activity就是一个界面

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        # 这是请求服务器（也就是appium服务端）的地址

    def test_into_friend(self):
        self.driver.implicitly_wait(60)
        # ele1 = self.driver.find_element_by_id('com.tencent.mm:id/bg1')
        ele1 = self.driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.tencent.mm:id/bg1'][1]")
        ele1.click()

if __name__ == "__main__":
    unittest.main()


