from pydantic import BaseModel
from model import Book


class BookDto(BaseModel):
    title: str
    author: str

    def toBook(self):
        return Book(title=self.title, author=self.author)