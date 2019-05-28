from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()     #声明浏览器
try:
     browser.get('https://taobao.com')
     browser.get('https://baidu.com')  #请求网页
     input = browser.find_element_by_id('kw') #根据id获取节点
     input.send_keys('秦时明月')   #输入文字
     time.sleep(2)   #停顿2秒
     input.clear()   #清空文字
     input.send_keys('Python')  #重新搜索
     input.send_keys(Keys.ENTER)   #搜索

     #time.sleep(2)
     #browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')  #下拉到底下
     #browser.execute_script('alert("To Bottom")')  #弹出提示框
     
     wait = WebDriverWait(browser,10)  #指定最长等待时间，之后调用unil(),传入等待条件。
     wait.until(EC.presence_of_element_located((By.ID,'content_left')))  #ID为content_left的节点搜索框，
     print(browser.current_url)
     print(browser.get_cookies())
     #print(browser.page_source) #获取网页源代码
finally:
     time.sleep(5)
     browser.close()
