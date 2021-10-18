from app.data_classes import Bookdto
from db import models


class BookParser:

    @staticmethod
    def parse_as_news_dto(news: models.Book) -> Bookdto:
        news_dto: Bookdto = Bookdto(
        )

        return news_dto