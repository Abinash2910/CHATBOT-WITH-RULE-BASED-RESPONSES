def chatbot_response(user_input):
    # Convert user input to lowercase to make the bot case-insensitive
    user_input = user_input.lower()
    
    # Define simple responses based on user input
    if "hello" in user_input or "hi" in user_input:
        return "Hey there! How's it going? How can I help you today?"
    elif "how are you" in user_input:
        return "I'm doing great, thank you! Just here to assist you with whatever you need."
    elif "what is your name" in user_input:
        return "I'm your friendly chatbot, always here to lend a hand."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Take care and have an awesome day!"
    else:
        return "Hmm, I'm not sure I understood that. Could you please rephrase?"

# Example interaction
user_message = input("You: ")
print("Chatbot: " + chatbot_response(user_message))
