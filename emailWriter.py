from openai import OpenAI

client = OpenAI(
  api_key="yourkeyhere"
)




brandName = "Nike"

cityAndCountry = "Jacksonville, Florida"

name = "Stefan Sisljagic"


def main(brandName, cityAndCountry, name):

  completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
      {"role": "user", "content": "Write a professional sponsorship inquiry email addressed to " + brandName + " from me: " + name + ". Do research on the brands tennis-related marketing, values, and athlete partnerships to tailor the message. Use the following information about me to personalize the email:I am a passionate tennis player based in + " + cityAndCountry + ".My training emphasizes performance and community outreach.I am seeking a brand partnership that aligns with my dedication to both athletic growth and promoting tennis in local communities.The email should be well-structured, polished, and immediately ready to send — do not include placeholders or brackets. Keep it sincere, confident, and aligned with the brand's style. Once again, use only the information given to you to write the email; DO NOT leave any brackets for where the user should type in more information, this email will be sent out immediately, so do not have that happen! ALso, don't include the subject in your response. "}
    ]
  )

  return(completion.choices[0].message.content)


print(main(brandName, cityAndCountry, name))