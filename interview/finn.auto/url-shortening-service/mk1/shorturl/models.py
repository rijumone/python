import datetime
from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class URLsMap(Base):
    __tablename__ = 'urls_map'

    id = Column(Integer, primary_key=True)
    short_url = Column(Text, nullable=True)
    full_url = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self) -> str:
        return f'''<URLsMap( 
            id={self.id},
            short_url={self.short_url},
            full_url={self.full_url},
            created_at={self.created_at},
        ) >'''
