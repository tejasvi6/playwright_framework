from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from config.config import USERNAME, PASSWORD, INVALID_PASSWORD
def test_valid_login(page):

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    dashboard = DashboardPage(page)
    dashboard.verify_dashboard()

    admin = AdminPage(page)
    admin.click_admin()
    admin.verify_admin_page()

    search_username = "Admin"

    admin.search_user(search_username)
    admin.verify_search_result(search_username)

    admin.click_add()

    admin.select_user_role()
    # admin.select_employee()
    # admin.select_status()   

def test_invalid_login(page):
    login = LoginPage(page)
    login.login(USERNAME, INVALID_PASSWORD)
    login.verify_invalid_credentials()
    
   

    

