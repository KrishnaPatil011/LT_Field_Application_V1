
import os
from datetime import datetime

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        driver=webdriver.Edge(EdgeChromiumDriverManager().install())

    elif browser=='firefox':
        webdriver.Firefox(GeckoDriverManager().install())

    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())

    return driver


def pytest_addoption(parser):  # This will get value from CLI
        parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")



########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'LTconf'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester'] = 'Krishna'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"
