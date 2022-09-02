from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField
from wtforms.validators import DataRequired,Email, EqualTo, ValidationError
from app.models import * 

class LoginForm(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    full_name = StringField('First & Last Name', validators=[DataRequired()])
    llc_name = StringField('Name of LLC', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    # phone = FormField('Phone Number', validators=[DataRequired()])
    referral = StringField('Contigo Agent or Referral Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
        validators=[DataRequired(), EqualTo('password', message='Passwords Must Match')])
    submit = SubmitField('Register')

    def validate_email(form, field):
        same_email_user = User.query.filter_by(email = field.data).first()
        if same_email_user:
            print('Email is Already in Use')
            return ValidationError('Email is Already in Use')


class EditProfileForm(FlaskForm):
    full_name = StringField('First & Last Name', validators=[DataRequired()])
    llc_name = StringField('Name of LLC', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    referral = StringField('Contigo Agent or Referral Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
         validators=[DataRequired(), EqualTo('password', message='Passwords Must Match')])
    submit = SubmitField('Edit Profile')

class ApplyForm(FlaskForm):
    loan_type = StringField('Loan Type', validators=[DataRequired()])
    loan_amount = DecimalField('Loan Amount', validators=[DataRequired()])
    property_type = StringField('Property Type', validators=[DataRequired()])
    property_address = StringField('Property Address', validators=[DataRequired()])
    under_contract = StringField('Under Contract?', validators=[DataRequired()])
    close_date = StringField('Close Date', validators=[DataRequired()])
    
    
    # password = PasswordField('Password', validators=[DataRequired()])
    # confirm_password = PasswordField('Confirm Password', 
    #      validators=[DataRequired(), EqualTo('password', message='Passwords Must Match')])
    submit = SubmitField('Get Approved')




