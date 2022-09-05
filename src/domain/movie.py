from uuid import uuid4

from pydantic import BaseModel


class Movie(BaseModel):
    name: str
    description: str = None
    genre: str = None
    synopsis: str = None

    def __int__(self, name, description, genre, synopsis):
        self.name = name
        self.description = description
        self.genre = genre
        self.synopsis = synopsis

