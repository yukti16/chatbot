import json
import random
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

with open("data/responses.json") as f:
    responses = json.load(f)

def chatbot_response(user_input):
    tokens = word_tokenize(user_input.lower())

    for key in responses:
        for pattern in responses[key]["patterns"]:
            pattern_tokens = word_tokenize(pattern.lower())
            if any(word in tokens for word in pattern_tokens):
                return random.choice(responses[key]["responses"])

    return "Sorry, I didn't understand that. Can you please rephrase?"

print("🤖 Flipkart Support Chatbot")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Thank you for contacting Flipkart Support 🙏")
        break
    reply = chatbot_response(user_input)
    print("Bot:", reply)
