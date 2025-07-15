import requests

from bs4 import BeautifulSoup as BS

response = requests.get("https://www.scoreandchange.com/tennis-sponsorships-men-singles/") #Put whatever website the king would like

soup = BS(response.content, "html.parser")

content_div = soup.find("div", class_="entry themeform") #Change the class to whatever is used in the website

if content_div:
    for paragraph in content_div.find_all("p"): #Prints paragraphs, change it for links or anything else
        print(paragraph.text.strip())

else:

    print("No content found.")