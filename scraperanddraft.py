import requests

from bs4 import BeautifulSoup as BS

response = requests.get("https://www.scoreandchange.com/tennis-sponsorships-men-singles/") #Put whatever website the king would like

soup = BS(response.content, "html.parser")

table = soup.find("table")

rows = table.find_all("tr")

headers = [th.get_text(strip=True) for th in rows[0].find_all("th")]

try:
    clothing_index = headers.index("Clothing")
except ValueError:
    print("Could not find 'Clothing' column.")
    clothing_index = None

clothing_index = headers.index("Clothing")

clothing_column = []

for row in rows[1:]:

    columns = row.find_all(["td", "th"])

    if len(columns) > clothing_index:
            clothing = columns[clothing_index].get_text(strip=True)
            clothing_column.append(clothing)

def get_brand_names():
    for item in clothing_column:
         print(item)
    select_brand()

def select_brand():

    user_choice = input("\nPlease enter a brand you're interested in partnering with:\n\n")

    user_full_name = input("What is your first and last name? (e.g. Billy Bob). This will be used to draft a personalized email shortly.\n\n")

    user_UTR = input("\n\nWhat is your UTR? This will be used to draft a personalized email shortly.\n\n")

    if user_choice.casefold() in [item.casefold() for item in clothing_column]:
        email = f"""
        Subject: Sponsorship Inquiry from a Rising Athlete

        Dear {user_choice.capitalize()} Team,

        My name is {user_full_name}, and I am a passionate and dedicated tennis player with a UTR of {user_UTR} and I am heavily inspired by your brand.
        I have noticed that many top players trust {user_choice.capitalize()}, and I would love the opportunity to discuss a potential partnership or sponsorship.

        I believe we could form a valuable collaboration. Please let me know if you're open to discussing this further.

        Best regards,  
        {user_full_name}
        """
        print("\nGenerated Email:\n")
        print(email)
    else:
        print("\nThat brand wasn’t found in the list. Please check the spelling or try a different one.")
        select_brand()   
        
get_brand_names()

 


