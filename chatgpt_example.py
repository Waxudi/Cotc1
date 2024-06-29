import openai

# Masukkan API Key Anda
openai.api_key = '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'

def ask_chatgpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    prompt = "Jelaskan cara kerja algoritma bubble sort."
    response = ask_chatgpt(prompt)
    print(response)
