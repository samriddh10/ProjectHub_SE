# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestT1():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_t1(self):
    # Test name: T1
    # Step # | name | target | value
    # 1 | open | http://127.0.0.1:5503/SElogin.html | 
    self.driver.get("http://127.0.0.1:5503/SElogin.html")
    # 2 | setWindowSize | 1050x590 | 
    self.driver.set_window_size(1050, 590)
    # 3 | click | css=.userid | 
    self.driver.find_element(By.CSS_SELECTOR, ".userid").click()
    # 4 | type | css=.userid | sam
    self.driver.find_element(By.CSS_SELECTOR, ".userid").send_keys("sam")
    # 5 | click | css=.password | 
    self.driver.find_element(By.CSS_SELECTOR, ".password").click()
    # 6 | type | css=.password | abcd
    self.driver.find_element(By.CSS_SELECTOR, ".password").send_keys("abcd")
    # 7 | click | css=.login-button | 
    self.driver.find_element(By.CSS_SELECTOR, ".login-button").click()
    # 8 | click | css=.sidebar-link:nth-child(1) > img | 
    self.driver.find_element(By.CSS_SELECTOR, ".sidebar-link:nth-child(1) > img").click()
    # 9 | click | css=.sidebar-link:nth-child(2) > img | 
    self.driver.find_element(By.CSS_SELECTOR, ".sidebar-link:nth-child(2) > img").click()
    # 10 | click | css=.sidebar-link:nth-child(3) > div | 
    self.driver.find_element(By.CSS_SELECTOR, ".sidebar-link:nth-child(3) > div").click()
    # 11 | click | css=.sidebar-link:nth-child(4) > div | 
    self.driver.find_element(By.CSS_SELECTOR, ".sidebar-link:nth-child(4) > div").click()
    # 12 | click | css=.sidebar-link:nth-child(5) > div | 
    self.driver.find_element(By.CSS_SELECTOR, ".sidebar-link:nth-child(5) > div").click()
    # 13 | click | css=.left | 
    self.driver.find_element(By.CSS_SELECTOR, ".left").click()
    # 14 | click | css=.search | 
    self.driver.find_element(By.CSS_SELECTOR, ".search").click()
  
