from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# Database URL (Tumcha password %40 sobat)
URL = "mysql+pymysql://root:18Bh%40#rati@localhost/cric_db_mysql"
engine = create_engine(URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# 1. Student Model define kara
class Student(Base):
    __tablename__ = "students"
    rollNo = Column(Integer, primary_key=True)
    name = Column(String(100))
    marks = Column(Float)

# Table create kara
Base.metadata.create_all(engine)

app = FastAPI()

# Database Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Student CRUD Operations ---

# GET: Saglya students chi list
@app.get("/students")
def read_students(db: Session = Depends(get_db)):
    return db.query(Student).all()

# POST: Navin student add kara
@app.post("/students")
def create_student(rollNo: int, name: str, marks: float, db: Session = Depends(get_db)):
    new_student = Student(rollNo=rollNo, name=name, marks=marks)
    db.add(new_student)
    db.commit()
    return {"message": f"Student {name} added successfully!"}

# UPDATE: Student che marks update kara
@app.put("/students/{rollNo}")
def update_marks(rollNo: int, new_marks: float, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.rollNo == rollNo).first()
    if student:
        student.marks = new_marks
        db.commit()
        return {"message": "Marks updated successfully!"}
    return {"error": "Student not found"}

# DELETE: Student la kadhun taka
@app.delete("/students/{rollNo}")
def delete_student(rollNo: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.rollNo == rollNo).first()
    if student:
        db.delete(student)
        db.commit()
        return {"message": "Student record deleted"}
    return {"error": "Not found"}