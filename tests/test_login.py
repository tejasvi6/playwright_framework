from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.config import USERNAME, PASSWORD, INVALID_PASSWORD
def test_valid_login(page):
    login = LoginPage(page)
    login.login(USERNAME,PASSWORD)

    dashboard = DashboardPage(page)
    dashboard.verify_dashboard()

def test_invalid_login(page):
    login = LoginPage(page)
    login.login(USERNAME, INVALID_PASSWORD)
    login.verify_invalid_credentials()
    input("Press Enter to continue...")
   

    

