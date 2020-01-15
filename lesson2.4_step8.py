from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной

button = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button = browser.find_element_by_css_selector("[id='book']")
button.click()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element_by_css_selector("[id='input_value']")
x = x_element.text
y = calc(x)

input_answer = browser.find_element_by_id("answer")
input_answer.send_keys(y)


# Отправляем заполненную форму
button = browser.find_element_by_css_selector("[id='solve']")
button.click()


#message = browser.find_element_by_id("verify_message")

#assert "successful" in message.text