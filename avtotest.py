import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Функция для pytest, которая загружает конфигурацию WebDriver
@pytest.fixture(scope='function')
def driver(request):
    # путь к драйверу WebDriver
    driver = webdriver.Firefox()
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver

# Параметризация теста с различными данными
test_data = [
    (
        'Иванов', 'Иван', '4958615315', 'tohimiw404@lisoren.com', 'Авиаторов', 'cbjdYwu51', 'cbjdYwu51', '4', True, ''),

    ('Иванов', '', '', '', '', '', '', '', False, ' Ошибка в поле "Имя": минимум 2 символа'),
    (
        'Иванов', 'Иван', '4958615315', 'hatabe1406@egela.com', 'Авиаторов', 'cbjdYwu51', 'wrong_password', '4', False, ' Поле Подтвердите пароль должно совпадать с полем Пароль.'
    ),
    (
        'Иванов', 'Иван', '4958615315', 'hatabe1406@egela.com', 'Авиаторов', 'cbjdYwu51', 'cbjdYwu51', '', False, ' Вы не доказали свое человечество, вы не знаете, сколько будет дважды два'
    ),
    ('Иванов', 'Иван', '49586153', 'hatabe1406@egela.com', 'Авиаторов', 'cbjdYwu51', 'cbjdYwu51', '4', False, ' Ошибка в поле "Телефон": минимум 11 символов. Вторая цифра не 7 и не 8.'),
    ('Иванов', 'Иван', '4958615315', 'test1@', 'Авиаторов', 'cbjdYwu51', 'cbjdYwu51', '4', False, '  Ваш E-mail адрес при проверке не подтвердился!'),
    (
        'Иванов', 'Иван', '4958615315', 'vadajah982@dovinou.com', 'Авиаторов', 'cbjdYwu51', 'cbjdYwu51', '4', False, '  Этот E-mail адрес уже есть в нашей базе данных!'
    ),
]

@pytest.mark.parametrize(
    'surname, name, phone, email, street, password, confirm_password, captcha_answer, expected_result, expected_error_message',
    test_data
)
def test_registration(
    driver, surname, name, phone, email, street, password, confirm_password, captcha_answer, expected_result, expected_error_message
):
    driver.implicitly_wait(10)
    driver.get('https://www.aqua-shop.ru')  # Замените на URL вашего сайта

    # автоматическое появление всплывающего окна
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.ID, 'choose_region'))
    )

    # кнопка "Выбрать"
    driver.find_element(By.ID, 'change_region').click()

    # загрузка страницы
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'main_wrap'))
    )

    # кнопка "Регистрация"
    driver.find_element(By.CSS_SELECTOR, 'a._grey').click()

    # загрузка страницы регистрации
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'main_wrap'))
    )

    # Заполнение регистрационной формы
    driver.find_element(By.ID, 'lastname').send_keys(surname)
    driver.find_element(By.ID, 'firstname').send_keys(name)
    driver.find_element(By.ID, 'phone').send_keys(phone)
    driver.find_element(By.ID, 'email_address').send_keys(email)
    driver.find_element(By.ID, 'street_address').send_keys(street)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.NAME, 'confirmation').send_keys(confirm_password)
    driver.find_element(By.NAME, 'otvet').send_keys(captcha_answer)

    # Нажать кнопку "Зарегистрироваться"
    driver.find_element(By.CSS_SELECTOR, '#main_wrap > div > div.one-row-wrap > div:nth-child(2) > form > div.submit > input').click()

    # Проверка результатов регистрации
    if expected_result:
        # Если ожидается успешная регистрация
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[1]/div/div[2]/div[2]/div/div/h1'))
        ).text

        assert 'Ваш Аккаунт успешно создан!' in success_message
    else:
        # Если ожидается ошибка
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'messageStackError'))
        )
        assert error_message.text == expected_error_message, f"Неожиданное сообщение об ошибке: {error_message.text}"

