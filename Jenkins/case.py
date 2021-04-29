# #八大定位方式——通过xpath绝对路径定位控件
from selenium import webdriver
import time
drive = webdriver.Chrome()
drive.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
drive.find_element_by_xpath('html/body/div/div/div/div/form/input[1]').send_keys('王麻子')



# #八大定位方式——通过xpath相对路径定位控件
# from selenium import webdriver
# import time
# drive = webdriver.Chrome()
# drive.get('http://101.133.169.100/yuns/index.php')
# time.sleep(3)
# drive.find_element_by_xpath("//input[@class='but1']").send_keys('王麻子')