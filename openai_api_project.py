from openai import OpenAI

client = OpenAI(
    # must go to email to get API key
    api_key=""
)


completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What does a cat say?"}
  ]
)

print(completion.choices[0].message.content)
