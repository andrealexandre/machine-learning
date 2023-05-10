# ChatGPT tutorial
# https://platform.openai.com/docs/libraries/python-library

import os
import openai

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

while True:
    user_input = input('You: ')
    match user_input:
        case 'quit':
            print("ChatGPT: Goodbye!")
            break
        case other:
            response = openai.Completion.create(
                model="text-davinci-003", 
                prompt=user_input,
                temperature=0.7, 
                max_tokens=1024
            )
            print(response.choices)
            print('ChatGPT: ' + response.choices[0].text)
