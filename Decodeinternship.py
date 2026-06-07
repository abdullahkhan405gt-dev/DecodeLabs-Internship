# Simple Rule-Based Chatbot

print("Chatbot: Hello! Type 'exit' to end the chat.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Chatbot: Hi there! How can I help you?")

    elif user_input == "how are you":
        print("Chatbot: I'm doing great! Thanks for asking.")

    elif user_input == "what is your name":
        print("Chatbot: I am a simple rule-based chatbot.")

    elif user_input == "bye" or user_input == "exit":
        print("Chatbot: Goodbye! Have a nice day.")
        break

    else:
        print("Chatbot: Sorry, I don't understand that.")