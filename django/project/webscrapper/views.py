from django.shortcuts import render
from django.http import HttpResponse
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# Create your views here.
'''

def home(request):
    return render (request,'home.html')
  

# Create your views here.

driver = webdriver.Chrome()
driver.get("https://www.99acres.com/ahmedabad-Real-Estate.htm?nn_medium=search&nn_account=google_brand&nn_campaign=111097165_6693921565&nn_keyword=%2Bwww99acres&nn_adnetwork=_b&nn_account=Google_99acres-brand&nn_campaign=111097165_6693921565_82606828885&nn_medium=111097165_6693921565_82606828885&nn_adtype=g_&nn_keyword=%2Bwww99acres&nn_placement=&gclid=EAIaIQobChMIx7SBmcSsgQMVMhuDAx3oGQjzEAAYASAAEgKJ6fD_BwE")
print(driver.title)
try :
 search_box = driver.find_element(By.ID, "keyword2")
 search_box.clear()
 search_box.send_keys("pune") # enter your name in the search box
 search_box.submit()
 property_name = driver.find_element(By.ID,"srp_tuple_society_heading")
 print('property_name')
 
property_cost = driver.find_element(By.ID,"srp_tuple_price")
property_type = driver.find_element(By.ID,"srp_tuple_bedroom")
property_area = driver.find_element(By.ID,"srp_tuple_primary_area")
property_locality = driver.find_element(By.ID,"SRP_REI_LOCALITY_TITLE")
individual_property_link = driver.find_element(By.ID,"srp_tuple_property_title")
driver.quit()

except Exception as e:
 print(f"An error occurred: {e}")
'''