from config.config import BASE_URL
from playwright.sync_api import expect
class LoginPage:
    def __init__(self,page):
        self.page=page

    def login(self,username,password):
        self.page.goto(BASE_URL)
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button",name="Login").click()

    def verify_invalid_credentials(self):
        error = self.page.get_by_text("Invalid credentials")
        expect(error).to_be_visible()


        

    

