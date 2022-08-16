import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from getpass import getpass


def login():

    username = input('Email: ')
    password = getpass('Password: ')

    driver = uc.Chrome()

    driver.delete_all_cookies()

    driver.get('https://accounts.google.com/ServiceLogin')

    WebDriverWait(
        driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//input[@type="email"]'))).send_keys(username)
    WebDriverWait(
        driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, 'identifierNext'))).click()


    WebDriverWait(
        driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//input[@type="password"]'))).send_keys(password)
    WebDriverWait(
        driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, 'passwordNext'))).click()

    driver.get('https://gmail.com')


if __name__ == '__main__':
    login()
