# import chatbot

# def main():
#     bot = chatbot.Chatbot()

#     print("Welconme to the ai language learninng model: ")

#     user_id = input('Enter your username: ')
#     native_language = input("What is your native language: ")
#     learning_language = input("What language do you want to learn: ")
#     level = input("What is your current level(Beginner/Intermediate/Advanced)?: " )

#     print(bot.start_conversation(user_id,native_language,learning_language,level))

#     while True:
#         user_input = input('\nYou:')
#         if user_input.lower() == "exit":
#             print('Existing the chatbot.Goodbye')
#             break

#         elif user_input.lower=="feedback":
#             print(bot.get_feedback(user_id))

#         else:
#             response = bot.chat(user_id,user_input)

#             print(f"chatbot :{response}")

# if __name__ == "__main__":
#     main()



import chatbot

def main():
    bot = chatbot.Chatbot()

    print("Welcome to the AI Language Learning Model!")

    user_id = input("Enter your username: ")
    native_language = input("What is your native language? ")
    learning_language = input("What language do you want to learn? ")
    level = input("What is your current level (Beginner/Intermediate/Advanced)? ")

    print(bot.start_conversation(user_id, native_language, learning_language, level))

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            print("Exiting the chatbot. Goodbye!")
            break
        elif user_input.lower() == "feedback":
            print(bot.get_feedback(user_id))
        else:
            response = bot.chat(user_id, user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
