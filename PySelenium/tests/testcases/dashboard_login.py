from tests.testcases.test_base import TestBase
from tests.pages.dashboard_login_page import LoginPage
from tests.pages.dashboard_home_page import HomePage
from selenpy.support import browser

class LoginTest(TestBase):
    
    login = LoginPage()
    home = HomePage()
    
    def DA_LOGIN_TC001(self):
        self.login.open_dashboard()
        self.login.login_dashboard("SampleRepository","administrator","")
        self.home.check_login_success("administrator","SampleRepository")        
    
    def test_DA_LOGIN_TC002(self):
        self.login.open_dashboard()
        self.login.login_dashboard("SampleRepository","abc","abc")
        alert = browser.get_driver().switch_to.alert
        assert self.alert.get_text() == "Username or password is invalid"
