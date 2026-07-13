from fastapi import FastAPI, HTTPException, Depends, status
from database import Base, engine, get_database
from sqlalchemy.orm import Session
from schemas import StudentRequest, StudentResponse
from student_service import *

Base.metadata.create_all(bind=engine)

app = FastAPI

@app.get("/")
def handle_check():
    return "API đang chạy"

@app.post("/students", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def handle_create_student(new_student:StudentRequest, db:Session=Depends(get_database)):
    student_created = create_student_service(new_student,db)
    return student_created

@app.get("/students", response_model=list[StudentResponse], status_code=status.HTTP_200_OK)
def handle_get_all_student(db:Session=Depends(get_database)):
    student_list = get_all_service(db)
    return student_list

@app.get("/students/search",response_model=list[StudentResponse],status_code=status.HTTP_200_OK)
def handle_search_student(class_name:str, db:Session=Depends(get_database)):
    results = search_student_by_class_service(class_name,db)
    return results

@app.get("/students/{student_id}", response_model=StudentResponse, status_code=status.HTTP_200_OK)
def handle_get_student_by_id(student_id: int, db: Session = Depends(get_database)):
    student = get_student_by_id_service(student_id=student_id, db=db)
    if not student:
        raise HTTPException(status_code=404, detail="Không tìm thấy học sinh")
    return student

@app.delete("/students/{student_id}", status_code=status.HTTP_200_OK)
def handle_delete_student(student_id: int, db: Session = Depends(get_database)):
    is_success = delete_student_service(tudent_id=student_id, db=db)
    if not is_success:
        raise HTTPException(status_code=404, detail="Không thể xóa, ID đội tuyển không tồn tại")
    return {"message": "Xóa thông tin đội tuyển thành công"}