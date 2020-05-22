import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time


browser = webdriver.Chrome()  # инициализация браузера
try:
    link = "http://suninjuly.github.io/explicit_wait2.html"  # ссылка для перехода

    browser.get(link)  # переход по ссылке
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element_by_id("book").click()


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x = browser.find_element_by_id("input_value").text
    browser.find_element_by_id("answer").send_keys(calc(x))

    browser.find_element_by_xpath("//button[text()='Submit']").click()
    print(browser.switch_to.alert.text)


finally:
    time.sleep(5)  # любуемся результатом
    browser.quit()  # выходим