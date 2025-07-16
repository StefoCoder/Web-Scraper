import requests
from bs4 import BeautifulSoup as BS
import re
from openai import OpenAI
import emailFinder
import emailWriter
import scraperanddraft


# THIS WILL RETURN ONLY THE EMAIL TEXT, WE NEED TO MAKE A NEW FILE CALLED EMAIL SENDER WHICH WILL THEN BE ABLE TO SEND THE EMAILS
# THIS FILE WILL THEN CALL THAT NEW FILE WHICH CAN SEND EMAILS


companies =["Nike", "Yonex", "Lotto", "Asics"]


def main(companies, cityAndCountry, userFullName, email, phone):
    for i in range(0, len(companies)):
        emails = emailFinder.find_emails(companies[i], num_results=10)
        # Now that we found the emails, let's get the text for the email using chatGPT
        print(emails)
        bodyOfEmail = emailWriter.main(companies[i], cityAndCountry, userFullName, email, phone)


        print(bodyOfEmail)

        for j in range(len(emails)):
            # This is where the actual emails will be sent, we gotta make another file for that...
            pass



        

    

    

main(companies, "Jacksonville Florida", "Stefan Sisljagic", "Sisljagics@icloud.com", "9047535115")
