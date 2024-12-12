# Main app

# import Libs
import os
import sys
import asyncio
from dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

# Import components
from components.voice_handler import VoiceHandler
from components.chat_bot import Chatbot
from components.command_processor import CommandProcessor


async def main():
    # Load environment variables
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    # Init Components
    voice_handler = VoiceHandler()
    chatbot = Chatbot(api_key=api_key)
    command_processor = CommandProcessor(voice_handler, chatbot)

    # Chào người dùng
    voice_handler.speak("What can I help with?")

    while True:
        command = await voice_handler.listen()
        if command != "none":
            should_continue = await command_processor.process_command(command)
            if not should_continue:
                break


if __name__ == "__main__":
    asyncio.run(main())
