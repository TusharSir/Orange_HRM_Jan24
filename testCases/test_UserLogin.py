from pageObjects.UserLoginPage import Login_Class
from utilities.Logger import LoggenClass
from utilities.readconfigfile import Readconfig


class Test_UserProfile:
    log = LoggenClass.log_generator()
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()

    def test_verify_Url_001(self, setup):
        self.log.info("TestCase test_verify_Url_001 is started")
        self.log.info("Opening browser and navigating to OrangeHrm site")
        self.driver = setup
        self.log.info("Checking the Page Title")
        if self.driver.title == "OrangeHRM":
            self.log.info("Page Title is-->" + self.driver.title)
            self.log.info("TestCase test_verify_Url_001 is Passed")
            assert True
        else:
            self.log.info("TestCase test_verify_Url_001 is Failed")
            self.driver.save_screenshot("..\\ScreenShots\\test_verify_Url_Fail.Png")
            assert False
        self.log.info("TestCase test_verify_Url_001 is Completed")

    def test_UserLogin_002(self, setup):
        self.log.info("TestCase test_UserLogin_002 is started")
        self.log.info("Opening browser and navigating to OrangeHrm site")
        self.driver = setup
        self.lp = Login_Class(self.driver)
        self.log.info("Enter Username")
        self.lp.Enter_Username(self.username)
        self.log.info("Enter Password")
        self.lp.Enter_Password(self.password)
        self.log.info("Click on Login Button")
        self.lp.Click_Login()
        if self.lp.Validate_Login_Status() == "login pass":
            self.log.info("Click on Menu Button")
            self.lp.Click_Menu_Button()
            self.log.info("Click on Logout Button")
            self.lp.Click_Logout()
            self.log.info("TestCase test_UserLogin_002 is passed")
            assert True
        else:
            self.driver.save_screenshot("..\\ScreenShots\\test_UserLogin_002_Fail.png")
            self.log.info("TestCase test_UserLogin_002 is Failed")
            assert False


# pytest -v -s --html=HTMLReports/myReport.html --alluredir="AllureReports" -n=2 --browser chrome
