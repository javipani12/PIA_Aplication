import os
from enum import StrEnum

class Credentials(StrEnum):
    OPENAI = os.environ["OPENAI"]
    LEONARDO = os.environ["LEONARDO"]
