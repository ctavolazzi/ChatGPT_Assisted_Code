# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

API_KEY = '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'

history = {
    'previous_prompts': [],
    'previous_responses': []
}

openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)