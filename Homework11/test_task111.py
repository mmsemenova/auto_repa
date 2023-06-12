# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
sbs_link = 'https://sbis.ru/'
contact_link = 'https://sbis.ru/contacts/16-respublika-tatarstan?tab=clients'
tensor_link = 'https://tensor.ru/'
more_link = 'https://tensor.ru/about'

try:
    driver.maximize_window()
    driver.get(sbs_link)  # Перейти на https://sbis.ru/
    sleep(2)
    assert driver.current_url == sbs_link, 'Неверная ссылка на сайт'
    tabs = driver.find_elements(By.CSS_SELECTOR, '.sbisru-Header__menu-item')
    assert len(tabs) == 4, 'Должно быть 4 вкладки'
    tab_contact = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1')
    assert tab_contact.is_displayed() is True, 'Не отображается вкладка "Контакты"'
    tab_contact.click()  # Перейти в раздел "Контакты"
    sleep(5)
    assert driver.current_url == contact_link, 'Неверная ссылка на сайт'
    sleep(5)
    # Найти баннер Тензор, кликнуть по нему
    banner_tensor = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor')
    banner_tensor.click()
    sleep(3)
    # Открытие в новой вкладке
    driver.switch_to.window(driver.window_handles[1])
    sleep(3)
    # Проверка, что перешли на https://tensor.ru/
    assert driver.current_url == tensor_link, 'Неверная ссылка на сайт'
    # Проверить, что есть блок новости "Сила в людях"
    news_block = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4 .tensor_ru-Index__card-title')
    news_block.location_once_scrolled_into_view
    sleep(3)
    assert news_block.is_displayed() is True, 'Не отображается блок "Сила в людях"'
    # Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
    button_more = driver.find_element(By.CSS_SELECTOR, '[href="/about"]')
    button_more.click()
    sleep(3)
    assert driver.current_url == more_link, 'Неверная ссылка на сайт'
finally:
    driver.quit()
