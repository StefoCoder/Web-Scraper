import re
from openai import OpenAI




client = OpenAI(
  api_key="no free keys for you bum ahh"
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


