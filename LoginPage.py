from seleniumpagefactory.Pagefactory import PageFactory
from selenium import webdriver

class LoginPage(PageFactory):

    def __init__(self, driver: webdriver):
        self.driver = driver

    locators = {
        "inptLogin": ('XPATH', '/html/body/div/div/div/section/form/div[1]/input'),
        "inptPassword": ('XPATH', '/html/body/div/div/div/section/form/div[2]/input'),
        "btnLogin": ('ID', 'login-btn')
    }

    def login(self):
        self.inptLogin.set_text("allan.neri")
        self.inptPassword.set_text("allan@mudar")
        self.btnLogin.click_button()

