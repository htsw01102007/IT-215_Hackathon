from database import Base
from sqlalchemy import Column, Integer, String

class StudentModel(Base):
    __tablename__ = "student"
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    full_name = Column(String(255), nullable=False)
    class_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone_number = Column(String(255), nullable=False)
