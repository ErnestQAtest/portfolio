# ----- Регистрация -----
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.common.exceptions import NoSuchFrameException
#----- инициализация библиотеки для Chrome -----
from selenium.webdriver.chrome.options import Options
#----- Использование Jenkins в headless режиме (без графического интерфейса) -----
options = Options()
options.headless = True
browser = webdriver.Chrome(options=options)

fake = Faker(["ru_RU"])  # Работаем с кириллицей
link = "https://pitergsm.ru/auth/?register=yes&backurl=%2Fcontacts%2Findex.php"  # Ссылка для подключения к ресурсу
browser = webdriver.Chrome()  # Отключить при использовании в headless режиме
browser.maximize_window()  # Максимальный размер экрана
browser.get(link)  # Устанавливаем подключение к ресурсу
wait = WebDriverWait(browser, 10)
# ---------------------Рандомизатор полей--------------------------
randomLogin = fake.user_name()  # Рандомизируем поле login-логин
randomPassword = fake.password()  # Рандомизируем поле password-пароль
randomEmail = fake.email()  # Рандомизируем поле email-Email
# ---------------------Регистрация--------------------------
# --------------Работа с рандомными данными--------------------
fieldLogin = browser.find_element(By.NAME, "REGISTER[LOGIN]").send_keys(randomLogin)
fieldPassword = browser.find_element(By.NAME, "REGISTER[PASSWORD]").send_keys(randomPassword)
fieldPassword1 = browser.find_element(By.NAME, "REGISTER[CONFIRM_PASSWORD]").send_keys(randomPassword)
fieldEmail = browser.find_element(By.NAME, "REGISTER[EMAIL]").send_keys(randomEmail)
time.sleep(5)
try:
    browser.driver.switch_to.frame(0)
except NoSuchFrameException:
    print("Frame at index 0 not found or inaccessible")
time.sleep(5)
captcha = browser.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-border").click()
time.sleep(5)
browser.driver.switch_to.default_content()
time.sleep(5)
submit = browser.find_element(By.NAME, "register_submit_button").click()
time.sleep(5)
