from selenpy.element.base_element import BaseElement
from selenpy.support.conditions import be, have
from selenpy.support import browser



class HomePage():
    
    _lbl_user_welcome = BaseElement("xpath=//div[@id='header']//a[@href='#Welcome']")
    _lbl_repository = BaseElement("xpath=//div[@id='header']//a[@href='#Repository']/span")    
    

    def __init__(self):
        pass    
    
    def check_login_success(self,username,repository):
        assert self._lbl_user_welcome.get_text() == username
        assert self._lbl_repository.get_text() == repository
    
        
        
       
