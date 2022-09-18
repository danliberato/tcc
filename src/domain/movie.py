
from pydantic import BaseModel


class MovieBase(BaseModel):
    id: str
    name: str
    description: str = None
    genre: str = None
    synopsis: str = None
    user_id: str
    movie_url: str

    def __int__(self, name, description, genre, synopsis, user_id):
        self.name = name
        self.description = description
        self.genre = genre
        self.synopsis = synopsis
        self.user_id = user_id


class MovieRequest(BaseModel):
    name: str
    description: str = None
    genre: str = None
    synopsis: str = None
    user_id: str

    def __int__(self):
        MovieBase.__int__(name=self.name, description=self.description, genre=self.genre, synopsis=self.synopsis,
                          user_id=self.user_id)


class MovieResponse(BaseModel):
    id: str
    # name: str
    # description: str = None
    # genre: str = None
    # synopsis: str = None
    # user_id: str
    movie_url: str

    # def __int__(self):
    #     MovieBase.__int__(id=self.id, name=self.name, description=self.description, genre=self.genre, synopsis=self.synopsis,
    #                       user_id=self.user_id)
    def __int__(self):
        MovieBase.__int__(id=self.id, movie_url=self.movie_url)
