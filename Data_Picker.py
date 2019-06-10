from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path="D:\\Browser_drivers\\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="D:\\Browser_drivers\\geckodriver.exe")
driver.get("https://jqueryui.com/datepicker/#dropdown-month-year")
driver.implicitly_wait(30)
framevar = driver.find_element_by_xpath("//iframe[@class='demo-frame']")
driver.switch_to.frame(framevar)
driver.find_element_by_xpath("//input[@class='hasDatepicker']").click()
month = driver.find_element_by_class_name("ui-datepicker-month")
S1 = Select(month)
S1.select_by_visible_text("Mar")
year = driver.find_element_by_class_name("ui-datepicker-year")
S2 = Select(year)
S2.select_by_value("2020")
driver.find_element_by_xpath("//a[text()='3']").click()


