# Author:   Rachman Walker
# Date:     March 15, 2021
# Filename: HomePage.py
"""
Purpose: Add the links (to the functionality) found on https://the-internet.herokuapp.com/
"""
from selenium.webdriver.common.by import By
from Src.PageObject.Locators import Locators


class HomePage(object):
    # Home page url
    app_url = "https://the-internet.herokuapp.com/"
