import pyttsx3
import speech_recognition as sr
import asyncio


class VoiceHandler:
    def __init__(self):
        voice_sped = 150    # Điều chỉnh tốc độ nói
        self.chatbot = pyttsx3.init()
        voices = self.chatbot.getProperty("voices")
        self.chatbot.setProperty("voice", voices[1].id)  # Chọn giọng nói
        self.chatbot.setProperty("rate", voice_sped)  

    def speak(self, audio):
        """Hàm bất đồng bộ để chatbot nói."""
        print(f"\nChatbot: {audio}")
        self.chatbot.say(audio)
        self.chatbot.runAndWait()

    async def listen(self):
        """Hàm bất đồng bộ để lắng nghe lệnh từ người dùng."""
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.pause_threshold = 1
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("> Listening...")
            try:
                audio = await asyncio.to_thread(recognizer.listen, source)
                query = await asyncio.to_thread(
                    recognizer.recognize_google_cloud, audio, language="en-US"
                )
                print(f"You: {query}")
                return query.lower()
            except sr.UnknownValueError:
                return "none"
            except sr.RequestError:
                self.speak("Network error. Please check your internet connection.")
                return "none"
