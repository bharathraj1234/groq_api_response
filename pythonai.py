import os

from groq import Groq

os.environ["GROQ_API_KEY"] = "api key here"

prompt = input("enter ur question here  ")

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "act like an human robot and response in a way like a real human do in very short ans and here is the question towards u"+prompt,
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)