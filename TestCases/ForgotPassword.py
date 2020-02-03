from selenium import webdriver
import unittest
import HtmlTestRunner

from SeleniumPrgms.POMProjectFlipcart.Pages.ForgotpasswordPage import Forgot


class Flipcart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r"C:\Users\Shashi_Admin\PycharmProjects\SeleniumPrgms\drivers\chromedriver.exe")
        cls.driver.maximize_window()


    def test_forgotpassword(self):
        driver = self.driver
        driver.get("https://www.flipkart.com/")
        forgotpassword = Forgot(driver)
        forgotpassword.click_popup()
        forgotpassword.click_loginonhomepage()
        forgotpassword.enter_username("9620690281")
        forgotpassword.click_forgot()
        forgotpassword.logout()



    if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
            output=r'C:\Users\Shashi_Admin\PycharmProjects\SeleniumPrgms\POMProjectFlipcart\Reports'))
