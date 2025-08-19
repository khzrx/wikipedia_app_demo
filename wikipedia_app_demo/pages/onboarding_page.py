import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from dataclasses import dataclass


class OnboardingPage:
    def __init__(self):
        self.skip_button = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button'))
        self.primary_text = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))
        self.secondary_text = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/secondaryTextView'))
        self.forward_button = browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button'))
        self.done_button = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button'))

    @allure.step('Кликнуть на кнопку "Skip" в онбординге.')
    def click_skip_button(self):
        self.skip_button.click()

    @allure.step('Проверить основной текст.')
    def primary_text_should_be_equal(self, primary_text: str):
        self.primary_text.should(have.text(primary_text))

    @allure.step('Проверить второстепенный текст.')
    def secondary_text_should_be_equal(self, secondary_text: str):
        self.secondary_text.should(have.text(secondary_text))

    @allure.step('Проверить текст на странице.')
    def text_should_be_equal(self, primary_text: str, secondary_text: str):
        self.primary_text_should_be_equal(primary_text)
        self.secondary_text_should_be_equal(secondary_text)

    @allure.step('Кликнуть на кнопку "Continue".')
    def click_continue_button(self):
        self.forward_button.click()

    @allure.step('Кликнуть на кнопку "Get started".')
    def click_done_button(self):
        self.done_button.click()


@dataclass
class OnboardingPageTexts:
    first_page_primary_text: str = 'The Free Encyclopedia\n…in over 300 languages'
    second_page_primary_text: str = 'New ways to explore'
    third_page_primary_text: str = 'Reading lists with sync'
    fourth_page_primary_text: str = 'Data & Privacy'
    first_page_secondary_text: str = 'We’ve found the following on your device:'
    second_page_secondary_text: str = 'Dive down the Wikipedia rabbit hole with a constantly updating Explore feed. \n'
    'Customize the feed to your interests – whether it’s learning about historical events '
    'On this day, or rolling the dice with Random.'
    third_page_secondary_text: str = 'You can make reading lists from articles you want to read later, even when you’re offline. \n'
    'Login to your Wikipedia account to sync your reading lists. Join Wikipedia'
    fourth_page_secondary_text: str = 'We believe that you should not have to provide personal information to participate in the free knowledge '
    'movement. Usage data collected for this app is anonymous. '
    'Learn more about our privacy policy and terms of use.'

onboarding_page = OnboardingPage()
onboarding_page_texts =OnboardingPageTexts()