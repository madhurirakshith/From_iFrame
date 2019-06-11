from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="D:\\Browser_drivers\\chromedriver.exe")
driver.get("https://phptravels.com/")
driver.find_element_by_xpath("//span[text()='Login']").click()
print("Current window", driver.current_window_handle)
c_w = driver.current_window_handle
w_h = driver.window_handles
for i in w_h:
    if i!=c_w:
        driver.switch_to.window(i)
driver.find_element_by_id("inputEmail").send_keys("TestWindows")