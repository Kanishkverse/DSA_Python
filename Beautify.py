
import urllib.request 
from bs4 import BeautifulSoup
import csv
  
# providing url
url = "https://www.udayton.edu"
  
# opening the url for reading
html = urllib.request.urlopen(url)
  
# parsing the html file
htmlParse = BeautifulSoup(html, 'html.parser')
  
# getting all the paragraphs
for para in htmlParse.find_all("p"):
    print(para.get_text())

