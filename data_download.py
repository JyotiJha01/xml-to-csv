# Importing necessary python libraries
import xml.etree.ElementTree as ET
import requests
import os

# parse the xml file
tree =ET.parse('main.xml')
root =tree.getroot()
result = root.find('result')

# storing all urls 
urls = []
for doc in result.findall('doc'):
    urls.append(doc[1].text.strip())

# create a directory to store all the files
if not os.path.exists('data'):
    os.makedirs('data')
# downloading all zip files from the urls 

for i in range(len(urls)):
    r = requests.get(urls[i])
    with open('data/data'+str(i)+'.zip', 'wb') as f:
        f.write(r.content)
print("All files downloaded successfully.")

# unzip all the files and delete the zip files
print("Unzipping all files...")
import zipfile
for i in range(len(urls)):
    with zipfile.ZipFile('data/data'+str(i)+'.zip', 'r') as zip_ref:
        zip_ref.extractall('data')
    os.remove('data/data'+str(i)+'.zip')
print("All files unzipped successfully.")











