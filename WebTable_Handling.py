from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file:///C:/Users/Rakshith%20Yenadka/Desktop/.html")

#var = driver.find_element_by_xpath("//*[@id='123']/tbody/tr[1]/td[3]").text
#print(var)

#ele = driver.find_elements_by_xpath("//*[@id='123']/tbody/tr[1]")
ele = driver.find_elements_by_xpath("//*[@id='123']/tbody/tr")
print(ele)
# print(len(ele)) #returns length of the row
for i in ele:
    print(i.text)