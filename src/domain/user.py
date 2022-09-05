from pydantic import BaseModel


class User(BaseModel):
    id: str
    name: str
    email: str
    birthdate: str

    def __int__(self, name, birthdate, email):
        self.name = name
        self.birthdate = birthdate
        self.email = email



