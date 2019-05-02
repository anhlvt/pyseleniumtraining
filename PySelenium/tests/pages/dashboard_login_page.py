from selenpy.element.text_box import TextBox
from selenpy.element.combo_box import ComboBox
from selenpy.element.base_element import BaseElement
from selenpy.support.conditions import be, have
from selenpy.support import browser



class LoginPage():
    
    _cbb_repository =ComboBox("id=repository")
    _txt_username = TextBox("id=username")
    _txt_password = TextBox("id=password")
    _btn_login = BaseElement("class=btn-login")    
    

    def __init__(self):
        pass
    
    def open_dashboard(self):
        browser.open_url("http://localhost:54000/TADashboard/login.jsp")        
        #browser.wait_until(have.title("TestArchitect ™"))        
        
    def login_dashboard(self,repository,username, password):        
        self._txt_username.wait_until(be.visible)
        self._cbb_repository.select_by_value(repository)
        self._txt_username.send_keys(username)
        self._txt_password.send_keys(password)
        self._btn_login.click()
        
