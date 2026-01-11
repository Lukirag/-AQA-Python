from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('#user-name')
        self.passwordinput = page.locator('#password')
        self.loginbutton = page.locator('#login-button')
        self.errormessage = page.locator('.error-message-container')
        self.inventorylist = page.locator('.inventory_list')

    def goto(self):
        """Открыть страницу логина"""
        self.page.goto('https://www.saucedemo.com/')

    def login(self, username: str, password: str):
        """Ввести логин/пароль и нажать кнопку"""
        self.usernameinput.fill(username)
        self.passwordinput.fill(password)
        self.loginbutton.click()

    def get_error_text(self) -> str:
        """Получить текст ошибки (если есть)"""
        return self.errormessage.text_content().strip() if self.errormessage.is_visible() else ''

    def is_on_inventory_page(self) -> bool:
        """Проверить, что URL ведёт на страницу инвентаря"""
        return self.page.url.endswith('/inventory.html')

    def is_inventory_loaded(self) -> bool:
        """Проверить видимость списка товаров"""
        return self.inventorylist.is_visible()
