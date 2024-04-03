from selenium import webdriver
from selenium.webdriver.common.by import By


class Home:

    macid_xpath="//input[@name='macID']"
    selectdropdown_xpath="//button[@type='button']"
    dev_xpath="//span[text()='Dev']"
    preprod_xpath="//span[text()='Pre Production']"
    prod_xpath="//span[text()='Production']"
    connectbutton_xpath = "//button[text()='Connect']"


    def __init__(self,driver):
        self.driver=driver

    def Enter_macid(self,macid):
        self.driver.find_element(By.XPATH,self.macid_xpath).send_keys(macid)


    def Click_on_dropdown(self):
        self.driver.find_element(By.XPATH,self.selectdropdown_xpath).click()

    def select_environment(self):
        self.driver.find_element(By.XPATH,self.prod_xpath).click()


    def click_on_connect(self):
        self.driver.find_element(By.XPATH,self.connectbutton_xpath).click()












