from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

# Инициализация драйвера
browser = webdriver.Chrome()

try:
    # Открываем страницу
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ожидаем пока цена не станет $100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажимаем кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # Ждем некоторое время, чтобы элемент с задачей загрузился
    time.sleep(2)

    # Получаем значение для решения задачи
    x_value = browser.find_element(By.ID, "input_value").text
    x = int(x_value.strip())  # Преобразуем в целое число

    # Решаем задачу
    answer = str(math.log(abs(12 * math.sin(x))))  # Задача: ln(abs(12*sin(x)))

    # Вводим ответ в поле ввода
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(answer)

    # Пытаемся отправить ответ
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

    # Ожидаем, когда появится сообщение с ответом
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, "h2"))
    )

    # Получаем результат
    result = browser.find_element(By.TAG_NAME, "h2").text
    print(result)

finally:
    # Закрываем браузер
    browser.quit()
