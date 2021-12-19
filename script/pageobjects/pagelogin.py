'''
@File:slftest.py
@DateTime:2021/11/22
@Author:sunlufan
@Desc:
'''

from selenium.webdriver.common.by import By

class Loginpage:
    def __init__(self,driver):
        self.account=By.ID,"account"
        self.password=By.NAME,"password"
        self.submit=By.ID,"submit"
        self.driver=driver

    def type_username(self,username):
        self.driver.find_element(*self.account).send_keys(username)

    def type_password(self,userpassword):
        self.driver.find_element(*self.password).send_keys(userpassword)

    def type_login(self):
        self.driver.find_element(*self.submit).click()