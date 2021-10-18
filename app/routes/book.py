from typing import Optional

from fastapi import Depends, Query, Path
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.orm import Session

from app import schemas
from app.depends.db_depend import get_db
from app.services.book import BookService
from app.utils import catch_not_implemented_exception

router = InferringRouter()


@cbv(router)
class Book:
    db: Session = Depends(get_db)

    @router.get("/book", response_model= schemas.BookListPaginatedResponse)
    @catch_not_implemented_exception
    def get_paginated_book_list(self, page_size: Optional[int] = Query(5), page_number: Optional[int] = Query(1)):
        return BookService().get_paginated_book_list(db=self.db, page_size=page_size, page_number=page_number)

    @router.get("/book/{id}", response_model=schemas.BookDetailResponse)
    @catch_not_implemented_exception
    def get_book_detail(self, id_: int = Path(..., alias="id")):
        return BookService().get_book_details(db=self.db, id_= id_)
