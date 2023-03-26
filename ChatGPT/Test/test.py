import openai
openai.api_key = "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"

response = openai.Completion.create(
  engine="davinci",
  prompt="What is the meaning of life?",
)

# print(response)
print(response["choices"][0]["text"])