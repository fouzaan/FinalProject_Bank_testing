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

class TestBalanceenquiry():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login_and_blank_error(self):
    self.driver.get("https://demo.guru99.com/V4/")
    self.driver.find_element(By.NAME, "uid").send_keys("mngr492649")
    self.driver.find_element(By.NAME, "password").send_keys("anyguqE")
    self.driver.find_element(By.NAME, "btnLogin").click()
    self.driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()
    self.driver.find_element(By.NAME, "accountno").click()
    self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
    assert self.driver.find_element(By.ID, "message2").text == "Account Number must not be blank"

  def test_char_error(self):
    self.driver.get("https://demo.guru99.com/V4/manager/BalEnqInput.php")
    self.driver.find_element(By.NAME, "accountno").send_keys("1234Acc123")
    self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
    assert self.driver.find_element(By.ID, "message2").text == "Characters are not allowed"

  def test_special_error(self):
    self.driver.get("https://demo.guru99.com/V4/manager/BalEnqInput.php")
    self.driver.find_element(By.NAME, "accountno").send_keys("123!@#\\n!@#")
    self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
    assert self.driver.find_element(By.ID, "message2").text == "Special characters are not allowed"

  def test_space_error(self):
    self.driver.get("https://demo.guru99.com/V4/manager/BalEnqInput.php")
    self.driver.find_element(By.NAME, "accountno").click()
    self.driver.find_element(By.NAME, "accountno").send_keys(Keys.SPACE)
    self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
    assert self.driver.find_element(By.ID, "message2").text == "First character cannot have space"
    #assert self.driver.find_element(By.ID, "message2").text == "Characters are not allowed"

  def test_valid_account_no(self):
    self.driver.get("https://demo.guru99.com/V4/manager/BalEnqInput.php")
    self.driver.find_element(By.NAME, "accountno").send_keys("121482")
    self.driver.find_element(By.NAME, "accountno").send_keys(Keys.ENTER)
    assert self.driver.find_element(By.CSS_SELECTOR, "table").is_displayed()

  def test_invalid_account_no(self):
    self.driver.get("https://demo.guru99.com/V4/manager/BalEnqInput.php")
    self.driver.find_element(By.NAME, "accountno").send_keys("12345")
    self.driver.find_element(By.NAME, "accountno").send_keys(Keys.ENTER)
    assert self.driver.switch_to.alert.text == "Account does not exist"
    self.driver.switch_to.alert.accept()

  def test_reset(self):
    self.driver.get("https://demo.guru99.com/V4/manager/BalEnqInput.php")
    self.driver.find_element(By.NAME, "accountno").send_keys("1234Acc123")
    self.driver.find_element(By.NAME, "res").click()
    assert self.driver.find_element(By.NAME, "accountno").text == ""
  
if __name__ == "__main__":
  pytest.main()