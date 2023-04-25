
import random
from time import sleep
from lxml import html
from my_fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


etree = html.etree

chrome_option = Options()
chrome_option.add_argument('--headless')
chrome_option.add_argument('--disable-gpu')
while True:
    ua = UserAgent(family='chrome')
    #请求头自动随机获取
    user_agent = ua.random()
    headers1 = {"User-Agent":  user_agent}
    url = 'https://www.wjx.cn/vm/wOHv78v.aspx'
    # referer = 'https://www.csdn.net/'
    #driver_path = 'chromedriver.exe'
    s = Service('chromedriver.exe')
    opt = webdriver.ChromeOptions()
    #代理ip伪装，如果要伪装ip需要先找到一个能用的高匿名代理IP，否则页面打不开
    opt.add_argument('--proxy-server=http://170.244.27.242')
    opt.add_experimental_option('excludeSwitches', ['enable-automation'])
    opt.add_experimental_option('useAutomationExtension', False)
    opt.add_argument('--user-agent=%s' % user_agent)
    opt.add_argument('--headers=%s' % headers1)
    # opt.add_argument('--referer=%s' % referer)
    # opt.add_argument('--user-agent=%s' % cookie)
    # 实现无可视化界面
    # opt.add_argument('--headless')
    # opt.add_argument('--disable-gpu')
    # 实现规避检测
    opt.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(service=s)
    browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                               {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})

    #根据问卷设置自动填写样式
    browser.get(url)
    logo = browser.find_element(By.XPATH,'//*[@id="q1"]').send_keys("杨明")
    browser.find_element(By.XPATH,'//*[@id="q2"]').send_keys("2100013157")
    browser.find_element(By.XPATH,'//*[@id="q3"]').send_keys("信科")
    browser.find_element(By.XPATH,'//*[@id="q4"]').send_keys("18811726567")
    #while i <= 14:
        #c = random.randint(1, 2);
        #c1 = '//*[@id="divquestion' + str(i) + '"]/ul/li[' + str(c) + ']/label'
        #browser.find_element_by_xpath(c1).click()
        #i = i + 1
    browser.find_element(By.XPATH,'//*[@id="divSubmit"]').click()
    sleep(1)
    browser.find_element(By.XPATH,'//*[@id="layui-layer1"]/div[3]/a').click()
    browser.find_element(By.XPATH,'//*[@id="captchaWrap"]').click()
    sleep(5)



