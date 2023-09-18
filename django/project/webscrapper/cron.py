from django.shortcuts import render
from django.http import HttpResponse
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from pymongo import MongoClient
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
'''
driver = webdriver.Chrome()
driver.get("https://www.99acres.com/ahmedabad-Real-Estate.htm?nn_medium=search&nn_account=google_brand&nn_campaign=111097165_6693921565&nn_keyword=%2Bwww99acres&nn_adnetwork=_b&nn_account=Google_99acres-brand&nn_campaign=111097165_6693921565_82606828885&nn_medium=111097165_6693921565_82606828885&nn_adtype=g_&nn_keyword=%2Bwww99acres&nn_placement=&gclid=EAIaIQobChMIx7SBmcSsgQMVMhuDAx3oGQjzEAAYASAAEgKJ6fD_BwE")
search_box = driver.find_element(By.ID, "keyword2")
search_box.clear()
search_box.send_keys("pune") # enter your name in the search box
search_box.submit()
driver.quit()'''

driver = webdriver.Chrome()
'''
class YourView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        # Access the 'city_name' parameter from the GET request
        city_name = request.GET.get("city_name", None)
        '''

url="https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa,Residential-Plot&cityName=Mumbai"
driver.get(url)
print(driver.title)
time.sleep(10)
property_title = driver.find_elements(By.CLASS_NAME, 'mb-srp__card--title')
property_title_text = []

for element in property_title:
    property_title_text.append(element.text)
#print("property_title:", property_title_text)



property_area = driver.find_elements(By.CLASS_NAME, 'mb-srp__card__summary--value')
property_area_text = []

for element in property_area:
    property_area_text.append(element.text)
#print("property_area:", property_area_text)



property_price = driver.find_elements(By.CLASS_NAME, 'mb-srp__card__price--amount')  
property_price_text = []


for element in property_price:
    property_price_text.append(element.text)
#print("property_price:", property_price_text)







'''
property_individual_link = driver.find_elements(By.ID, 'cardid68289857')
print("PP",property_individual_link)
property_individual_link_text = []
for element in property_individual_link:
    property_individual_link_text.append(element.text)
    
    # Execute JavaScript to extract the content of the script tag within the div
for element in property_individual_link_text:
    script_content = element.get_attribute("innerHTML")  # or "innerHTML" to get the content as HTML
    if script_content:
        print("property_individual_link:", script_content)
    # Print the script content
       '''


driver.quit()
merged_data_list = []
for i in range(len(property_title_text)):
    merged_data_list.append({
        "data_1": property_title_text[i],
        "data_2": property_area_text[i],
        "data_3": property_price_text[i]
    })

client = MongoClient('mongodb://localhost:27017/')
db = client['webscrapper']  # Replace with your actual database name
collection = db['magicbricks']

result = collection.insert_many(merged_data_list)
print("Inserted IDs:", result.inserted_ids)



'''
# Insert data into MongoDB collections
collection_1 = db['propertytitle']  # Replace with your actual collection name
result_1 = collection_1.insert_many(property_title_text)
print("Inserted IDs for Collection 1:", result_1.inserted_ids)

collection_2 = db['propertyarea']  # Replace with your actual collection name
result_2 = collection_2.insert_many(property_area_text)
print("Inserted IDs for Collection 2:", result_2.inserted_ids)

collection_3 = db['propertyprice']  # Replace with your actual collection name
result_3 = collection_3.insert_many(property_price_text)
print("Inserted IDs for Collection 3:", result_3.inserted_ids)'''