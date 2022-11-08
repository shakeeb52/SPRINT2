import logging
import time

import allure
from allure_commons._allure import severity
from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Utilities import configreader
from Utilities.LogUtil import Logger

from features.pageobjects.LoginPage import LoginPage
from features.pageobjects.Search import Search

log = Logger(__name__, logging.INFO)


@Given(u'we navigate to flipkart homepage')
def step_imp1(context):
    context.reg = LoginPage(context.driver)
    context.reg.open(configreader.ConfigReader("base info", "URL"))
    log.logger.info("Navigate to Flipkart Homepage")
    context.reg.clickclose()
    log.logger.info("Close button clicked")


# @Then(u'we click on close button')
# def step_imp1(context):
#    context.reg.clickclose()
#   log.logger.info("Close button clicked")


@When(u'we click on the login button')
def step_imp1(context):
    context.reg.clicklogin()
    log.logger.info("Login button clicked")


@Then(u'we type in the "{username}" edit box')
def step_imp1(context, username):
    context.reg.setusername(username)
    log.logger.info("Username field typed")


@Then(u'we type in the "{password}" field')
def step_imp1(context, password):
    context.reg.setpassword(password)
    log.logger.info("Password field typed")


@Then(u'we click on the sign in button')
def step_imp1(context):
    context.reg.clicksignin()
    log.logger.info("Sign IN BUTTON CLICKED")


@then(u'type "{searchTEXT}" in search bar')
def step_imp2(context, searchTEXT):
    context.sea = Search(context.driver)
    context.sea.text_Searchbar(searchTEXT)


@then(u'Click on search button')
def step_imp2(context):
    context.sea.Click_SEARCHBUTTON()


@then(u'Check on Relevance is clickable')
def step_imp2(context):
    context.sea.Check_Relevance()


@then(u'Check on popularity is clickable')
def step_imp2(context):
    context.sea.Check_POPULARITY()


@then(u'Check on Price low-high is clickable')
def step_imp2(context):
    context.sea.Check_LOWTOHIGH()


@then(u'Check on Price high-low is clickable')
def step_imp2(context):
    context.sea.Check_HIGHTOLOW()


@then(u'Check on newest first is clickable')
def step_imp2(context):
    context.sea.Check_NEWESTFIRST()


@then(u'we validate filter text is present or not')
def step_imp2(context):
    context.sea.validFilter("Filters")


@then(u'select the dropdown')
def step_imp2(context):
    context.sea.dropdown()


@then(u'type "{brand}" in the search bar')
def step_imp2(context, brand):
    context.sea.brandsearch(brand)


@then(u'click on the checkbox')
def step_imp2(context):
    context.sea.brandcheck()


@then(u'click on the assured checkbox')
def step_imp2(context):
    context.sea.assured()


# @then(u'click on the checkbox')
# def step_imp2(context):
# context.sea.checkbox()

@then(u'Click on ratings checkbox 4* above and 3* above')
def step_imp2(context):
    context.sea.ratings()


@then(u'Open GST link')
def step_imp2(context):
    context.sea.checkbox()


@then(u'ram checkbox clicked')
def step_imp2(context):
    context.sea.ram()


@then(u'internal storage checkbox clicked')
def step_imp2(context):
    context.sea.int()


@then(u'battery link is opened')
def step_imp2(context):
    context.sea.batt()


@then(u'Get the first element on the page')
def step_imp2(context):
    context.sea.product()
