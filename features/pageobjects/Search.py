import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import action_chains
from selenium.webdriver.common import actions

from Utilities import configreader
from features.pageobjects.Base import BaseSettingsPage


class Search(BaseSettingsPage):

    def __init__(self, driver):
        super().__init__(driver)

    def text_Searchbar(self, searchTEXT):
        WebDriverWait(self.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")))

        self.DynamicImplicitWait(40)
        self.TypeEditBox("SEARCHBAR_XPATH", searchTEXT)
        time.sleep(5)

    def Click_SEARCHBUTTON(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("SEARCHBUTTON_XPATH")
        time.sleep(5)

    def Check_Relevance(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("RELAVENCE_XPATH")
        time.sleep(5)

    def Check_POPULARITY(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("POPULARITY_XPATH")
        time.sleep(5)

    def Check_LOWTOHIGH(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("LOWTOHIGH_XPATH")
        time.sleep(5)

    def Check_HIGHTOLOW(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("HIGHTOLOW_XPATH")
        time.sleep(5)

    def Check_NEWESTFIRST(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("NEWESTFIRST_XPATH")
        time.sleep(5)

    def validFilter(self, expectedtext):
        self.DynamicImplicitWait(40)
        self.AssertText("filter_XPATH", expectedtext)
        time.sleep(5)

    def dropdown(self):
        drop = Select(self.driver.find_element(By.XPATH,
                                               "//*[@id='container']/div/div[3]/div/div[1]/div/div[1]/div/section[2]/div[4]/div[1]/select"))
        drop.select_by_index(1)
        time.sleep(3)
        drop = Select(self.driver.find_element(By.XPATH,
                                               "//*[@id='container']/div/div[3]/div/div[1]/div/div[1]/div/section[2]/div[4]/div[3]/select"))
        drop.select_by_index(1)
        time.sleep(3)

    def brandsearch(self, brand):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("brand_XPATH", brand)
        time.sleep(5)

    def brandcheck(self):
        self.DynamicImplicitWait(40)
        self.ClickCheckbox("brandcheck_XPATH")
        time.sleep(5)

    def assured(self):
        self.DynamicImplicitWait(40)
        self.ClickCheckbox("assured_XPATH")
        time.sleep(10)

    def ratings(self):
        self.DynamicImplicitWait(40)
        self.driver.execute_script("window.scrollBy(0,400)")
        self.ClickCheckbox("ratings4_XPATH")
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,400)")
        self.DynamicImplicitWait(40)
        self.ClickCheckbox("ratings3_XPATH")
        time.sleep(5)

    # def checkbox(self):
    #   self.DynamicImplicitWait(40)
    #    checkboxes = self.driver.find_elements(By.CLASS_NAME, "//input[@type='checkbox']")

    def checkbox(self):
        self.DynamicImplicitWait(40)
        self.driver.execute_script("window.scrollBy(0,500)")
        self.ClickLinks("GSTO_XPATH")
        time.sleep(5)
        self.ClickCheckbox("gst_XPATH")
        time.sleep(5)

    def ram(self):
        self.DynamicImplicitWait(40)
        self.driver.execute_script("window.scrollBy(0,500)")
        self.ClickCheckbox("ram4_XPATH")
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,500)")
        self.DynamicImplicitWait(40)
        self.ClickCheckbox("ram3_XPATH")
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,500)")
        self.DynamicImplicitWait(40)
        self.ClickCheckbox("ram6_XPATH")
        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(5)
        self.DynamicImplicitWait(40)
        self.ClickCheckbox("ram8_XPATH")
        time.sleep(5)

    def ram(self):
        self.DynamicImplicitWait(40)
        self.driver.execute_script("window.scrollBy(0,500)")
        self.ClickCheckbox("ram4_XPATH")
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,500)")
        self.DynamicImplicitWait(40)
        self.ClickCheckbox("ram3_XPATH")
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,500)")
        self.DynamicImplicitWait(40)
        self.ClickCheckbox("ram6_XPATH")
        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(5)
        self.DynamicImplicitWait(40)
        self.ClickCheckbox("ram8_XPATH")
        time.sleep(5)

    def int(self):
        self.driver.execute_script("window.scrollBy(0,600)")
        self.DynamicImplicitWait(40)
        self.ClickLinks("INT_XPATH")
        time.sleep(5)
        self.DynamicImplicitWait(40)
        self.ClickCheckbox("INT128_XPATH")
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,600)")
        self.ClickLinks("INT_XPATH")
        time.sleep(5)
        self.DynamicImplicitWait(40)
        self.ClickCheckbox("INT64_XPATH")
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,600)")
        self.ClickLinks("INT_XPATH")
        time.sleep(5)
        self.DynamicImplicitWait(40)
        self.ClickCheckbox("INT32_XPATH")
        time.sleep(5)

    def batt(self):
        self.driver.execute_script("window.scrollBy(0,600)")
        self.DynamicImplicitWait(40)
        self.ClickLinks("BATT_XPATH")
        time.sleep(5)
        self.DynamicImplicitWait(40)
        self.ClickCheckbox("BATT3000_XPATH")
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,600)")
        self.DynamicImplicitWait(40)
        self.ClickLinks("BATT_XPATH")
        time.sleep(5)
        self.DynamicImplicitWait(40)
        self.ClickCheckbox("BATT4000_XPATH")
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,600)")
        self.DynamicImplicitWait(40)
        self.ClickLinks("BATT_XPATH")
        time.sleep(5)
        self.DynamicImplicitWait(40)
        self.ClickCheckbox("BATT6000_XPATH")
        time.sleep(5)

    def product(self):
        self.driver.execute_script("window.scrollBy(0,-600)")
        self.DynamicImplicitWait(40)
        self.ClickLinks("product_XPATH")
        time.sleep(5)