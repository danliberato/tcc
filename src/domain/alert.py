import datetime
from typing import Optional

from pydantic import BaseModel


class AlertBase(BaseModel):
    id: Optional[str] = None
    movie_name: str
    email: str
    date: str
    title: str
    category: str
    image_url: str

    def __int__(self):
        super.__init__(movie_name=self.movie_name, email=self.email, date=self.date,
                           title=self.title, category=self.category, image_url=self.image_url)


class AlertRequest(AlertBase):
    def __int__(self):
        AlertBase.__init__(movie_name=self.movie_name, email=self.email, date=self.date,
                           title=self.title, category=self.category, image_url=self.image_url)


class AlertResponse(BaseModel):
    id: str

    def __int__(self):
        AlertBase.__init__(movie_name=self.movie_name, email=self.email, date=self.date,
                           title=self.title, category=self.category, image_url=self.image_url)
