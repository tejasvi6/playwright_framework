from config.config import BASE_URL,USERNAME,PASSWORD
class LoginPage:
    def __init__(self,page):
        self.page=page

    def login(self):
        self.page.goto(BASE_URL)
        self.page.get_by_placeholder("Username").fill(USERNAME)
        self.page.get_by_placeholder("Password").fill(PASSWORD)
        self.page.get_by_role("button",name="Login").click()

        

    

