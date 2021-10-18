from sqlalchemy.orm import Session

from app.cruds.table_repository import TableRepository
from db import models


class UserReviewCrud(TableRepository):
    def __init__(self, db: Session):
        super().__init__(db=db, entity=models.UserReview)

    def gets_by_book_id(self, book_id):
        return self.db.query(models.UserReview).filter(models.UserReview.book_id == book_id).all()