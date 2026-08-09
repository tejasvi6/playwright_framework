from playwright.sync_api import expect


class AdminPage:

    def __init__(self, page):
        self.page = page

    def click_admin(self):
        self.page.get_by_role("link", name="Admin").click()

    def verify_admin_page(self):
        expect(self.page).to_have_url(
            "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"
        )
        expect(self.page).to_have_title("OrangeHRM")
        expect(
            self.page.get_by_role("heading", name="Admin")
        ).to_be_visible()

    def search_user(self, username):
        search_form = self.page.locator("form")

        search_form.locator("input.oxd-input").first.fill(username)

        search_form.get_by_role(
            "button", name="Search"
        ).click()

    def verify_search_result(self, username):
        table = self.page.locator(".oxd-table-body")

        rows = table.locator(".oxd-table-row")

        matching_row = rows.filter(
            has_text=username
        ).first

        expect(matching_row).to_be_visible()

    def click_add(self):
        self.page.get_by_role(
            "button", name="Add"
        ).click()

    def select_user_role(self):
        self.page.locator(
            ".oxd-select-text"
        ).first.click()

        self.page.get_by_role(
            "listbox"
        ).get_by_text(
            "Admin",
            exact=True
        ).click()

    # def select_employee(self, search_text="a"):
    #     employee_input = self.page.get_by_placeholder(
    #         "Type for hints..."
    #     )

    #     employee_input.fill(search_text)

    #     dropdown = self.page.locator(
    #         ".oxd-autocomplete-dropdown"
    #     )

    #     expect(dropdown).to_be_visible()

    #     options = dropdown.locator(
    #         ".oxd-autocomplete-option"
    #     )

    #     expect(options.first).to_be_visible()

    #     options.first.click()

    # def select_status(self):
    #     self.page.locator(
    #         ".oxd-select-text"
    #     ).nth(1).click()

    #     self.page.get_by_role(
    #         "listbox"
    #     ).get_by_text(
    #         "Enabled",
    #         exact=True
    #     ).click()