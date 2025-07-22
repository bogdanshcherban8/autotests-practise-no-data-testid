import allure
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page:Page):
        self.page = page
    def visit(self, url:str):
        with allure.step(f'Opening the url "{url}"'):
            self.page.goto(url, wait_until="networkidle")
    def reload(self):
        with allure.step(f'Reloading page with url "{self.page.url}"'):
            self.page.reload(wait_until="domcontentloaded")