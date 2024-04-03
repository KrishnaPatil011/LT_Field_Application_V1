import os.path
import time

import pytest

from pageObjects.login import Login
from pageObjects.Home import Home
from utilities.customlogger import LogGen
from utilities.readProperties import ReadConfig


class Test_Login:
    # baseurl="https://ltconfigweb.beta.livingthings.in/login"
    baseurl=ReadConfig.getApplicationURL()
    # logger=LogGen.loggen()           #For logging

    @pytest.mark.sanity
    @pytest.mark.parametrize('user,pwd,mac', [("7410162452", "Ayush2511", "C8:F0:9E:29:41:31")])

    # ("74101624521", "Ayush2511", "C8:F0:9E:29:41:31"), ("7410162452", "Ayush2511", "C8:F0:9E:29:41")


    def test_login(self,user,pwd,mac,setup):
        self.logger.info("****_Login_Test_Started_***")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.lgn=Login(self.driver)
        self.lgn.Enteruserid(user)
        self.lgn.Enterpassword(pwd)
        self.lgn.Clickonlogin()
        time.sleep(10)
        try:
            self.logger.info("****_HomePage_Test_Started_***")
            time.sleep(5)
            self.act_url1 = self.driver.current_url
            # self.hp=Home(self.driver)
            # time.sleep(5)
            # self.hp.Enter_macid(mac)
            # time.sleep(5)
            # self.hp.Click_on_dropdown()
            # self.hp.select_environment()
            # self.hp.click_on_connect()
            # time.sleep(5)
            # self.act_url2 = self.driver.current_url
            self.driver.close()
            assert self.act_url1 == "https://ltconfigweb.beta.livingthings.in/"
            # assert self.act_url2 == "https://ltconfigweb.beta.livingthings.in/device"

        except:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_login.png")
            self.driver.close()
            assert False


        self.logger.info("****_Login_Test_Finished***")











