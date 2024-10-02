from lxml import html
import csv
import requests

# Your Python code here
url = 'https://www.prokerala.com/travel/indian-railway/trains/?amp=1'
response = requests.get(url)
tree = html.fromstring(response.content)
print(type(tree))

# Convert your Python code to XPath
xpath = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "table-striped", " " ))]//a')
train = []

xpath_index = tree.xpath('//td[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]')
index = []

train_dict = {}

for i in range(len(xpath)):
    train_dict[int(xpath_index[i].text)] = xpath[i].text

#print(train_dict)

