import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup






def selenium():


    headers={
        # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    }
    url = "http://sdcs.sysu.edu.cn/research/activity"
    # url = "http://www.baidu.com"


    # html_doc = requests.get(url, headers=headers)
    # print(html_doc)

    options = webdriver.ChromeOptions()
    # options.add_argument('--remote-debugging-port=9222')
    # options.add_argument("--disable-extensions")
    # options.add_experimental_option("debuggerAddress","127.0.0.1:9222")

    # options.add_argument('--no-sandbox')
    # options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    

    


    browser = webdriver.Chrome(executable_path='chromedriver',chrome_options = options)
    browser.get(url)
    
    time.sleep(3)
    

    print(browser.page_source)
    
    
    elems_li = browser.find_elements_by_css_selector('li')
    print()
    

    # soup = BeautifulSoup(html_doc, 'html.parser')


if __name__ == "__main__":
    selenium()
