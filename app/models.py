from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


user_loan = db.Table("user_loan",
     db.Column("loan_id", db.Integer, db.ForeignKey("loanapp.id")),
     db.Column("user_id", db.Integer, db.ForeignKey("user.id"))
)

class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String)
    llc_name = db.Column(db.String)
    phone = db.Column(db.String)
    referral = db.Column(db.String)
    email = db.Column(db.String, unique=True, index=True)
    password = db.Column(db.String)
    loan = db.relationship("LoanApp", secondary=user_loan, backref="client", lazy="dynamic")
       
    def __repr__(self):
        return f'<User: {self.email} | {self.id}>'
    
    def __str__(self):
        return f'<User: {self.email} | {self.full_name} {self.llc_name}>'

    def hash_password(self, original_password):
        return generate_password_hash(original_password)

    def check_hashed_password(self, login_password):
        return check_password_hash(self.password, login_password)

    def save(self):
        db.session.add(self) # add the userr to the session
        db.session.commit() # save the stuff in the session to the database

    def from_dict(self, data):
        self.full_name = data['full_name']
        self.llc_name = data['llc_name']
        self.phone = data['phone']
        self.referral = data['referral']
        self.email = data['email']
        self.password = self.hash_password(data['password'])
            
           
    def delete(self):
        db.session.delete(self) # remove the user from the session
        db.session.commit() # save the stuff in the session to the database

    

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class LoanApp(db.Model):
    __tablename__ = 'loanapp'

    id = db.Column(db.Integer, primary_key=True)
    loan_type = db.Column(db.String)
    loan_amount = db.Column(db.Integer)
    property_type = db.Column(db.String)
    property_address = db.Column(db.String)
    under_contract = db.Column(db.String)
    close_date = db.Column(db.DateTime)
    
    
    
    def __repr__(self):
        return f'<LoanApp: {self.loan_type}> | Id: {self.id}'

    def from_dict(self, loan_dict):
        self.loan_type = loan_dict['loan_type']
        self.loan_amount = loan_dict['loan_amount']
        self.property_type = loan_dict['property_type']
        self.property_address = loan_dict['property_address']
        self.under_contract = loan_dict['under_contract']
        self.close_date = loan_dict['close_date']
        

    def save_loan(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_loan(self):
        db.session.delete(self)
        db.session.commit()