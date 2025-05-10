from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"  # или registration2.html для проверки багов
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля уникальными селекторами:
    browser.find_element(By.CSS_SELECTOR, "input.form-control.first[placeholder='Input your first name']").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, "input.form-control.second[placeholder='Input your last name']").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, "input.form-control.third[placeholder='Input your email']").send_keys("test@example.com")

    # Отправляем форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()

    # Ждем загрузки страницы
    time.sleep(1)

    # Проверяем успешность регистрации
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
