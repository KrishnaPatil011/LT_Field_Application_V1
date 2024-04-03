from selenium.webdriver.common.by import By


class MyAccountPage:
    logout_xpath="//button[text()='Log Out']"





    def __init__(self,driver):
        self.driver=driver


    def logout(self):
        self.driver.find_element(By.XPATH,self.logout_xpath).click()

