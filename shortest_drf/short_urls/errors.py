class Error(Exception):
    pass


class InvalidSlugGenerationError(Error):
    def __init__(self, url: str):
        self.url: str = url

    def __str__(self) -> str:
        return f'Could not generate unique slug for {self.url}'
