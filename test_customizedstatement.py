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

class TestCustomizedstatement():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login_and_blank_error_in_account_no(self):
    self.driver.get("https://demo.guru99.com/V4/")
    self.driver.find_element(By.NAME, "uid").send_keys("mngr492649")
    self.driver.find_element(By.NAME, "password").send_keys("anyguqE")
    self.driver.find_element(By.NAME, "btnLogin").click()
    self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
    self.driver.find_element(By.NAME, "accountno").click()
    self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
    assert self.driver.find_element(By.ID, "message2").text == "Account Number must not be blank"

  def test_char_in_account_no(self):
    self.driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
    self.driver.find_element(By.NAME, "accountno").send_keys("1234Acc123")
    self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
    assert self.driver.find_element(By.ID, "message2").text == "Characters are not allowed"

  def test_special_in_account_no(self):
    self.driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
    self.driver.find_element(By.NAME, "accountno").send_keys("123!@#\\n!@#")
    self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
    assert self.driver.find_element(By.ID, "message2").text == "Special characters are not allowed"

  def test_space_in_account_no(self):
    self.driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
    self.driver.find_element(By.NAME, "accountno").send_keys("123 12")
    self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
    assert self.driver.find_element(By.ID, "message2").text == "Characters are not allowed"
  
  def test_only_space_in_account_no(self):
    self.driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
    self.driver.find_element(By.NAME, "res").click()
    self.driver.find_element(By.NAME, "accountno").click()
    self.driver.find_element(By.NAME, "accountno").send_keys(Keys.SPACE)
    self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
    assert self.driver.find_element(By.ID, "message2").text == "First character cannot have space"

  def test_blank_from_date(self):
    self.driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
    self.driver.find_element(By.NAME, "fdate").click()
    assert self.driver.find_element(By.ID, "message26").text == "From Date Field must not be blank"

  def test_blank_to_date(self):
    self.driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
    self.driver.find_element(By.NAME, "tdate").click()
    assert self.driver.find_element(By.ID, "message27").text == "To Date Field must not be blank"

  def test_char_in_minimum_value(self):
    self.driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
    self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("1234Acc123")
    self.driver.find_element(By.NAME, "amountlowerlimit").send_keys(Keys.TAB)
    assert self.driver.find_element(By.ID, "message12").text == "Characters are not allowed"

  def test_special_in_minimum_value(self):
    self.driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
    self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("123!@#\\n!@#")
    self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
    assert self.driver.find_element(By.ID, "message12").text == "Special characters are not allowed"

  def test_space_in_minimum_value(self):
    self.driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
    self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("123 12")
    self.driver.find_element(By.NAME, "amountlowerlimit").send_keys(Keys.TAB)
    assert self.driver.find_element(By.ID, "message12").text == "Characters are not allowed"

  def test_only_space_in_minimum_value(self):
    self.driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
    self.driver.find_element(By.NAME, "amountlowerlimit").click()
    self.driver.find_element(By.NAME, "amountlowerlimit").send_keys(Keys.SPACE)
    self.driver.find_element(By.NAME, "amountlowerlimit").send_keys(Keys.TAB)
    assert self.driver.find_element(By.ID, "message12").text == "First character cannot have space"

  def test_char_in_transaction_no(self):
    self.driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
    self.driver.find_element(By.NAME, "numtransaction").send_keys("1234Acc123")
    self.driver.find_element(By.NAME, "numtransaction").send_keys(Keys.TAB)
    assert self.driver.find_element(By.ID, "message13").text == "Characters are not allowed"

  def test_special_in_transaction_no(self):
    self.driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
    self.driver.find_element(By.NAME, "numtransaction").send_keys("123!@#\\n!@#")
    self.driver.find_element(By.NAME, "numtransaction").send_keys(Keys.TAB)
    assert self.driver.find_element(By.ID, "message13").text == "Special characters are not allowed"

  def test_space_in_transaction_no(self):
    self.driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
    self.driver.find_element(By.NAME, "numtransaction").send_keys("123 12")
    self.driver.find_element(By.NAME, "numtransaction").send_keys(Keys.TAB)
    assert self.driver.find_element(By.ID, "message13").text == "Characters are not allowed"

  def test_only_space_in_transaction_no(self):
    self.driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
    self.driver.find_element(By.NAME, "numtransaction").click()
    self.driver.find_element(By.NAME, "numtransaction").send_keys(Keys.SPACE)
    self.driver.find_element(By.NAME, "numtransaction").send_keys(Keys.TAB)
    assert self.driver.find_element(By.ID, "message13").text == "First character cannot have space"

  def test_reset(self):
    self.driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
    self.driver.find_element(By.NAME, "accountno").send_keys("dsgsd")
    self.driver.find_element(By.NAME, "fdate").send_keys("2023-04-05")
    self.driver.find_element(By.NAME, "tdate").send_keys("2023-04-28")
    self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("5")
    self.driver.find_element(By.NAME, "numtransaction").send_keys("1")
    self.driver.find_element(By.NAME, "res").click()
    assert self.driver.find_element(By.NAME, "accountno").text == ""
    assert self.driver.find_element(By.NAME, "fdate").text == ""
    assert self.driver.find_element(By.NAME, "tdate").text == ""
    assert self.driver.find_element(By.NAME, "amountlowerlimit").text == ""
    assert self.driver.find_element(By.NAME, "numtransaction").text == ""

  # TODO: test_valid_details
  
if __name__ == "__main__":
  pytest.main()