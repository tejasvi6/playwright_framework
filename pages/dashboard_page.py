from playwright.sync_api import expect
class DashboardPage:
    def __init__(self,page):
        self.page = page

    def verify_dashboard(self):
        expect(self.page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")