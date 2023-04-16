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

class TestDeletecustomer():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login_and_assert_empty(self):
    self.driver.get("https://demo.guru99.com/V4/")
    self.driver.set_window_size(1920, 1040)
    self.driver.find_element(By.NAME, "uid").click()
    self.driver.find_element(By.NAME, "uid").send_keys("mngr492649")
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("anyguqE")
    self.driver.find_element(By.NAME, "btnLogin").click()
    self.driver.find_element(By.LINK_TEXT, "Delete Customer").click()
    self.driver.find_element(By.NAME, "cusid").click()
    self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
    assert self.driver.find_element(By.ID, "message14").text == "Customer ID is required"

  def test_nonnumber_error(self):
    self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
    self.driver.find_element(By.NAME, "cusid").send_keys("NONNUMBER")
    self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
    assert self.driver.find_element(By.ID, "message14").text == "Characters are not allowed"

  def test_special_error(self):
    self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
    self.driver.find_element(By.NAME, "cusid").send_keys("$PEC!AL")
    self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
    assert self.driver.find_element(By.ID, "message14").text == "Special characters are not allowed"

  def test_space_error(self):
    self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
    self.driver.find_element(By.NAME, "cusid").send_keys("123 12")
    self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
    assert self.driver.find_element(By.ID, "message14").text == "Characters are not allowed"
  
  def test_only_space_error(self):
    self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
    self.driver.find_element(By.NAME, "cusid").click()
    self.driver.find_element(By.NAME, "cusid").send_keys(Keys.SPACE)
    self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
    assert self.driver.find_element(By.ID, "message14").text == "First character can not have space"

  def test_customer_doesnt_exist(self):
    self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
    self.driver.find_element(By.NAME, "cusid").send_keys("123456")
    self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
    self.driver.find_element(By.NAME, "cusid").send_keys(Keys.ENTER)
    assert self.driver.switch_to.alert.text == "Do you really want to delete this Customer?"
    self.driver.switch_to.alert.accept()
    assert self.driver.switch_to.alert.text == "Customer does not exist!!"

  def test_correct_id(self):
    self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
    self.driver.find_element(By.NAME, "cusid").send_keys("35203")
    self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
    self.driver.find_element(By.NAME, "cusid").send_keys(Keys.ENTER)
    assert self.driver.switch_to.alert.text == "Do you really want to delete this Customer?"
    self.driver.switch_to.alert.accept()
    assert self.driver.switch_to.alert.text == "Customer does not exist could not be deleted!! First delete all accounts of this customer then delete the customer"


  def test_reset(self):
    self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
    self.driver.find_element(By.NAME, "res").click()
    assert self.driver.find_element(By.NAME, "cusid").text == ""
  
if __name__ == "__main__":
  pytest.main()