# ----Выбор товара в магазине и его оформление--------
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from faker import Faker
# -----------------инициализация библиотеки для firefox-------------
from selenium.webdriver.firefox.options import Options
# -------Использование Jenkins в headless режиме (без графического интерфейса)---------
options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)

fake = Faker(["ru_RU"])  # Работаем с кирилицей
link = "https://pitergsm.ru/personal/profile/index.php"  # Ссылка для подключения к ресурсу
browser = webdriver.Firefox()  # Отключить при использовании в headless режиме
browser.maximize_window()  #Максимальный размер экрана
browser.get(link)  # Устанавливаем подключение к ресурсу
wait = WebDriverWait(browser, 10)
# ---------------------Рандомизатор полей--------------------------
randomName = fake.name_male()  # Рандомизируем поле name-Name
randomComment = fake.text()  # Рандомизируем поле сomment-Комментарий к заказу
randomAddress = fake.address()  # Полный адрес
def generate_phone_number(): # Рандомизируем поле phone-телефон (т.к. ограничение на сайте, номер с цифры 9)
    phone_number = "9"
    for _ in range(9):
        phone_number += str(fake.random_digit())
    return phone_number
# ---------------------Авторизация--------------------------
string_login = browser.find_element(By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-body > div > div > form > div:nth-child(4) > div > input")
string_login.send_keys('and_1')
string_pass = browser.find_element(By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-body > div > div > form > div:nth-child(5) > div > input")
string_pass.send_keys('111and111')
submit = browser.find_element(By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-body > div > div > form > input.btn.btn_green.btn_txt-big").click()
# ---------------------Поиск товара--------------------------
gorod1 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-line > div.sh-line__row > div.sh-line__side > div.sh-geo.sh-line__geo > div > a.sh-geo__city.js-show-popup").click()  # Выбор города по кнопке "Нет, выбрать другой"
gorod2 = browser.find_element(By.CSS_SELECTOR, "#pop-city > div > div > div.popup__content > ul > li:nth-child(10) > div").click()  # Выбрать в списке город "Омск"
mag1 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-megamenu > ul > li:nth-child(4) > a").click()  # Переход во вкладку "Умные часы"
mag2 = browser.find_element(By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head.page-head--catalog > div.page-head__nav > ul > li:nth-child(2) > a").click()  # Выбор категории "Samsung"
mag3 = browser.find_element(By.CSS_SELECTOR, "#catalog > div:nth-child(13) > div > a").click()  # Выбор товара "Часы Samsung Galaxy Watch 5 Pro 45mm (SM-R920) (Черный титан)"
mag4 = browser.find_element(By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-body.product > div.product-head > div.product-info > div.product-info__unit.product-info__unit--params > div > form > div:nth-child(4) > ul > li:nth-child(1) > label > span").click()  # Изменить цвет товара на серый
time.sleep(3)
mag5 = browser.find_element(By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-body.product > div.product-head > div.product-info > div.product-info__unit.product-info__unit--offers > div.product-price > div.product-price__buy > a.btn.btn_green.product-price__buy-btn.product-buy-trigger.detail-product-buy-trigger").click()  # Клик по кнопке "Купить"
time.sleep(3)
product = browser.find_element(By.LINK_TEXT, "В корзину").click()  # Переход в корзину по кнопке "В корзину"
time.sleep(3)
quantity = browser.find_element(By.CSS_SELECTOR, "a[class*=counter__btn_more]").click()  # Устанавливаем количество товара "Часы Samsung Galaxy Watch 5 Pro 45mm (SM-R920) (Серый титан)"
order = browser.find_element(By.CSS_SELECTOR, "#basket_form > div.tiles__slim > div > div > div.resume__final > button").click()  # Клик по кнопке "Оформить заказ"
time.sleep(3)
oformleniye_zakaza = browser.find_element(By.CSS_SELECTOR, "#soa-property-1").clear() # Очистка значения по умолчанию, в поле ФИО
# --------------Работа с рандомными данными (оформление заказа)--------------------
fieldName = browser.find_element(By.CSS_SELECTOR, "#soa-property-1").send_keys(randomName)
phone = generate_phone_number()
fieldPhone = browser.find_element(By.CSS_SELECTOR, "#soa-property-3").send_keys(phone)
textarea = browser.find_element(By.CSS_SELECTOR, "#bx-soa-order > div.col-sm-9.bx-soa.tiles__wide > div:nth-child(4) > div.form__line > textarea").send_keys(randomComment)
# --------------Выбор способа получения заказа------------------
dostavka1 = browser.find_element(By.CSS_SELECTOR, ".bubble-tabs--vertical > div:nth-child(2) > a:nth-child(2)").click()  # Доставка
time.sleep(3)
dostavka2 = browser.find_element(By.CSS_SELECTOR, "li.button-line__item:nth-child(2) > label:nth-child(1) > span:nth-child(2)").click()  # по пригородам
time.sleep(3)
dostavka3 = browser.find_element(By.CSS_SELECTOR, ".selector__val").click()  # Выберите район доставки
time.sleep(3)
dostavka4 = browser.find_element(By.CSS_SELECTOR, ".selector__list > li:nth-child(2)").click()  # Авиагородок
time.sleep(3)
fieldAddress = browser.find_element(By.CSS_SELECTOR, "#soa-property-36").send_keys(randomAddress)
time.sleep(3)
button = browser.find_element(By.CSS_SELECTOR, "#bx-soa-total-panel > div.bx-soa-cart-total.resume > div.bx-soa-cart-total-button-container.visible-xs > a").click()  # Переход на оформить заказ
time.sleep(3)
browser.quit()  # Закрыть браузер
# Ответ "Заказ сформирован"
# # --------------Работа с рандомными данными (оплата)------------------
# card_number = fake.credit_card_number()  # Заполнение номера карты
# time.sleep(5)
# card_number_input = browser.find_element(By.CSS_SELECTOR,"#cp-pan-decor")
# card_number_input.send_keys(card_number)
# expiration_month = fake.date(pattern="%m")  # Заполнение даты истечения срока действия
# expiration_year = str(fake.future_date(end_date="+10y").year)[-2:]
# expiration_date_input = browser.find_element(By.CSS_SELECTOR,"#cc-exp-month")
# expiration_date_input.send_keys(f"{expiration_month}/{expiration_year}")
# cvv = fake.random_int(min=100, max=999)  # Заполнение кода безопасности CVV2
# cvv_input = browser.find_element(By.CSS_SELECTOR,"#cvv2")
# cvv_input.send_keys(str(cvv))
# time.sleep(3)
# oplata = browser.find_element(By.CSS_SELECTOR, "#OK").click()  # Клик по кнопке "Оплатить"
# time.sleep(5)
# # товар оплачен, ждем оповещение от банка