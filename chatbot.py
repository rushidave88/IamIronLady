faqs = {
    "programs": "Iron Lady offers leadership programs on entrepreneurship, women empowerment, and skill development.",
    "duration": "The duration ranges from 3 to 6 months depending on the course.",
    "mode": "Programs are offered both online and offline.",
    "certificates": "Certificates are provided upon completion.",
    "mentors": "Mentors include experienced women leaders and industry experts."
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    if "program" in user_input:
        return faqs["programs"]
    elif "duration" in user_input:
        return faqs["duration"]
    elif "mode" in user_input:
        return faqs["mode"]
    elif "online" in user_input or "offline" in user_input:
        return faqs["mode"]
    elif "certificate" in user_input:
        return faqs["certificates"]
    elif "mentor" in user_input or "coach" in user_input:
        return faqs["mentors"]
    else:
        return "Sorry, I don't understand. Please ask about programs, duration, mode, certificates, or mentors."

print("Welcome to Iron Lady FAQ Chatbot! Type 'exit' to quit.")
while True:
    user_input = input('You: ')
    if user_input.lower() == 'exit':
        print("Chatbot: Thank you! Goodbye.")
        break
    print("Chatbot:", chatbot_response(user_input))
