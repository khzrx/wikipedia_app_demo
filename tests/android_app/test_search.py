import allure
from allure_commons.types import Severity
from wikipedia_app_demo.pages.onboarding_page import onboarding_page
from wikipedia_app_demo.pages.main_page import main_page
from wikipedia_app_demo.pages.article_page import article_page
from wikipedia_app_demo.pages.navigator_panel import navigator_panel

@allure.parent_suite('Mobile')
@allure.suite('Поиск')
@allure.sub_suite('Поиск и поисковая выдача')
@allure.epic('Реализовать поиск')
@allure.feature('Поиск статьи')
@allure.story('Пользователь должен иметь возможность найти статью по запросу')
class TestSearch:

    @allure.title('Проверка наличия запрашиваемой статьи в поисковой выдаче.')
    @allure.severity(Severity.NORMAL)
    @allure.tag('Поиск')
    @allure.label('owner', 'fdgoncharenko')
    def test_search(self):
        article_name = 'Naruto'
        onboarding_page.click_skip_button()

        main_page.type_article_name_in_search_field(article_name)

        main_page.search_results_should_contain_article(article_name)


    @allure.title('Проверка наличия искомой статьи в истории поиска.')
    @allure.severity(Severity.NORMAL)
    @allure.tag('Поиск')
    @allure.label('owner', 'fdgoncharenko')
    def test_article_in_search_history(self):
        article_name = 'Naruto'
        onboarding_page.click_skip_button()

        main_page.type_article_name_in_search_field(article_name)
        main_page.click_first_article_in_search_results()
        article_page.click_modal_close_button()
        article_page.click_back_button()
        article_page.click_back_button()
        navigator_panel.click_search_button()

        main_page.search_history_should_contain_article(article_name)

