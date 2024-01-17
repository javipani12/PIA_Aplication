import os
from dotenv import load_dotenv

class Credentials():
    def __init__(self):
        load_dotenv()
        self.openai_key = os.getenv("OPENAI")
        self.leonardo_key = os.getenv("LEONARDO")
        self.laguage = os.getenv("LANGUAGE")

