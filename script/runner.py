# -*- coding: utf-8 -*-
# @Time : 2021/12/15 20:43
# @Author : shelly
# @File : runner.py.py
# @Desc :
import unittest
from BeautifulReport import BeautifulReport


#加载准备好的测试用例
cases=unittest.defaultTestLoader.discover(start_dir=r"E:\slftest1\script\testcases", pattern='test*.py')
#执行测试用例
result=BeautifulReport(cases)
#生成测试报告
result.report(description="系统用户的测试报告", filename="SIT测试报告2", report_dir=r"E:\slftest1\script\report")