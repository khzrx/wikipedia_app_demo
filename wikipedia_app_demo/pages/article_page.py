import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class ArticlePage:
    def __init__(self):
        self.close_button = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/closeButton'))
        self.back_button = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Navigate up'))

    @allure.step('Кликнуть на кнопку, ведущую назад.')
    def click_back_button(self):
        self.back_button.click()

    @allure.step('Кликнуть на кнопку закрытия у модального окна.')
    def click_modal_close_button(self):
        self.close_button.click()

article_page = ArticlePage()