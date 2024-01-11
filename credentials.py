from dotenv import load_dotenv
import os

class Credentials:
    
    def load_keys(self):
        load_dotenv()
    
    def __init__(self, OPENAI, DALLE, LEONARDO):
        self.load_keys()
        
        self.OPENAI = os.getenv("OPENAI")
        self.DALLE = os.getenv("DALLE")
        self.LEONARDO = os.getenv("LEONARDO")



