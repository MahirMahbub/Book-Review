import logging
import os
import textwrap
from typing import Any

from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload, subqueryload
from sqlalchemy_pagination import paginate, Page
from starlette import status

from app.cruds.book import BookCrud
# from app.data_classes import Bookdto
from app.cruds.user_review import UserReviewCrud
from db import models


class BookService(object):
    def get_paginated_book_list(self, db: Session, page_size: int, page_number: int):
        try:
            crud_list_object = BookCrud(db).gets_query
            for i in crud_list_object:
                print(i.user_associations)
                print(i.user)
            __pagination_obj: Page = paginate(crud_list_object, page=page_number, page_size=page_size)
            # return __pagination_obj
        except AttributeError as e:
            logging.exception("Attribute Error occurred")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=str(e))

        if __pagination_obj:
            try:
                book_manipulated = self.__get_paginated_book_list_with_book_details(db=db,
                                                                                    book_data_list=__pagination_obj.items)

                __pagination_obj.items = book_manipulated
                # return __pagination_obj
                return {
                    'found': True if __pagination_obj.items else False,
                    'items': __pagination_obj.items,
                    'next_page': __pagination_obj.next_page,
                    'previous_page': __pagination_obj.previous_page,
                    'total_items': __pagination_obj.total,
                    'pages': __pagination_obj.pages,
                    'has_next': __pagination_obj.has_next,
                    'has_previous': __pagination_obj.has_previous
                }
            except Exception as e:
                logging.exception("Error occurred")
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail="Error occurred")
        else:
            logging.exception("Pagination failed")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Pagination failed")

    # def manipulate_book_query(self, query_object):

    def __get_paginated_book_list_with_book_details(self, db, book_data_list):
        manipulated_book_list = []
        for book in book_data_list:
            print(book.name)
            avg_rating = None
            total_rated = 0
            total_reviewed = 0
            sum_rating = 0
            for association_data in book.user_associations:
                if association_data.rating is not None:
                    sum_rating += association_data.rating
                    total_rated += 1

                if association_data.review is not None:
                    total_reviewed += 1

            if total_rated > 0:
                avg_rating = sum_rating / total_rated
            book = self.additional_data_injection(avg_rating, book, total_rated, total_reviewed)
            manipulated_book_list.append(book)

        return manipulated_book_list

    @staticmethod
    def additional_data_injection(avg_rating, book, total_rated, total_reviewed):
        book.total_rated = total_rated
        book.average_rating = avg_rating
        book.total_reviewed = total_reviewed
        book.url = os.environ['APP_URL'] + "book/" + str(book.id)
        return book

    def get_book_details(self, db, id_):
        book_list = []
        association_list = UserReviewCrud(db).gets_by_book_id(id_)
        book = association_list[0].book
        book.user_rate_review = []
        total_reviewed = 0
        total_rated = 0
        for assc in association_list:
            user_name = assc.user.first_name + " " + assc.user.last_name
            rating = assc.rating
            review = assc.review
            if review is not None:
                total_reviewed += 1
            if rating is not None:
                total_rated += 1
            book.user_rate_review.append({"user_name": user_name,
                                          "rating": rating,
                                          "review": review})
            book.total_rated = total_rated
            book.total_reviewed = total_reviewed
        # book_detail = BookCrud(db).get_query(id_).options(joinedload(models.Book.user)).all()
        return book
