from Base.InitiateDriver import startBrowser,closeBrowser
import time

def test_Validate_InValid_data_Registration():
    driver=startBrowser()
    driver.find_element('xpath',"//input[@name='firstname']").send_keys('12345')
    driver.find_element('xpath',"//input[@name='lastname']").send_keys('000')

    closeBrowser()
    time.sleep(30)