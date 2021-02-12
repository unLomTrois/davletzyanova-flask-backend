from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, Date, VARCHAR

Base = declarative_base()

class Note(Base):
    __tablename__ = "note"

    id = Column(
        Integer, nullable=False, unique=True, primary_key=True, autoincrement=True
    )
    title = Column(VARCHAR(255))
    description = Column(Text)

    def __repr__(self):
        return "<Note(title='{}', description='{}')>".format(
            self.title, self.description
        )

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
