# -*- coding: utf-8 -*-
# @Time : 2021/12/15 20:39
# @Author : shelly
# @File : test_login.py
# @Desc :
import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pageobjects.pagelogin import Loginpage
from config.config import url,driver_path,data_file,sheet
from data.read_write import ReadWrite
from log.log import logger

class TestCases(unittest.TestCase):
    def setUp(self):
        print("打开浏览器")
        s = Service(driver_path)
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        self.driver.get(url)
        self.page=Loginpage(self.driver)
        self.open=ReadWrite(data_file,sheet)

    def tearDown(self):
        print("关闭浏览器")
        self.driver.quit()
#测试用例1
    def test_login_success(self):
        '''成功登录'''
        data_list=self.open.Read()
        self.page.type_username(data_list[0][0])
        self.page.type_password(data_list[0][1])
        self.page.type_login()
        # self.driver.find_element(By.ID, "account").send_keys("shelly")
        # self.driver.find_element(By.NAME, "password").send_keys("p@ssw0rd")
        # self.driver.find_element(By.ID, "submit").click()
        time.sleep(2)
        try:
            assert self.driver.title == "我的地盘 - 禅道"
            logger.info("验证登录成功测试的信息")
            print("验证登录成功测试----passed")

        except:
            print("验证登录成功测试----failed")


    def test_login_false(self):
        '''密码错误登录失败'''
        data_list = self.open.Read()
        self.page.type_username(data_list[1][0])
        self.page.type_password(data_list[1][1])
        self.page.type_login()
        # self.driver.find_element(By.ID, "account").send_keys("shelly")
        # self.driver.find_element(By.NAME, "password").send_keys("123456")
        # self.driver.find_element(By.ID, "submit").click()
        time.sleep(2)
        try:

            self.assertEqual(self.driver.title,"我的地盘 - 禅道")
            print("验证密码错误登录失败测试----failed")
        except:
            print("验证密码错误登录失败测试----passed")
        # try:
        #     assert self.driver.title != "我的地盘 - 禅道"
        #     print("验证密码错误登录失败测试----passed")
        # except:
        #     print("验证密码错误登录失败测试----failed")



    def test_login_false2(self):
        '''账号错误登录失败'''
        data_list = self.open.Read()
        self.page.type_username(data_list[2][0])
        self.page.type_password(data_list[2][1])
        self.page.type_password("p@ssw0rd")
        self.page.type_login()
        time.sleep(2)
        try:
            self.assertEqual(self.driver.title,"我的地盘 - 禅道")
            print("验证账号错误登录失败测试----failed")
        except:
            print("验证账号错误登录失败测试----passed")
        # try:
        #     assert self.driver.title != "我的地盘 - 禅道"
        #     print("验证账号错误登录失败测试----passed")
        # except:
        #     print("验证账号错误登录失败测试----failed")


if __name__=="__main__":
    # unittest.main()
    suite=unittest.TestSuite()
    # suite.addTest(TestCases("test_adduser"))
    # suite.addTest(TestCases("test_showuser"))
    # suite.addTest(TestCases("test_updateuser"))
    # suite.addTest(TestCases("test_deleteuser"))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCases))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCases))
    test_runner=unittest.TextTestRunner()
    test_runner.run(suite)