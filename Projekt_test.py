# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
saby_site = 'https://saby.ru/'
tensor_site = 'https://tensor.ru/'

try:
    '''Открываем сайт https://saby.ru/'''
    browser.get(saby_site)
    sleep(1)
    assert browser.current_url == saby_site, 'Неверно открыт сайт'
    print(f'Открыт сайт {saby_site}')

    '''Переходим в раздел Контакты'''
    start_btn = browser.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1')
    start_btn.click()
    print(f'Нажали вкладку {start_btn.text}')
    sleep(1)
    next_btn = browser.find_element(By.CSS_SELECTOR, '[href="/contacts"]')
    sleep(1)
    assert next_btn.is_displayed(), 'Элемент не отображается'
    button_txt = 'Еще 13 офисов в регионе'
    assert next_btn.text == button_txt
    next_btn.click()
    print(f'Кликнули по ссылке {button_txt}')
    assert browser.title == "Saby Контакты — Ярославская область", 'Неверно открыт сайт'
    print(f'Заголовок страницы {browser.title}')
    # handles = browser.window_handles
    # browser.switch_to.window(handles[1])

finally:
    browser.quit()