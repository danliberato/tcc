from src.domain.alert import AlertRequest, AlertBase, AlertResponse


def alert_request_to_base(request: AlertRequest):
    return AlertBase(movie_name=request.movie_name, email=request.email, date=request.date,
                     title=request.title, category=request.category, image_url=request.image_url)


def alert_base_to_response(base: AlertBase):
    return AlertResponse(id=base.id, movie_name=base.movie_name, email=base.email, date=base.date,
                         title=base.title, category=base.category, image_url=base.image_url)

