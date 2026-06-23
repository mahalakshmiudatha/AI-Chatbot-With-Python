print("🤖 My Chatbot")
print("Type 'bye' to exit")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi! Welcome.")
    
    elif user == "how are you":
        print("Bot: I am fine.")
    
    elif user == "what is your name":
        print("Bot: My name is ChatBot.")
    
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    
    else:
        print("Bot: Sorry, I don't understand.")