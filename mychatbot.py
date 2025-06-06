# Omah Dental Clinic Chatbot
# Rule-based chatbot with friendly replies

#It greet the user
def greet_user():
    print("Hello! Welcome to Omah Dental Clinic.")
    name = input("May I know your name? ").strip().title()
    print(f"It’s a pleasure to meet you, {name}! I'm here to help—what would you like to know?")
    return name
#show services we provide
def show_services():
    print("\n You can ask about:")
    print("1. Working Hours ,2. Location,3. Appointment Booking,4. Dental Services we provide ,5. Walk-in Policy")
    print("You can type 'services' to see this list again or 'Exit' to Leave.")

#It give response from user
def get_response(user_Input):
    user_Input = user_Input.lower()

    # response for Thank-you 
    if any(keyword in user_Input for keyword in ["thank", "thanks", "thank you", "ok thank you", "thx"]):
        return "You're welcome!!"

    if any(keyword in user_Input for keyword in ["hour", "time", "open", "working"]):
        return "Our working hours are Monday to Friday, 9 AM to 5 PM."

    elif any(keyword in user_Input for keyword in ["location", "where", "address"]):
        return "We are located at 67 Anjuman complex, Nagpur -11."

    elif any(keyword in user_Input for keyword in ["appointment", "book", "schedule"]):
        return "You can book an online appointment by visiting our website and by calling (6786 or 7123)"

    elif any(keyword in user_Input for keyword in ["service", "cleaning", "whitening", "braces"]):
        return "Yes, we offer teeth whitening and many other dental services."

    elif any(keyword in user_Input for keyword in ["walk-in", "walkin", "walk ins"]):
        return "Yes, we accept walk-ins, but scheduled appointments are preferred."

    elif user_Input == "services":
        show_services()
        return None

    elif user_Input in ["exit", "quit", "bye"]:
        return "exit"

    else:
        return " I'm not sure about that yet. You can try asking something else or type 'services' for help."

def mychatbot():
    name = greet_user()
    show_services()

    while True:
        user_Input = input("\nYou: ").strip()
        response = get_response(user_Input)

        if response == "exit":
            print(f"Bot: Thank you for visiting Omah Dental, {name}. Have a great day!!!!")
            break
        elif response:
            print("Bot:", response)

# Run  chatbot
if __name__ == "__main__":
    mychatbot()
