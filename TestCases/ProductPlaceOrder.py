from selenium import webdriver
import unittest
import HtmlTestRunner

from SeleniumPrgms.POMProjectFlipcart.Pages.AddToCartPage import Addtocart
from SeleniumPrgms.POMProjectFlipcart.Pages.CheckoutPage import Checkout
from SeleniumPrgms.POMProjectFlipcart.Pages.LoginPage import loginpopup
from SeleniumPrgms.POMProjectFlipcart.Pages.HomePage import Search
from SeleniumPrgms.POMProjectFlipcart.Pages.Logoutpage import Logout


class Flipcart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r"C:\Users\Shashi_Admin\PycharmProjects\SeleniumPrgms\drivers\chromedriver.exe")
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://www.flipkart.com/")
        login = loginPopup(driver)
        login.click_popup()
        login.click_loginonhomepage()
        login.enter_username("9620690281")
        login.enter_password("Chinnu1989$")
        login.click_loginbutton()


        search = Search(driver)
        search.enter_productname("samsung s10")
        search.click_product()


        addtocart = Addtocart(driver)
        addtocart.click_addtocart()
        addtocart.click_plussign()
        addtocart.click_savebutton()
        addtocart.click_movetocartbutton()
        addtocart.click_placeorderbutton()

        checkout = Checkout(driver)
        checkout.enter_name("Shilpashree")
        checkout.enter_phno("9620689990")
        checkout.enter_pincode("577204")
        checkout.enter_locality("Vinobanagar")
        checkout.enter_address("Sri Maruthi Krupa,60 feet Road,Vinoba nagar")
        checkout.enter_landmark("OPP ShubhaMangala Kalyana Mantapa")
        checkout.click_homeaddress()
        checkout.click_deliverbutton()
        checkout.click_continuebutton()
        checkout.click_flipcarthomebutton()

        logout = Logout(driver)
        logout.close()



        if __name__ == '__main__':
            unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
                output='C:/Users/Shashi_Admin/PycharmProjects/SeleniumPrgms/POMProjectFlipcart/Reports'))
