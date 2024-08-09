# -----Проверка главной страницы в качестве не зарегистрированного пользователя-----
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# -----инициализация библиотеки для Edge-----
from selenium.webdriver.edge.options import Options
# -----Использование Jenkins в headless режиме (без графического интерфейса)-----
options = Options()
options.headless = True
browser = webdriver.Edge(options=options)

link = "https://pitergsm.ru/"  # Ссылка для подключения к ресурсу
browser = webdriver.Edge()  # Отключить при использовании в headless режиме
browser.maximize_window()  # Максимальный размер экрана
browser.get(link)  # Устанавливаем подключение к ресурсу
wait = WebDriverWait(browser, 10)
# ---------------------Поисковая строка--------------------------
string = browser.find_element(By.CSS_SELECTOR, "#smart-title-search-input").send_keys("Часы самсунг")
submit = browser.find_element(By.CSS_SELECTOR, "#smart-title-search > form > div > span > button").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head > h1"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Результаты поиска"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------Вход / Регистрация--------------------------
knopka1 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-line > div.sh-line__row > div.sh-nav.sh-line__nav > div:nth-child(3) > a").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#pop-login > div > div > form > div.popup__title"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Вход в личный кабинет"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
popup_close = browser.find_element(By.CSS_SELECTOR, "#pop-login > div > a").click()
# ---------------------Контакты--------------------------
knopka2 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-line > div.sh-line__row > div.sh-nav.sh-line__nav > div.sh-nav__col.for-contact > a").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div.contacts > div.contacts__side > dl > div.contacts__way > div.contacts__header"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Как нас найти"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------Доставка и оплата--------------------------
knopka3 = browser.find_element(By.LINK_TEXT, "Доставка и оплата").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head > h1"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Доставка и оплата"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------Статьи--------------------------
knopka4 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-line > div.sh-line__row > div.sh-nav.sh-line__nav > ul > ul > li:nth-child(3) > a").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head > h1"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Статьи"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------Trade-in--------------------------
knopka5 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-line > div.sh-line__row > div.sh-nav.sh-line__nav > ul > ul > li:nth-child(4) > a").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head > h1"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Trade-in"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------Сервис--------------------------
knopka6 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-line > div.sh-line__row > div.sh-nav.sh-line__nav > ul > ul > li:nth-child(5) > a").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head > h1"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Сервис"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------Акции--------------------------
knopka7 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-line > div.sh-line__row > div.sh-nav.sh-line__nav > ul > ul > li:nth-child(6) > a").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head > h1"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Акции"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------Гарантия--------------------------
knopka8 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-line > div.sh-line__row > div.sh-nav.sh-line__nav > ul > ul > li:nth-child(7) > a").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head > h1"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Гарантия"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------Кредит--------------------------
knopka9 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-line > div.sh-line__row > div.sh-nav.sh-line__nav > ul > ul > li:nth-child(8) > a").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head > h1"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "В кредит"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------О магазине--------------------------
knopka10 = browser.find_element(By.LINK_TEXT, "О магазине").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head > h1"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "О магазине"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------Адрес--------------------------
knopka11 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-line > div.sh-line__row > div.sh-line__side > div.sh-geo.sh-line__geo > div > a.sh-geo__city.js-show-popup > span").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#pop-city > div > div > div.popup__title"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Выберите ваш город"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
closed = browser.find_element(By.CSS_SELECTOR, "#pop-city > div > a").click()
# ---------------------Вкладка iPhone--------------------------
knopka12 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-megamenu > ul > li:nth-child(1) > a").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head.page-head--catalog > h1"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "iPhone"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------Вкладка iPad--------------------------
knopka13 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-megamenu > ul > li:nth-child(2) > a").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head.page-head--catalog > h1"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Планшеты Apple iPad"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------Вкладка Mac--------------------------
knopka14 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-megamenu > ul > li:nth-child(3) > a").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head.page-head--catalog > h1"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "MacBook"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------Вкладка Умные часы--------------------------
knopka15 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-megamenu > ul > li:nth-child(4) > a").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head.page-head--catalog > h1"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Умные часы"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------Вкладка Аудио--------------------------
knopka16 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-megamenu > ul > li:nth-child(5) > a").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head.page-head--catalog > h1"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Аудио"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------Вкладка Смартфоны--------------------------
knopka17 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-megamenu > ul > li:nth-child(6) > a").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head.page-head--catalog > h1"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Смартфоны"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------Вкладка Электроника--------------------------
knopka18 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-megamenu > ul > li:nth-child(7) > a").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head.page-head--catalog > h1"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Электроника"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------Вкладка Приставки и игры--------------------------
knopka19 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-megamenu > ul > li:nth-child(8) > a").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head.page-head--catalog > h1"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Приставки и игры"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------Вкладка Техника для дома--------------------------
knopka20 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-megamenu > ul > li:nth-child(9) > a").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head.page-head--catalog > h1"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Техника для дома"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------Вкладка Гаджеты--------------------------
knopka21 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-megamenu > ul > li:nth-child(10) > a").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head.page-head--catalog > h1"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Гаджеты"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------Вкладка Телевизоры--------------------------
knopka22 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-megamenu > ul > li:nth-child(11) > a").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head.page-head--catalog > h1"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Телевизоры"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------Вкладка Планшеты и ноутбуки--------------------------
knopka23 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-megamenu > ul > li:nth-child(12) > a").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head.page-head--catalog > h1"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Планшеты и ноутбуки"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------Вкладка Аксессуары--------------------------
knopka24 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-megamenu > ul > li:nth-child(13) > a").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head.page-head--catalog > h1"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Аксессуары"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------Вкладка Сертификаты--------------------------
knopka25 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-megamenu > ul > li:nth-child(14) > a").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head.page-head--catalog > h1"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Сертификаты"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------Проверка формы отправки Email для получения писем со скидками--------------------------
string_skidka = browser.find_element(By.CSS_SELECTOR, "#bx_subscribe_subform_sljzMT > div.sf-subscribe__row > input").send_keys('and_1@mail.ru')
knopka26 = browser.find_element(By.CSS_SELECTOR, "#bx_subscribe_btn_sljzMT").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#sender-subscribe-response-cont > div > table > tbody > tr > td:nth-child(2) > div:nth-child(2)"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Вам выслано письмо. Для подтверждения перейдите по ссылке из письма"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
knopka = browser.find_element(By.CSS_SELECTOR, "#sender_subscribe_component > span").click()
# ---------------------Вход / Регистрация--------------------------
knopka27 = browser.find_element(By.CSS_SELECTOR, "body > div.site-wrapper > header > div.sh-basket.site-header__basket > div > div > div.sh-basket__btns-nav > a.sh-basket__auth.sh-basket__auth--login.js-show-popup > span").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#pop-login > div > div > form > div.popup__title"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Вход в личный кабинет"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
popup_close = browser.find_element(By.CSS_SELECTOR, "#pop-login > div > a").click()
# ---------------------Сравнение--------------------------
knopka28 = browser.find_element(By.CSS_SELECTOR, "body > div.site-wrapper > header > div.sh-basket.site-header__basket > div > div > div.sh-basket__btns-nav > a.sh-basket-btn.sh-basket__compares > span.sh-basket-btn__title").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head > h1"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Сравнение товаров"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------Избранное--------------------------
knopka29 = browser.find_element(By.CSS_SELECTOR, "body > div.site-wrapper > header > div.sh-basket.site-header__basket > div > div > div.sh-basket__btns-nav > a.sh-basket-btn.sh-basket__favorites > span.sh-basket-btn__title").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head > h1"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Избранные товары"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------Корзина--------------------------
knopka30 = browser.find_element(By.CSS_SELECTOR, "#bx_basketFKauiI > div.sh-basket__btns-basket > a > span").click()
proverka = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.site-wrapper > main > div > div.page-head > h1.page-head__title.nomobile"))).text
print(f"Тест ({proverka}) выполнен успешно !!!")
proverka1 = "Моя корзина"
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
# ---------------------логотип---------------------------
knopka31 = browser.find_element(By.CSS_SELECTOR, "#js-drop-header > div.sh-line > div.sh-line__row > div.sh-line__logo > div > a").click()
image_element = browser.find_element(By.CSS_SELECTOR,"#js-drop-header > div.sh-line > div.sh-line__row > div.sh-line__logo > div > img.sh-logo__img.sh-logo__img--mob")
image_src = image_element.get_attribute("src")  # Получение ссылки на изображение
expected_image_src = "https://pitergsm.ru/local/templates/main/tpl/img/logo-color.svg"  # Ожидаемая ссылка на изображение
if image_src == expected_image_src:
    print("Изображение логотипа соответствует ожидаемому")
else:
    print("Изображение логотипа не соответствует ожидаемому")