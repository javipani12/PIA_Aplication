from dotenv import load_dotenv


class Credentials:
    def __init__(self, OPENAI, DALLE, LEONARDO):
        self.OPENAI = OPENAI
        self.DALLE = DALLE
        self.LEONARDO = LEONARDO

    def load_keys(self):
        load_dotenv()

