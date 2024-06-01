import os
import creds
from groq import Groq

os.environ["GROQ_API_KEY"] = creds.api

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "when will the world end according to science",
        },
        {
            "role": "assistant",
            "content": "i am jessi robot my name is jessi, i am robot made by my developer bharath",
        },
        {
            "role": "user",
            "content": "what do u do for living and tell me ur name ",
        },
        {
            "role": "assistant",
            "content": "i am jessi robot my name is jessi, i am robot made by my developer bharath",
        }
    ],
    model="llama3-70b-8192",
)

print(chat_completion.choices[0].message.content)
print("")
print("the second response is here :")
print("  ")
print(chat_completion.choices[1].message.content)