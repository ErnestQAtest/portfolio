from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    url = "https://tramontana.ru/"
    driver.get(url)
    yield driver

# Проверка на не возможность авторизации с пустыми полями

@pytest.mark.parametrize('login, password, expected_result',[('', 'test01', 'Заполните это поле'),('tokmakov.k@rambler.ru', '', 'Заполните это поле'),('', '', 'Заполните это поле')])
def test_empty_data_login(driver, login, password, expected_result):
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

        wait = WebDriverWait(driver,5)
        err_msg = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'error')))

        actual_result = err_msg.text

    except Exception as err:
        print(err)

    assert actual_result == str(expected_result)

# Проверка на не возможность авторизации с не корректными данными полей

@pytest.mark.parametrize('login, password, expected_result', [('ivanov@rambler.ru', 'test01', 'Неверный логин или пароль.') ,('tokmakov.k@rambler.ru', 'test999', 'Неверный логин или пароль.'), ('ivanov@rambler.ru', 'test999', 'Неверный логин или пароль.')])
def test_invalid_data_login(driver, login, password, expected_result):
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
        incorrect_err_msg = wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='Неверный логин или пароль.']")))

        actual_result = incorrect_err_msg.text

    except Exception as err:
        print(err)

    assert actual_result == str(expected_result)

