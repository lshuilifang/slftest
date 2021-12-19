'''
@File:slftest.py
@DateTime:2021/11/22
@Author:sunlufan
@Desc:
'''

from selenium.webdriver.common.by import By
import win32gui
import win32con

class addbug:
    def __init__(self,driver):
        self.account=By.ID,"account"
        self.password=By.NAME,"password"
        self.submit=By.ID,"submit"
        self.exit=By.XPATH,"//a[@class='dropdown-toggle']/span[1]"
        self.acceptEx=By.LINK_TEXT,"退出"
        self.testButton=By.LINK_TEXT,"测试"
        self.testButton2=By.XPATH,"//nav[@id='subNavbar']/ul/li[1]/a"
        self.addBug=By.LINK_TEXT,"提Bug"
        self.class1=By.CLASS_NAME,"search-field"
        self.class2=By.CLASS_NAME,"active-result"
        self.title=By.ID,"title"
        self.openfile1=By.XPATH,"//tbody/tr[10]/td[1]/div[1]/div[1]/div[1]/button[1]"
        self.driver=driver
        self.save=By.ID,"submit"



    def openfile(self):
        self.dialog = win32gui.FindWindow("#32770", "打开")
        #
        self.ComboBoxEx32 = win32gui.FindWindowEx(self.dialog, 0, "ComboBoxEx32", None)  # 二级
        self.comboBox = win32gui.FindWindowEx(self.ComboBoxEx32, 0, "ComboBox", None)  # 三级
        # 编辑按钮
        self.edit = win32gui.FindWindowEx(self.comboBox, 0, 'Edit', None)  # 四级
        # 打开按钮
        self.button = win32gui.FindWindowEx(self.dialog, 0, 'Button', "打开(&O)")  # 二级
        # 往编辑当中，输入文件路径 。
        win32gui.SendMessage(self.edit, win32con.WM_SETTEXT, None, r"C:\Users\slfpa\Desktop\mine\1.jpg")  # 发送文件路径
        win32gui.SendMessage(self.dialog, win32con.WM_COMMAND, 1, self.button)  # 点击打开按钮


    def click1(self):
        self.driver.find_element(*self.testButton).click()
        self.driver.find_element(*self.testButton2).click()
        self.driver.find_element(*self.addBug).click()
        self.driver.find_element(*self.class1).click()
        self.driver.find_element(*self.class2).click()

    def imputtitle(self,content):
        self.driver.find_element(*self.title).send_keys(content)

    def scroll(self):
        js="var q=document.documentElement.scrollTop=1000"
        self.driver.execute_script(js)

    def open_File(self):
        self.driver.find_element(*self.openfile1).click()

    def Save(self):
        self.driver.find_element(*self.save).click()




