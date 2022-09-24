import datetime

from pydantic import BaseModel


class AlertBase(BaseModel):
    movie_name: str
    email: str
    date: datetime.date
    title: str
    category: str
    image_url: str

    def __int__(self, movie_name, email, date, title, category, image_url):
        self.movie_name = movie_name
        self.email = email
        self.date = date
        self.title = title
        self.category = category
        self.image_url = image_url


class AlertRequest(AlertBase):
    pass


class AlertResponse(AlertBase):
    id: str
    pass


