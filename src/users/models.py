from application import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(250))
    active = db.Column(db.Boolean(), default=True, nullable=False)
    
    def __init__(self,username, email,password):
        self.username = username
        self.email = email
        self.password = password
    # def set_password(self, password):
    #     """Create hashed password."""
    #     self.password = generate_password_hash(password, method='sha256')
    # def check_password(self,password):
    #     """Create hashed Password"""
    #     return check_password_hash(self.password, password)
    
    def __repr__(self):
        return '<User {}> with email {}'.format(self.id, self.email)