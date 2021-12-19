# -*- coding: utf-8 -*-
# @Time : 2021/12/15 22:01
# @Author : shelly
# @File : test_bug.py
# @Desc :
import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
import win32con
import win32gui
from config.config import driver_path,url
from pageobjects.pageaddbug import addbug
from pageobjects.pagelogin import Loginpage

class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("打开浏览器")
        s = Service(driver_path)
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.maximize_window()
        cls.driver.get(url)

    @classmethod
    # def tearDownClass(cls):
    #     print("关闭浏览器")
    #     cls.driver.quit()

    def setUp(self):
        self.page1=Loginpage(self.driver)
        print("登录")
        self.page1.type_username("shelly")
        self.page1.type_password("p@ssw0rd")
        self.page1.type_login()
        # self.driver.find_element(By.ID, "account").send_keys("shelly")
        # self.driver.find_element(By.NAME, "password").send_keys("p@ssw0rd")
        # self.driver.find_element(By.ID, "submit").click()
        sleep(2)

    # def tearDown(self):
    #     print("退出系统")
    #     self.driver.find_element(By.XPATH, "//a[@class='dropdown-toggle']/span[1]").click()
    #     self.driver.find_element(By.LINK_TEXT, "退出").click()
#测试用例1
    def test_1_addbug_success(self):
        '''成功添加bug'''
        self.page2=addbug(self.driver)
        sleep(3)
        self.page2.click1()
        self.page2.imputtitle("slfbug")
        sleep(2)
        self.page2.scroll()
        sleep(1)
        self.page2.open_File()
        self.openfile()
        # self.page2.Save()
        # self.driver.find_element(By.LINK_TEXT, "测试").click()
        # self.driver.find_element(By.XPATH, "//nav[@id='subNavbar']/ul/li[1]/a").click()
        # self.driver.find_element(By.LINK_TEXT, "提Bug").click()
        # self.driver.find_element(By.CLASS_NAME, "search-field").click()
        # self.driver.find_element(By.CLASS_NAME, "active-result").click()
        # self.driver.find_element(By.ID, 'title').send_keys("slfbug")
        # sleep(2)
        # js = "var q=document.documentElement.scrollTop=1000"
        # self.driver.execute_script(js)
        # sleep(1)
        # self.driver.find_element(By.XPATH, "//tbody/tr[10]/td[1]/div[1]/div[1]/div[1]/button[1]").click()
        # sleep(2)
        # dialog = win32gui.FindWindow("#32770", "打开")
        # #
        # ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
        # comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
        # # 编辑按钮
        # edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
        # # 打开按钮
        # button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")  # 二级
        # # 往编辑当中，输入文件路径 。
        # win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, r"C:\Users\slfpa\Desktop\mine\1.jpg")  # 发送文件路径
        # win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
        # self.driver.find_element(By.ID,"submit").click()
        # # sleep(2)
        # # print(self.driver.find_element(By.LINK_TEXT, "提Bug").text)
        # sleep(3)
        # try:
        #     self.assertEqual(self.driver.find_element(By.LINK_TEXT,"提Bug").text,"提Bug")
        #     print("创建bug成功")
        # except:
        #     print("添加bug失败")

    # def test_2_solvebug(self):
    #     '''解决Bug成功'''
    #     sleep(1)
    #     self.driver.find_element(By.LINK_TEXT, "测试").click()
    #     self.driver.find_element(By.XPATH, "//nav[@id='subNavbar']/ul/li[1]/a").click()
    #     # self.driver.find_element(By.XPATH,"//tbody/tr[1]/td[11]/a[2]/i[1]").click()
    #     self.driver.find_element(By.XPATH,"//td[@class='c-actions']/a[2]/i[1]").click()
    #     sleep(2)
    #     self.driver.switch_to.frame("iframe-triggerModal")
    #     self.driver.find_element(By.XPATH,"//tbody/tr[1]/td[1]/div[1]/a[1]/span[1]").click()
    #     sleep(1)
    #     self.driver.find_element(By.XPATH,"//tbody/tr[1]/td[1]/div[1]/div[1]/ul[1]/li[4]").click()
    #
    #     self.driver.find_element(By.XPATH,"//td[@class='required']/div[1]/div[1]/a[1]").click()
    #     self.driver.find_element(By.XPATH,"//tbody/tr[3]/td[2]/div[1]/div[1]/div[1]/ul[1]/li[1]").click()
    #     self.driver.find_element(By.ID,"submit").click()
    #     self.driver.switch_to.default_content()
    #     sleep(2)
    #     try:
    #         self.assertEqual(self.driver.find_element(By.LINK_TEXT, "提Bug").text, "提Bug")
    #         print("解决bug成功")
    #
    #     except:
    #          print("解决bug失败")
    #
    # def test_3_offbug(self):
    #     '''关闭Bug成功'''
    #     sleep(1)
    #     self.driver.find_element(By.LINK_TEXT, "测试").click()
    #     self.driver.find_element(By.XPATH, "//nav[@id='subNavbar']/ul/li[1]/a").click()
    #     # self.driver.find_element(By.XPATH,"//tbody/tr[1]/td[11]/a[1]/i[1]").click()
    #
    #     self.driver.find_element(By.XPATH,"//a[@class='btn iframe']/i[1]").click()
    #     self.driver.switch_to.frame("iframe-triggerModal")
    #     sleep(1)
    #     self.driver.find_element(By.ID,"submit").click()
    #     self.driver.switch_to.default_content()
    #     sleep(1)
    #     try:
    #         self.assertEqual(self.driver.find_element(By.LINK_TEXT, "提Bug").text, "提Bug")
    #         print("关闭bug成功")
    #
    #     except:
    #          print("关闭bug失败")



if __name__=="__main__":
    suit=unittest.TestSuite()
    suit.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCases))
    # suit.addTest(TestCases("test_1_addbug_success"))
    # suit.addTest(TestCases("test_2_solvebug"))
    # suit.addTest(TestCases("test_3_offbug"))
    test_runner=unittest.TextTestRunner()
    test_runner.run(suit)

