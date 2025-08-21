# Демо-проект по автоматизации мобильного приложения Wikipedia на Android

----
### Проект реализован с использованием:
<img src="resources/python-original.svg" width="50"><img src="resources/pytest-original.svg" width="50"><img src="resources/selenium-original.svg" width="50"><img src="resources/selene.png" width="50"><img src="resources/jenkins-original.svg" width="50"><img src="resources/selenoid.png" width="50"><img src="resources/allure_report.png" width="50"><img src="resources/allure-test-ops.png" width="50"><img src="resources/tg.png" width="50"><img src="resources/appium.svg" width="50"><img src="resources/browserstack.svg" width="50">

----

### Особенности проекта

* Отчеты с видео, скриншотом, исходной моделью разметки страницы
* Сборка проекта в Jenkins
* Запуск тестов удаленно на Browserstack или локально
* Отчеты Allure Report
* Интеграция с Allure TestOps
* Оповещения о тестовых прогонах в Telegram

 ### Список реализованных проверок

- [x] Проверка наличия запрашиваемой статьи в поисковой выдаче.
- [x] Проверка текстов онбординга.
- [x] Проверка наличия искомой статьи в истории поиска.

____

### Локальный запуск
Для возможности локального запуска необходимо подготовить систему: установить Android Studio и Appium.
<a href="https://github.com/qa-guru/knowledge-base/wiki/20.-%D0%9C%D0%BE%D0%B1%D0%B8%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F-%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F-%232.-%D0%A0%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%B0%D1%82%D1%8B%D0%B2%D0%B0%D0%B5%D0%BC-%D0%B0%D0%B2%D1%82%D0%BE%D1%82%D0%B5%D1%81%D1%82%D1%8B-%D1%81-%D1%8D%D0%BC%D1%83%D0%BB%D1%8F%D1%82%D0%BE%D1%80%D0%BE%D0%BC-Android-%D1%83%D1%81%D1%82%D1%80%D0%BE%D0%B9%D1%81%D1%82%D0%B2%D0%B0-python">Инструкция по установке.</a>

> Для локального запуска необходимо выполнить команды:
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest --context=local_emulator
```
----

### Удаленный запуск автотестов выполняется в Jenkins или в Allure TestOps
> <a href="https://jenkins.autotests.cloud/job/20_goncharenko_filipp_wikipedia_app_demo/">Ссылка на проект в Jenkins</a>

> <a href="https://allure.autotests.cloud/project/4891/dashboards">Ссылка на проект в Allure TestOps</a>

#### Для запуска автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/20_goncharenko_filipp_wikipedia_app_demo/">проект</a>
2. Нажать кнопку `Build Now`
3. Результат запуска сборки можно посмотреть в отчёте Allure, в запуске Allure TestOps

#### Для запуска автотестов в Allure TestOps

1. Открыть <a target="_blank" href="https://allure.autotests.cloud/project/4891/dashboards">проект</a>
2. В боковом меню перейти на вкладку "Джобы".
3. Кликнуть кнопку "Запустить джобу" у `20_goncharenko_filipp_wikipedia_app_demo`
4. В открывшемся модальном окне при необходимости указать название и другую мета-информацию.
5. Кликнуть на кнопку "Отправить".
6. Отслеживать выполнение можно на вкладке<a target="_blank" href="https://allure.autotests.cloud/project/4891/launches">"Запуски"</a>.


----

### Параметры pytest при локальном запуске

<code>pytest --context=local_emulator</code> – запуск тестов локально на эмуляторе.

<code>pytest --context=local_real_device</code> – запуск тестов локально на девайсе.

<code>pytest --context=bstack</code> – запуск тестов на BrowserStack (понадобится файл <code>.env.credentials</code> с данными учетной записи BrowserStack).


### Allure отчет


#### Общие результаты
<img src="resources/allure_overview.png" alt="Allure отчет. Общие результаты." width="800">

#### Список тест кейсов в Allure 
<img src="resources/allure_test_cases.png" alt="Allure отчет. Список тест кейсов в Allure." width="800">

#### Пример тест кейса в Allure с логированием и вложениями
<img src="resources/allure_test_sample.png" alt="Allure отчет. Пример тест кейса в Allure" width="400">

### Allure TestOps

#### Примеры запуска в Allure TestOps
<img src="resources/allure_test_ops_1.png" alt="Allure TestOps 1" width="800">
<br>
<img src="resources/allure_test_ops_2.png" alt="Allure TestOps 2" width="800">
<br>
<img src="resources/allure_test_ops_3.png" alt="Allure TestOps 3" width="800">

#### Нотификация в Telegram
<img src="resources/tg_report.png" alt="Telegram notification" width="400">

#### Видео прохождения теста
<img src="resources/test_gif.gif" alt="test video" width="400">