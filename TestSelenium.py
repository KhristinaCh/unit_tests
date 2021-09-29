from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://passport.yandex.ru/auth/')

login_element = driver.find_element_by_name('login')
login_element.send_keys('your_login')
login_element.send_keys(Keys.RETURN)

driver.implicitly_wait(1)

passwd_element = driver.find_element_by_name('passwd')
passwd_element.send_keys('your_password')
passwd_element.send_keys(Keys.RETURN)

