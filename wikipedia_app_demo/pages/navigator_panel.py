import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


class NavigatorPanel:
    def __init__(self):
        self.search_button = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/nav_tab_search'))

    @allure.step('Кликнуть на кнопку "Search" на панели навигации.')
    def click_search_button(self):
        self.search_button.click()


navigator_panel = NavigatorPanel()