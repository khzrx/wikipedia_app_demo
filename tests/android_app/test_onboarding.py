import allure
from allure_commons.types import Severity
from wikipedia_app_demo.pages.main_page import main_page
from wikipedia_app_demo.pages.onboarding_page import onboarding_page, onboarding_page_texts as t


@allure.parent_suite('Mobile')
@allure.suite('Онбординг')
@allure.sub_suite('Android Онбординг')
@allure.epic('Реализовать онбординг в приложении.')
@allure.feature('Онбординг приложения')
@allure.story('Пользователь должен иметь возможность пройти онбординг при открытии приложения.')
class TestOnboarding:

    @allure.title('Проверка текстов онбординга.')
    @allure.severity(Severity.MINOR)
    @allure.tag('Онбординг')
    @allure.label('owner', 'fdgoncharenko')
    def test_onboarding_texts(self):
        onboarding_page.text_should_be_equal(t.first_page_primary_text, t.first_page_secondary_text)
        onboarding_page.click_continue_button()

        onboarding_page.text_should_be_equal(t.second_page_primary_text, t.second_page_secondary_text)
        onboarding_page.click_continue_button()

        onboarding_page.text_should_be_equal(t.third_page_primary_text, t.third_page_secondary_text)
        onboarding_page.click_continue_button()

        onboarding_page.text_should_be_equal(t.fourth_page_primary_text, t.fourth_page_secondary_text)
        onboarding_page.click_done_button()

        main_page.search_container_should_be_visible()