from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# 1. Database Configuration
# 'cric_db_mysql' chya jagi tumhi 'StudentInfo' db vapru shakta
URL = "mysql+pymysql://root:18Bh%40#rati@localhost/cric_db_mysql"
engine = create_engine(URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# 2. Table Name: StudentRecord
class StudentRecord(Base):
    __tablename__ = "StudentRecord"
    
    # Roll No Primary Key
    rollNo = Column(Integer, primary_key=True)
    # Student Name
    studentName = Column(String(100))
    # Student Standard (Std)
    studentStd = Column(Integer)
    # Marks (Optional - thevle aahet jar garaj lagli tar)
    marks = Column(Float)

# Table automatically create hoto
Base.metadata.create_all(engine)

app = FastAPI()

# Database Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- CRUD Operations ---

# GET: Sagle records baghnyasathi
@app.get("/students")
def get_students(db: Session = Depends(get_db)):
    return db.query(StudentRecord).all()

# POST: Navin student record add karnyathi
@app.post("/students")
def add_student(rollNo: int, name: str, std: int, marks: float, db: Session = Depends(get_db)):
    new_s = StudentRecord(rollNo=rollNo, studentName=name, studentStd=std, marks=marks)
    db.add(new_s)
    db.commit()
    return {"message": f"Record for {name} saved successfully!"}

# DELETE: Record delete karnyathi
@app.delete("/students/{rollNo}")
def delete_student(rollNo: int, db: Session = Depends(get_db)):
    record = db.query(StudentRecord).filter(StudentRecord.rollNo == rollNo).first()
    if record:
        db.delete(record)
        db.commit()
        return {"message": "Record deleted"}
    return {"error": "Not found"}