from pydantic import BaseModel


class AlertBase(BaseModel):
    movie_id: str
    email: str
    date: str
    title: str
    category: str
    image_url: str

    def __int__(self):
        super.__init__(movie_id=self.movie_id, email=self.email, date=self.date,
                       title=self.title, category=self.category, image_url=self.image_url)


class AlertRequest(AlertBase):
    def __int__(self):
        AlertBase.__init__(movie_id=self.movie_id, email=self.email, date=self.date,
                           title=self.title, category=self.category, image_url=self.image_url)


class AlertResponse(AlertBase):
    pass
