import pytest
import time
import json
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep


# Definhg a main class which will hold methods which will act as test fixtures.
class TestEditCustomertest(unittest.TestCase):

    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def login_to_bank(self):
        self.driver.get("https://demo.guru99.com/V4/index.php")
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr492649")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("anyguqE")
        self.driver.find_element(By.NAME, "btnLogin").click()

    def login_as_manager(self):
        self.login_to_bank()
        self.driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("35203")
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        self.driver.find_element(By.NAME, "AccSubmit").click()

    def test_idisnull(self):
        self.driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message14").text == "Customer ID is required"

    def test_id_contains_space_first(self):
        self.driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys(" ")
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message14").text == "First character can not have space"

    def test_id_has_charectores(self):
        self.driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("1234Acc")
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message14").text == "Characters are not allowed"

    def test_id_has_charectores_02(self):
        self.driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("Acc123")
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message14").text == "Characters are not allowed"

    def test_id_contains_special_charectores(self):
        self.driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123!@#")
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message14").text == "Special characters are not allowed"

    def test_id_contains_special_charectores_01(self):
        self.driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("!@#")
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message14").text == "Special characters are not allowed"

    def test_id_having_valid_data_loginin(self):
        self.login_as_manager()
        expected_url = "https://demo.guru99.com/V4/manager/editCustomerPage.php"
        self.assertEqual(self.driver.current_url, expected_url)

    def test_empty_addresses_01(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "addr").click()
        self.driver.find_element(By.NAME, "addr").clear()
        self.driver.find_element(By.NAME, "addr").send_keys(Keys.TAB)
        sleep(2)
        assert self.driver.find_element(
            By.ID, "message3").text == "Address Field must not be blank"

    def test_empty_city(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").clear()
        self.driver.find_element(By.NAME, "city").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message4").text == "City Field must not be blank"

    def test_is_city_numeric_01(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys("1234")
        self.driver.find_element(By.NAME, "city").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message4").text == "Numbers are not allowed"

    def test_is_city_numeric_02(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys("city1234")
        self.driver.find_element(By.NAME, "city").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message4").text == "Numbers are not allowed"

    def test_is_city_has_specialcharectors(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys("city!@#")
        self.driver.find_element(By.NAME, "city").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message4").text == "Special characters are not allowed"

    def test_is_city_has_specialcharectors_02(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys("!@#")
        self.driver.find_element(By.NAME, "city").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message4").text == "Special characters are not allowed"

    def test_is_state_empty(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").clear()
        self.driver.find_element(By.NAME, "state").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message5").text == "State must not be blank"

    def test_is_state_numeric(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys("1234")
        self.driver.find_element(By.NAME, "state").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message5").text == "Numbers are not allowed"

    def test_is_state_numeric_01(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys("state123")
        self.driver.find_element(By.NAME, "state").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message5").text == "Numbers are not allowed"

    def test_is_state_has_specialchars(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys("state!@#")
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message5").text == "Special characters are not allowed"

    def test_is_state_has_specialchars_01(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys("!@#")
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message5").text == "Special characters are not allowed"

    def test_is_pinno_numeric_01(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").clear()
        self.driver.find_element(By.NAME, "pinno").send_keys("1234")
        self.driver.find_element(By.NAME, "pinno").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message6").text == "PIN Code must have 6 Digits"

    def test_is_pinno_numeric_02(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").clear()
        self.driver.find_element(By.NAME, "pinno").send_keys("1234PIN")
        self.driver.find_element(By.NAME, "pinno").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message6").text == "Characters are not allowed"

    def test_is_pinno_empty(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").clear()
        self.driver.find_element(By.NAME, "pinno").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message6").text == "PIN Code must not be blank"

    def test_is_pinno_six_length_01(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").clear()
        self.driver.find_element(By.NAME, "pinno").send_keys("1234567")
        self.driver.find_element(By.NAME, "pinno").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message6").text == "PIN Code must have 6 Digits"

    def test_is_pinno_six_length_02(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").clear()
        sleep(5)
        self.driver.find_element(By.NAME, "pinno").send_keys("123")
        self.driver.find_element(By.NAME, "pinno").send_keys(Keys.TAB)
        sleep(5)
        assert self.driver.find_element(
            By.ID, "message6").text == "PIN Code must have 6 Digits"

    def test_is_pinno_has_specialchars(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").clear()
        self.driver.find_element(By.NAME, "pinno").send_keys("state!@#")
        self.driver.find_element(By.NAME, "pinno").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message6").text == "Special characters are not allowed"

    def test_is_pinno_has_specialchars_01(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").clear()
        self.driver.find_element(By.NAME, "pinno").send_keys("!@#")
        self.driver.find_element(By.NAME, "pinno").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message6").text == "Special characters are not allowed"

    def test_is_number_empty(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").clear()
        self.driver.find_element(By.NAME, "telephoneno").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message7").text == "Mobile no must not be blank"

    def test_is_number_have_special_charector(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").clear()
        self.driver.find_element(
            By.NAME, "telephoneno").send_keys("886636!@12")
        self.driver.find_element(By.NAME, "telephoneno").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message7").text == "Special characters are not allowed"

    def test_is_number_have_special_charector_01(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").clear()
        self.driver.find_element(
            By.NAME, "telephoneno").send_keys("!@88662682")
        self.driver.find_element(By.NAME, "telephoneno").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message7").text == "Special characters are not allowed"

    def test_is_number_have_special_charector_02(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").clear()
        self.driver.find_element(
            By.NAME, "telephoneno").send_keys("88663682!@")
        self.driver.find_element(By.NAME, "telephoneno").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message7").text == "Special characters are not allowed"

    def test_is_email_empty(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").clear()
        self.driver.find_element(By.NAME, "emailid").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message9").text == "Email-ID must not be blank"

    def test_not_a_valid_email_01(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").clear()
        self.driver.find_element(By.NAME, "emailid").send_keys("guru99@gmail")
        self.driver.find_element(By.NAME, "emailid").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message9").text == "Email-ID is not valid"

    def test_not_a_valid_email_02(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").clear()
        self.driver.find_element(By.NAME, "emailid").send_keys("guru99")
        self.driver.find_element(By.NAME, "emailid").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message9").text == "Email-ID is not valid"

    def test_not_a_valid_email_03(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").clear()
        self.driver.find_element(By.NAME, "emailid").send_keys("Guru99@")
        self.driver.find_element(By.NAME, "emailid").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message9").text == "Email-ID is not valid"

    def test_not_a_valid_email_04(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").clear()
        self.driver.find_element(By.NAME, "emailid").send_keys("guru99@gmail.")
        self.driver.find_element(By.NAME, "emailid").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message9").text == "Email-ID is not valid"

    def test_not_a_valid_email_05(self):
        self.login_as_manager()
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").clear()
        self.driver.find_element(
            By.NAME, "emailid").send_keys("guru99gmail.com")
        self.driver.find_element(By.NAME, "emailid").send_keys(Keys.TAB)
        assert self.driver.find_element(
            By.ID, "message9").text == "Email-ID is not valid"

    def test_submit_button_click(self):
        self.login_as_manager()
        # self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "sub").click()
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert_visible = True
        except TimeoutException:
            alert_visible = False

        # Assert that the alert was visible
        self.assertTrue(alert_visible)

        # Assert that the alert is present
        self.assertTrue(alert_visible)

if __name__ == "__main__":
    pytest.main()