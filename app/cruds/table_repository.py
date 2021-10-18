from typing import TypeVar, Generic

from sqlalchemy.orm import Session

T = TypeVar('T')


class TableRepository:
    entity: Generic[T] = None
    db: Session = NotImplementedError

    def __init__(self, db: Session, entity: Generic[T]):
        self.db: Session = db
        self.entity: Generic[T] = entity

    def store(self, item):
        item = item.dict(exclude_unset=True)
        model_object = self.entity(**item)
        self.db.add(model_object)
        return model_object

    def get(self, id_: int):
        return self.db.query(self.entity).filter(self.entity.id == id_).first()

    @property
    def get_query(self, id_: int):
        return self.db.query(self.entity).filter(self.entity.id == id_)

    def gets(self):
        return self.gets_query.all()

    @property
    def gets_query(self):
        return self.db.query(self.entity)

    def update(self, id_, item):
        item_dict = item.dict(exclude_unset=True)
        return self.db.query(self.entity).filter(self.entity.id == id_).update(item_dict)
