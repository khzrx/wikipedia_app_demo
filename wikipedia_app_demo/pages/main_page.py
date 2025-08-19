import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


class MainPage:
    def __init__(self):
        self.search_field_wrapper = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia'))
        self.search_field = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text'))
        self.search_results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        self.search_container = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_container'))

    @allure.step('В поле поиска ввести значение {article_name}.')
    def type_article_name_in_search_field(self, article_name):
        self.search_field_wrapper.click()
        self.search_field.type(article_name)

    @allure.step('Проверить наличие статьи {article_name} в поисковой выдаче.')
    def search_results_should_contain_article(self, article_name):
        with allure.step('Проверить наличие результатов поисковой выдачи.'):
            self.search_results.should(have.size_greater_than(0))

        with allure.step('Проверить наличие искомой статьи на первом месте в списке поисковой выдачи.'):
            self.search_results.first.should(have.text(article_name))

    @allure.step('Кликнуть по первой статье в поисковой выдаче.')
    def click_first_article_in_search_results(self):
        self.search_results.first.click()

    @allure.step('Проверить наличие статьи {article_name} истории поиска.')
    def search_history_should_contain_article(self, article_name):
        self.search_results.first.should(have.text(article_name))

    @allure.step('Проверить видимость поля поиска.')
    def search_container_should_be_visible(self):
        self.search_container.should(be.visible)


main_page = MainPage()