from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

driver = webdriver.Chrome()
driver.get("https://account.booking.com/sign-in?op_token=EgVvYXV0aCL6AgoUdk8xS2Jsazd4WDl0VW4yY3BaTFMSCWF1dGhvcml6ZRo1aHR0cHM6Ly9zZWN1cmUuYm9va2luZy5jb20vbG9naW4uaHRtbD9vcD1vYXV0aF9yZXR1cm4qmQJVck1CWEFzSlM0cVVFMVRCd1dSZTNUd2d3Unp3SVVDLUhkMGZ4ZC1ZV1V0LWItTkp5Z183bHE3RDlPUDJEZ1lKaXdFSG5NTUk1LXBaS29BZ1QyZmlXX2FjWGZwNjNpeVhuNk0weUUtVjlrZHhHNXpyVUVxVy10NFpqQ1ZsbGpGTzUxbVRZUVUzeVM0U1RDbm91OFh6Ny0zSzlhTkl4UnZZV3FjbVhqenVZRW9ZbEZVVUlzSXVkMjF5NlZzZUtSaWs5Y19VeEJBTmt3OERGNEl6VFdGbDRDYW5LcERydS1VUGx3UnZYSTRNSmU0OXZRaWhtSGM9KmV5SnBaQ0k2SW5SeVlYWmxiR3hsY2w5b1pXRmtaWElpZlE9PUIEY29kZSoxCI7IEjD5ubbx85EnOgBCAFjqreW0BpIBEHRyYXZlbGxlcl9oZWFkZXKaAQVpbmRleA")

# Wait for the username field to be visible and enter the email
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("sahil312003@gmail.com")

# Click on the next button
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/form/div[2]/div[2]/button/span').click()

# Wait for the password field to be visible and enter the password
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys("S@hil312003")

# Click on the login button
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/form/div/div[2]/div/button/span').click()

# Optional: Wait for some time to see the result
time.sleep(5)

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id=":r8:"]'))).send_keys("Bangalore")
driver.find_element(By.XPATH,'//*[@id="indexsearch"]/div[2]/div/form/div[1]/div[2]/div/div/button[1]/span').click()
driver.find_element(By.XPATH,'//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[1]/table/tbody/tr[4]/td[5]/span').click()
driver.find_element(By.XPATH,'//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[1]/table/tbody/tr[5]/td[3]/span').click()
driver.find_element(By.XPATH,'//*[@id="indexsearch"]/div[2]/div/form/div[1]/div[4]/button/span').click()

time.sleep(5)

hotels = []

name_xpath_template = '//*[@id="bodyconstraint-inner"]/div[4]/div/div[2]/div[3]/div[2]/div[2]/div[3]/div[{0}]/div[1]/div[2]/div/div[1]/div[1]/div/div[1]/div/h3/a/div[1]'
price_xpath_template = '//*[@id="bodyconstraint-inner"]/div[4]/div/div[2]/div[3]/div[2]/div[2]/div[3]/div[{0}]/div[1]/div[2]/div/div[3]/div[2]/div/div[1]/span/div/div/span[1]'

for i in range(6, 11):  # Extracting first 10 hotels
    try:
        # Extract hotel name
        hotel_name_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, name_xpath_template.format(i))))
        hotel_name = hotel_name_element.text

        # Extract hotel price
        hotel_price_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, price_xpath_template.format(i))))
        hotel_price = hotel_price_element.text

        # Append the name and price to the list
        hotels.append((hotel_name, hotel_price))
    
    except Exception as e:
        print(f"Could not extract data for hotel {i}: {e}")

# Save the data to a CSV file
with open('hotels.csv', 'w',encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Hotel Name", "Price"])
    writer.writerows(hotels)

# Optional: Close the browser
driver.quit()


