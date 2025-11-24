from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserCreate

# Service method to create user
def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Fetch all users
def get_users(db: Session):
    return db.query(User).all()

# Fetch a single user by ID
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Update user details
def update_user(db: Session, user_id: int, user_data: UserCreate):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.name = user_data.name
        user.email = user_data.email
        db.commit()
        db.refresh(user)
        return user
    return None

# Delete user
def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False
