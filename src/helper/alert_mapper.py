from src.domain.alert import AlertRequest, AlertBase, AlertResponse


def alert_request_to_base(request: AlertRequest):
    return AlertBase(movie_id=request.movie_id, email=request.email, date=request.date,
                     title=request.title, category=request.category, image_url=request.image_url)


def alert_base_to_response(base: AlertBase):
    return AlertResponse(movie_id=base.movie_id, email=base.email, date=base.date,
                         title=base.title, category=base.category, image_url=base.image_url)

