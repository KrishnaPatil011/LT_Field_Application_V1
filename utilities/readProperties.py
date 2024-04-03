import configparser
import os.path

config=configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+"\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=(config.get('commonInfo','baseurl'))
        return url

    @staticmethod
    def getUserId():
        Userid = (config.get('commonInfo', 'userid'))
        return Userid

    @staticmethod
    def getPassword():
        password = (config.get('commonInfo', 'password'))
        return password