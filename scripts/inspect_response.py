from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Reply exactly: API connection works",
)

print(response.id)
print(response.model)
print(response.status)
print(response.output_text)
print(response.usage)
