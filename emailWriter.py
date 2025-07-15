import re
from openai import OpenAI

client = OpenAI(
  api_key=""
)


brandName = "Nike"
cityAndCountry = "Jacksonville, Florida"
name = "Stefan Sisljagic"
email = "stefan.s@example.com"
phone = "(904) 555-1234"


def strip_brackets(text):
    return re.sub(r"\[.*?\]", "", text).strip()

def main(brandName, cityAndCountry, name, email, phone):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {
                "role": "user",
                "content": (
                    f"Write a professional sponsorship inquiry email addressed to {brandName} from me: {name}. "
                    f"Do research on the brand's tennis-related marketing, values, and athlete partnerships to tailor the message. "
                    f"I am a passionate tennis player based in {cityAndCountry}. "
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


print(main(brandName, cityAndCountry, name, email, phone))
