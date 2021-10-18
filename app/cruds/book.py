from sqlalchemy.orm import Session

from app.cruds.table_repository import TableRepository
from db import models


class BookCrud(TableRepository):
    def __init__(self, db: Session):
        super().__init__(db=db, entity=models.Book)


