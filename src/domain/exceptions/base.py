class ArticlePlatformException(Exception):
    @property
    def message(self) -> str:
        return "Article Platform exception occurred."
