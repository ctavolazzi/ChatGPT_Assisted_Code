import openai

# Set up the OpenAI API client
openai.api_key = "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"

def generate_random_number():
    prompt = "Generate one random name"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
    )
    print(response)
    return response.choices[0].text.strip()

print(generate_random_number())