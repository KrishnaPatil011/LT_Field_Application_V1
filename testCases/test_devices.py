import os.path
import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from pageObjects.login import Login
from pageObjects.Home import Home
from utilities.customlogger import LogGen
from utilities.readProperties import ReadConfig


class Test_devices:
    # baseurl="https://ltconfigweb.beta.livingthings.in/login"
    baseurl=ReadConfig.getApplicationURL()
    # logger=LogGen.loggen()           #For logging

    # @pytest.mark.regression


    @pytest.mark.parametrize('user,pwd,mac', [("7410162452", "Ayush2511", "80:64:6F:3F:2E:11")])

    # ("74101624521", "Ayush2511", "C8:F0:9E:29:41:31"), ("7410162452", "Ayush2511", "C8:F0:9E:29:41")


    def test_home(self,user,pwd,mac,setup):
        # self.logger.info("****_Login_Test_Started_***")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.lgn=Login(self.driver)
        self.lgn.Enteruserid(user)
        self.lgn.Enterpassword(pwd)
        self.lgn.Clickonlogin()
        time.sleep(5)
        # self.logger.info("****_HomePage_Test_Started_***")
        # time.sleep(5)
        self.act_url1 = self.driver.current_url
        self.hp=Home(self.driver)
        # time.sleep(5)
        self.hp.Enter_macid(mac)
        # time.sleep(5)
        self.hp.Click_on_dropdown()
        self.hp.select_environment()
        self.hp.click_on_connect()
        # time.sleep(5)
        self.act_url2 = self.driver.current_url
        try:
            time.sleep(5)
            self.data_ac=self.driver.find_element(By.XPATH,"//td[text()='DATA_AC']").is_displayed()
            print(self.data_ac)
            time.sleep(5)
            # self.driver.find_element(By.XPATH,"//button[text()='Restart Device']").click()
            # time.sleep(5)
            # self.do= self.driver.find_element(By.XPATH, "//td[text()='DO']").is_displayed()
            # print(self.do)
            self.driver.close()
            assert self.data_ac==True
            # assert self.do==True

        # assert self.act_url1 == "https://ltconfigweb.beta.livingthings.in/"
        # assert self.act_url2 == "https://ltconfigweb.beta.livingthings.in/device

        except:
            allure.attach(self.driver.get_screenshot_as_png(),name="Test_Login",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_login.png")
            self.driver.close()
            assert False
        #
        #
        # self.logger.info("****_Login_Test_Finished***")










