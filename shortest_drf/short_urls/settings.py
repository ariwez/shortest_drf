import os

SLUG_LENGTH: int = int(os.getenv('SLUG_LENGTH', 4))
SLUG_MAX_RETRIES: int = int(os.getenv('SLUG_MAX_RETRIES', 10))
