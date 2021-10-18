from typing import Optional, List, Any

from fastapi_camelcase import CamelModel
from pydantic import BaseModel


class BookBase(CamelModel):
    id: int
    name: str
    isbn: str
    author_name: str
    total_rated: Optional[int] = None
    total_reviewed: Optional[int] = None


class BookBaseForListResponse(BookBase, CamelModel):
    url: str = None
    average_rating: Optional[float] = None

    class Config:
        orm_mode = True


class BookListPaginatedResponse(CamelModel):
    items: List[BookBaseForListResponse]
    # items: Any
    previous_page: Optional[int] = None
    next_page: Optional[int] = None
    has_previous: bool
    has_next: bool
    total_items: int
    pages: int


class UserReviewResponse(CamelModel):
    user_name: str
    rating: Optional[int] = None
    review: Optional[str] = None


class BookDetailResponse(BookBase, CamelModel):
    user_rate_review: Optional[List[UserReviewResponse]] = None

    class Config:
        orm_mode = True
