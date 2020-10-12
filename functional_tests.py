# author: wemo  time:2020/10/12

from selenium import webdriver

browser = webdriver.Firefox(executable_path=r"D:\webDrivers\geckodriver.exe")
browser.get('http://localhost:8000')
assert 'Django' in browser.title


