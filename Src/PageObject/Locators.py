# Author:   Rachman Walker
# Date:     March 15, 2021
# Filename: Locators.py
"""
Purpose: Add element locators for the various objects, which, in this
case, are located on the Selenium test page at https://the-internet.herokuapp.com/
"""


class Locators(object):
    # Dropdown list url and locators
    dropdown_list_url = "https://the-internet.herokuapp.com/dropdown"
    dropdown_list = "//*[@id='dropdown']"
    dropdown_option_1 = "//option[text()='Option 1']"
    dropdown_option_2 = "//option[text()='Option 2']"
