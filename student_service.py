from sqlalchemy.orm import Session
from model import StudentModel
from schemas import StudentRequest

#API5
def create_student_service(new_student: StudentRequest, db: Session):
    new_student_db = StudentModel( 
        full_name = new_student.full_name,
        class_name = new_student.class_name,
        email = new_student.email,
        phone_number = new_student.phone_number
    )
    db.add(new_student_db)
    db.commit()
    db.refresh(new_student_db)
    return new_student_db

#API2
def get_all_service(db: Session):
    return db.query(StudentModel).all()

#API4
def get_student_by_id_service(student_id: int, db: Session):
    return db.query(StudentModel).filter(StudentModel.id == student_id).first()

#API6
def update_student_by_id_service(student_id: int, update_data: StudentRequest, db: Session):
    find_student_db = db.query(StudentModel).filter(StudentModel.id == student_id).first()
    if find_student_db:
        find_student_db.full_name = update_data.full_name
        find_student_db.class_name = update_data.class_name
        find_student_db.email = update_data.email
        find_student_db.phone_number = update_data.phone_number
        db.commit()
        db.refresh(find_student_db)
    return find_student_db

#API7
def delete_student_service(student_id: int, db: Session):
    find_student_db = db.query(StudentModel).filter(StudentModel.id == student_id).first()
    if find_student_db:
        db.delete(find_student_db)
        db.commit()
        return True
    return False

#API3
def search_student_by_class_service(keyword: str, db: Session):
    return db.query(StudentModel).filter(StudentModel.class_name.like(f"%{keyword}%")).all()