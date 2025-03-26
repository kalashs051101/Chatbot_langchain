# import os 
# import openai
# # from langchain_community.chat_models import ChatOpenAI
# from langchain_openai import ChatOpenAI  # ✅ Correct
# from langchain.schema import HumanMessage, SystemMessage
# from langchain_google_genai import GoogleGenerativeAI
# from dotenv import load_dotenv
# from database import Database

# load_dotenv()
# # openai.api_key = os.getenv("GOOGLE_API_KEY")
# os.getenv("GOOGLE_API_KEY")

# # print(openai.api_key)


# class Chatbot:
#     def __init__(self):
#         # self.model = ChatOpenAI(model_name ="gpt-4")
#         self.model = GoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=os.getenv("GOOGLE_API_KEY"))
#         # self.model = Ollama(model_name ="llama3.2")
#         # self.model = Ollama(model="llama3")

#         # print(f'this is model{self.model}')

#         self.db = Database()
#         # pass

#     def start_conversation(self,user_id,native_language,learning_language,level):
#         # pass
#         self.db.add_user(user_id,native_language,learning_language,level)

#         return f"Great let start learning {learning_language} I will guide you and track your mistakes"

#     def chat(self,user_id,user_input):
#         # pass
#         messages=[
#             SystemMessage(
#                 content = "you are langauge tutor that helps users learn a new language",
            
#             ),
#             HumanMessage(
#                 content=user_input
#             )
#         ]
#         response = self.model.invoke(messages)

#         ai_response = response.content if hasattr(response, "content") else response
#         if "incorrect" in ai_response.lower() or "should be" in ai_response.lower():  

#             print('user input : ++',user_input)
#             print('si response',ai_response)
            
#             mistake = user_input  # Store user input as mistake
#             correction = ai_response  # Store AI response as correction
#             self.db.log_mistake(user_id, mistake, correction)

#         return ai_response
#         # if 'mistake' in user_input.lower():
#         #     mistake = "mistake_word"
#         #     correction = "corrected_word" 
#         #     self.db.log_mistake(user_id,mistake,correction)
#         # # return response.content
#         # if isinstance(response, str):  # If response is a string, return it directly
#         #     return response
#         # elif hasattr(response, "content"):  # If response has 'content' attribute
#         #     return response.content
#         # else:
#         #     return "Sorry, I couldn't understand the response."

#     def get_feedback(self,user_id):
#         mistakes = self.db.get_mistake(user_id)
#         feedback = "\n".join([f"{m[0]}->{m[1]}" for m in mistakes]) or "no mistakes recorded"

#         return f"your mistakes:\n{feedback}"
    



import os
import re
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain_google_genai import GoogleGenerativeAI
from database import Database

# Load environment variables
load_dotenv()

class Chatbot:
    def __init__(self):
        # Initialize AI Model (Using Google Gemini 1.5 Pro)
        self.model = GoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=os.getenv("GOOGLE_API_KEY"))
        self.db = Database()

    def start_conversation(self, user_id, native_language, learning_language, level):
        """Registers user and starts language learning session."""
        self.db.add_user(user_id, native_language, learning_language, level)
        return f"Great! Let's start learning {learning_language}. I will guide you and track your mistakes."

    # def chat(self, user_id, user_input):
    #     """Handles chat interaction and detects mistakes."""
    #     messages = [
    #         SystemMessage(content="You are a language tutor that helps users learn a new language. "
    #                               "If the user makes a grammatical mistake, provide a correction in this format: "
    #                               "'Correction: {corrected sentence}'"),
    #         HumanMessage(content=user_input)
    #     ]
    #     response = self.model.invoke(messages)

    #     ai_response = response.content if hasattr(response, "content") else response

    #     # Extract correction using regex
    #     match = re.search(r'Correction:\s*(.*)', ai_response)
    #     if match:
    #         corrected_sentence = match.group(1)
    #         self.db.log_mistake(user_id, user_input, corrected_sentence)  # Store mistake

    #     return ai_response
    import re

    def chat(self, user_id, user_input):
        """Handles chat interaction and detects mistakes while responding naturally."""
        messages = [
            SystemMessage(content="You are a language tutor that helps users learn a new language. "
                                "If the user makes a mistake, provide a correction in this format: "
                                "'Correction: {corrected sentence}'. After that, reply naturally."),
            HumanMessage(content=user_input)
        ]
        response = self.model.invoke(messages)

        ai_response = response.content if hasattr(response, "content") else response

        # Extract the correction using regex
        match = re.search(r'Correction:\s*(.*)', ai_response)
        
        if match:
            corrected_sentence = match.group(1)
            self.db.log_mistake(user_id, user_input, corrected_sentence)  # Store mistake

            # Remove correction from AI response to keep conversation natural
            ai_response = ai_response.replace(match.group(0), "").strip()

        return ai_response

    def get_feedback(self, user_id):
        """Retrieves user's mistake history."""
        mistakes = self.db.get_mistakes(user_id)
        feedback = "\n".join([f"{m[0]} -> {m[1]}" for m in mistakes]) if mistakes else "No mistakes recorded."
        return f"Your mistakes:\n{feedback}"
