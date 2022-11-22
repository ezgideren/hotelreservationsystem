from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base


class account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    #email = Column(String, unique=True, index=True)
    #hashed_password = Column(String)
   

    
