# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains

sbs_site = 'https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru/'
contacts = 'https://fix-online.sbis.ru/page/dialogs'
driver = webdriver.Chrome()

try:
    driver.maximize_window()

    # Открываем и авторизовываемся на сайте https://fix-online.sbis.ru/
    driver.get(sbs_site)
    sleep(2)
    assert driver.current_url == sbs_site, 'Неверно открыт сайт'
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys('убадмин', Keys.ENTER)
    assert login.get_attribute('value') == 'убадмин', 'Не ввелся логин в поле'
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys('й1ц2у3к4е5н6', Keys.ENTER)
    assert password.get_attribute('value') == 'й1ц2у3к4е5н6', 'Не ввелся пароль в поле'
    sleep(2)

    # Перейти в реестр Контакты
    driver.get(contacts)
    sleep(2)
    # Отправить сообщение самому себе
    plus_btn = driver.find_element(By.CSS_SELECTOR, '.icon-RoundPlus')
    plus_btn.click()
    sleep(2)

    fio_field = driver.find_elements(By.CSS_SELECTOR, '.controls-InputBase__nativeField_hideCustomPlaceholder')
    fio_field[0].send_keys('Админ Всея Аккаунта', Keys.ENTER)
    sleep(2)
    admin_find = driver.find_element(By.CSS_SELECTOR, '.person-Info__withActivity')
    admin_find.click()
    sleep(2)
    message_text = driver.find_element(By.CSS_SELECTOR, '.textEditor_slate_Container')
    sleep(2)
    message_text.send_keys('Текст сообщения самому себе')
    yes_btn = driver.find_element(By.CSS_SELECTOR, '.icon-BtArrow')
    yes_btn.click()
    sleep(3)

    # Убедиться, что сообщение появилось в реестре
    sent_messages = driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item p')
    assert sent_messages[0].text == 'Текст сообщения самому себе', 'Отправленное сообщение отсутствует в реестре!'

    # Удалить это сообщение и убедиться, что удалили
    action_chain = ActionChains(driver)
    action_chain.move_to_element(sent_messages[0])
    action_chain.perform()
    delete_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')
    delete_btn.click()
    sleep(3)
    assert driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item p')[0] != sent_messages[0], 'Сообщение не удалено!'
    sleep(3)
finally:
    driver.quit()
