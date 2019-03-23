import db

class todo(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, nullable=False, primary_key = True)
    task_name = db.column(db.String(64), nullable=False)
    description = db.column(db.String(64), nullable = False)
    date=db.column(db.DateTime(timezone=True), nullable=False)
    completed=db.column(db.Integer, nullable =False)
    