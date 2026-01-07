from Base.InitiateDriver import startBrowser,closeBrowser
from Library.ConfigReader import ElementsRead

def test_ValidateRegistration():
    driver=startBrowser()
    driver.find_element('name',ElementsRead('Registration','fname')).send_keys('Shyam')
    driver.find_element('name',ElementsRead('Registration','lname')).send_keys('Thapa')
    driver.find_element('password',ElementsRead('Registration','pwd')).send_keys('Shyam123')
    # driver.find_element('xpath',"//input[@name='lastname']").send_keys('Thapa')

    closeBrowser()