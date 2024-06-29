from application import db
from datetime import datetime
import enum


class TaskStatus(enum.Enum):
    Open = "Open"
    In_Progress = "Progress"
    Closed = "Close"


class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    description = db.Column(db.Text, nullable=False)
    # status = db.Column(db.Enum(TaskStatus), default=TaskStatus.Open)
    status = db.Column(db.Enum(TaskStatus), default="Open")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                        nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, title, description, user_id, due_date):
        self.title = title
        self.description = description
        self.user_id = user_id
        self.due_date = due_date

    def __repr__(self):
        return f"{self.id} by {self.user_id} with status {self.status}"


class BuddyContact(db.Model):
    __tablename__ = "buddy_info"
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    first_buddy_email = db.Column(db.String(128),  nullable=False)
    second_buddy_email = db.Column(db.String(128))  # Optional second
