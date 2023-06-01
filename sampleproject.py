from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# initialize driver
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.implicitly_wait(10)
# Automate Login:
#To find the username and password fields and enter the credentials
username_field = driver.find_element(By.ID,"user-name").send_keys("standard_user")
password_field = driver.find_element(By.ID,"password").send_keys("secret_sauce")

#To find the username and password fields and enter the another credentials
# username_field = driver.find_element(By.ID,"user-name").send_keys("performance_glitch_user")
# password_field = driver.find_element(By.ID,"password").send_keys("secret_sauce")

# Submit the form
login_button = driver.find_element(By.ID,"login-button").click()


# Add items to the cart
add_to_cart_buttons = driver.find_elements(By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]')
for add_button in add_to_cart_buttons:
      add_button.click()

#Go to the cart page
cart_link = driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()

#Remove items from the cart
remove_buttons = driver.find_elements(By.ID,"remove-sauce-labs-backpack")
for remove_button in remove_buttons:
      remove_button.click()

#Add items to the cart again
add_to_cart_buttons = driver.find_elements(By.ID,"add-to-cart-sauce-labs-backpack")
for add_button in add_to_cart_buttons:
      add_button.click()

#Go to the cart page
cart_link = driver.find_element(By.CSS_SELECTOR,".shopping_cart_link")
cart_link.click()

#Proceed to checkout
checkout_button = driver.find_element(By.ID,"checkout")
checkout_button.click()

#Enter shipping and billing information
firstname_field = driver.find_element(By.ID,"first-name").send_keys("lara")
lastname_field = driver.find_element(By.ID,"last-name").send_keys("daniel")
postalcode_field = driver.find_element(By.ID,"postal-code").send_keys("12345")

#Place the order
place_order_button = driver.find_element(By.ID,"continue").click()
# Close the browser:
driver.quit()
