link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_is_have_button_add_to_basket(browser):
    browser.get(link)    
    browser.find_element_by_class_name("btn-add-to-basket")