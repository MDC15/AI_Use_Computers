import os
import datetime
import webbrowser as wb


class CommandProcessor:
    def __init__(self, voice_handler, chatbot):
        self.voice_handler = voice_handler
        self.chatbot = chatbot
        
        
    async def get_time(self):
        """Hàm bất đồng bộ để trả lời thời gian hiện tại."""
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        self.voice_handler.speak(f"The time is {current_time}")
        
        
    async def process_command(self, command):
        """Hàm bất đồng bộ để xử lý các lệnh người dùng."""
        if "google" in command:
            self.voice_handler.speak("What should I search?")
            search_query = await self.voice_handler.listen()
            if search_query != "none":
                url = f"https://google.com/search?q={search_query}"
                wb.get().open(url)
                self.voice_handler.speak(f"Here is your {search_query} on Google")
        elif "youtube" in command:
            self.voice_handler.speak("What should I search?")
            search_query = await self.voice_handler.listen()
            if search_query != "none":
                url = f"https://youtube.com/search?q={search_query}"
                wb.get().open(url)
                self.voice_handler.speak(f"Here is your {search_query} on YouTube")
        elif "see you" in command:
            self.voice_handler.speak("Goodbye!")
            return False
        elif "open video" in command:
            video_path = r"C:\Users\Admin\Desktop\test\meme.mp4"
            if os.path.exists(video_path):
                os.startfile(video_path)
            else:
                self.voice_handler.speak("Sorry, I couldn't find the video.")
        elif "time" in command:
            await self.get_time()
        else:
            response = await self.chatbot.generate_response(command)
            self.voice_handler.speak(response)
        return True


