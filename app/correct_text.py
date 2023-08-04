import openai

def correct_text(text):
    openai_api_key = "YOUR_OPENAI_API_KEY"
    openai.api_key = openai_api_key

    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=f"Please correct the following text: {text}",
      max_tokens=150
    )

    corrected_text = response.choices[0].text.strip()
    return corrected_text

