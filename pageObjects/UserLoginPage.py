from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Login_Class:
    Text_Username_Xpath = "//input[@placeholder='Username']"
    Text_Password_Xpath = "//input[@placeholder='Password']"
    Click_Login_Button_Xpath = "//button[@type='submit']"
    Click_menu_Button_Xpath = "//img[@class='oxd-userdropdown-img']"
    Click_Logout_Xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=0.5)

    def Enter_Username(self, username):
        self.driver.find_element(By.XPATH, self.Text_Username_Xpath).send_keys(username)

    def Enter_Password(self, password):
        self.driver.find_element(By.XPATH, self.Text_Password_Xpath).send_keys(password)

    def Click_Login(self):
        self.driver.find_element(By.XPATH, self.Click_Login_Button_Xpath).click()

    def Click_Menu_Button(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.Click_menu_Button_Xpath)))
            self.driver.find_element(By.XPATH, self.Click_menu_Button_Xpath).click()
        except:
            pass

    def Click_Logout(self):
        self.driver.find_element(By.XPATH, self.Click_Logout_Xpath).click()

    def Validate_Login_Status(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.Click_menu_Button_Xpath)))
            return "login pass"
        except:
            return "login fail"
