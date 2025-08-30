from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Group(Base):
    __tablename__ = 'groups'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    
    # Зв'язок з студентами
    students = relationship("Student", back_populates="group")

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String(100), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=False)
    
    # Зв'язки
    group = relationship("Group", back_populates="students")
    grades = relationship("Grade", back_populates="student")

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String(100), nullable=False)
    
    # Зв'язок з предметами
    subjects = relationship("Subject", back_populates="teacher")

class Subject(Base):
    __tablename__ = 'subjects'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=False)
    
    # Зв'язки
    teacher = relationship("Teacher", back_populates="subjects")
    grades = relationship("Grade", back_populates="subject")

class Grade(Base):
    __tablename__ = 'grades'
    
    id = Column(Integer, primary_key=True, index=True)
    grade = Column(Float, nullable=False)  # Оцінка (наприклад, 4.5, 5.0)
    date_received = Column(DateTime, default=func.now())
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.id'), nullable=False)
    
    # Зв'язки
    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")