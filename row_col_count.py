from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file:///C:/Users/Rakshith%20Yenadka/Desktop/.html")

col_val = driver.find_elements_by_xpath("//*[@id='123']/tbody/tr[1]/td")
col_count = len(col_val)
print("Column count",col_val)

row_val = driver.find_elements_by_xpath("//*[@id='123']/tbody/tr")
row_count = len(row_val)
print("Row count",row_val)