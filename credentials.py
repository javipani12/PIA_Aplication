import os
from enum import StrEnum

class Credentials(StrEnum):
    OPENAI = os.environ["OPENAI"]
    DALLE = os.environ["DALLE"]
    LEONARDO = os.environ["LEONARDO"]



