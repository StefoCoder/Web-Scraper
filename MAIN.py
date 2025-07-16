import requests

from bs4 import BeautifulSoup as BS

import re

from openai import OpenAI

response = requests.get("https://www.scoreandchange.com/tennis-sponsorships-men-singles/") #DO NOT CHANGE THE WEBSITE, I WOULD HAVE TO RECODE EVERYTHING SINCE THE HTML STRUCTURE VARIES PER SITE

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
    return select_brand()

def select_brand():

    user_choice = input("\nThese are the most recent brands found working with professional tennis athletes. Please enter a brand you're interested in partnering with from the list above:\n\n")

    if user_choice.casefold() in [item.casefold() for item in clothing_column]:
        user_full_name = input("What is your first and last name? (e.g. Billy Bob). This and the following questions will be used to draft a personalized email shortly.\n\n")

        user_UTR = input("\n\nWhat is your UTR?\n\n")

        cityAndCountry = input("\n\nWhat is your city and country?\n\n")

        email = input("\n\nWhat is your email?\n\n")

        phone = input("\n\nLast question! What is your phone number?\n\n")

        return user_choice, user_full_name, user_UTR, cityAndCountry, email, phone  

    else:
        print("\nThat brand wasn’t found in the list. Please check the spelling or try a different one.")
        return select_brand()   

    #IGNORE WHAT FOLLOWS

    '''
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
    '''
    #RESUME READING HERE
     
#THIS IS THE END OF THE WEBSCRAPER AND BELOW MARKS THE BEGINNING OF THE PERSONALIZED EMAIL DRAFTER#

client = OpenAI(
  api_key=""
)

def strip_brackets(text):
    return re.sub(r"\[.*?\]", "", text).strip()

def main(user_choice, cityAndCountry, user_full_name, email, phone):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {
                "role": "user",
                "content": (
                    f"Write a professional sponsorship inquiry email addressed to {user_choice} from me: {user_full_name}. "
                    f"Do research on the brand's tennis-related marketing, values, and athlete partnerships to tailor the message. "
                    f"I am a passionate tennis player based in {cityAndCountry} with a UTR of {user_UTR}. "
                    f"My training emphasizes performance and community outreach. "
                    f"I am seeking a brand partnership that aligns with my dedication to both athletic growth and promoting tennis in local communities. "
                    f"My contact email is {email} and phone number is {phone}. "
                    f"The email should be well-structured, polished, and immediately ready to send — do not include placeholders or brackets. "
                    f"Keep it sincere, confident, and aligned with the brand's style. "
                    f"Do NOT include the subject in your response."
                )
            }
        ]
    )
    return strip_brackets(completion.choices[0].message.content)

user_choice, user_full_name, user_UTR, cityAndCountry, email, phone = get_brand_names()
print("\n\n--- EMAIL GENERATING SHORTLY ---\n")
print(main(user_choice, cityAndCountry, user_full_name, email, phone))

