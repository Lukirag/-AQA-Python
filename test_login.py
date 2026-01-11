import pytest
from pages.login_page import LoginPage


class TestLoginScenarios:

    @pytest.mark.allure.title('Успешный логин (standard_user)')
    def test_successful_login(self, page):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login('standard_user', 'secret_sauce')
        assert login_page.is_on_inventory_page(), 'Не перешли на /inventory.html'
        assert login_page.is_inventory_loaded(), 'Список товаров не виден'

    @pytest.mark.allure.title('Логин с неверным паролем')
    def test_invalid_password(self, page):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login('standard_user', 'wrong_password')
        error_text = login_page.get_error_text()
        assert 'Username and password do not match' in error_text, f'Неверное сообщение: {error_text}'

    @pytest.mark.allure.title('Логин заблокированного пользователя')
    def test_locked_user(self, page):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login('locked_out_user', 'secret_sauce')
        error_text = login_page.get_error_text()
        assert 'Sorry, this user has been locked out' in error_text, f'Неверное сообщение: {error_text}'

    @pytest.mark.allure.title('Логин с пустыми полями')
    def test_empty_fields(self, page):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login('', '')
        error_text = login_page.get_error_text()
        assert 'Username is required' in error_text, f'Нет сообщения: {error_text}'

    @pytest.mark.allure.title('Логин performance_glitch_user (с задержками)')
    def test_glitch_user(self, page):
        login_page = LoginPage(page)
        login_page.goto()
        page.set_default_timeout(30000)  # 30 сек
        login_page.login('performance_glitch_user', 'secret_sauce')
        assert login_page.is_on_inventory_page(), 'Не перешли на /inventory.html (glitch)'
        assert login_page.is_inventory_loaded(), 'Товары не загрузились (glitch)'