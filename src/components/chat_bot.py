import google.generativeai as genai
import asyncio


class Chatbot:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash-002",
            system_instruction="You are a helpful and knowledgeable assistant.Your name is 'Gemini'.",
        )
        self.chat_session = self.model.start_chat(history=[])

    def _remove_asterisks(self, text):
        return text.replace("**" and "*", "")

    async def generate_response(self, user_query):
        """Hàm bất đồng bộ để giao tiếp với AI và nhận phản hồi."""
        response = await asyncio.to_thread(self.chat_session.send_message, user_query)
        model_response = response.text
        model_response = self._remove_asterisks(model_response)
        self.chat_session.history.append({"role": "user", "parts": [user_query]})
        self.chat_session.history.append({"role": "model", "parts": [model_response]})
        return model_response
