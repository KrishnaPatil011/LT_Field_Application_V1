from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    userid_xpath="//input[@type='text'][1]"
    password_xpath="//input[@type='password'][1]"
    loginbutton_xapth="//button[@type='submit'][1]"




    def __init__(self,driver):
        self.driver=driver


    def Enteruserid(self,user):
        self.driver.find_element(By.XPATH,self.userid_xpath).send_keys(user)


    def Enterpassword(self,pwd):
        self.driver.find_element(By.XPATH,self.password_xpath).send_keys(pwd)


    def Clickonlogin(self):
       self.driver.find_element(By.XPATH,self.loginbutton_xapth).click()















