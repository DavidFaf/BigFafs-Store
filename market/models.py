from market import db, bcrypt
from market import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), unique=True, nullable=False)
    email_address = db.Column(db.String(length=50), nullable= False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1200)
    items = db.relationship('Item', backref='owned_user', lazy=True)    

    # def __repr__(self):
    #     return f'User {self.username}'

    @property
    def prettier_budget(self):
        return f"{self.budget:,}"

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_password):
        self.password_hash = bcrypt.generate_password_hash(plain_password).decode('utf-8')

    def password_checker(self, password_to_check):
        return bcrypt.check_password_hash(self.password_hash,password_to_check)


class Item(db.Model):
    id= db.Column(db.Integer(), primary_key= True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    serial_number = db.Column(db.String(length=10), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(1024), unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))


    def __repr__(self):
        return f'Item {self.name}'
