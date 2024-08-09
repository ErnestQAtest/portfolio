
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = "https://tramontana.ru/"
    driver.get(url)
    yield driver

@pytest.mark.parametrize('login, password, expected_result', [('tokmakov.k@rambler.ru', 'test01', 'Мой кабинет'),])
def test_valid_data_login(driver, login, password, expected_result):
    try:
        driver.implicitly_wait(10)
        acc_ent = driver.find_element(By.LINK_TEXT, 'ВОЙТИ')
        acc_ent.click()

        login_input = driver.find_element(By.ID, 'USER_LOGIN_POPUP')
        login_input.click()
        login_input.clear()
        login_input.send_keys(login)

        password_input = driver.find_element(By.ID, 'USER_PASSWORD_POPUP')
        password_input.click()
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)

        wait = WebDriverWait(driver,10)
        account_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Мой кабинет')))

        actual_result = account_button.text

    except Exception as err:
        print(err)

    assert actual_result == str(expected_result)
