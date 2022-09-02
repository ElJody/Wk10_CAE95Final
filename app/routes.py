from flask import redirect, render_template, request, url_for, flash
from app import app, db
from flask_login import login_user, login_required, logout_user, current_user
from app.forms import LoginForm, RegisterForm, ApplyForm, EditProfileForm
from .models import User, LoanApp
 


@app.route('/', methods=['GET'])
def index():
    return render_template('home.html.j2')

@app.route('/why', methods=['GET'])
def why():
    return render_template('index.html.j2')

@app.route('/what', methods=['GET'])
def what():
    return render_template('whatis.html.j2')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        print('login POST success')
        if form.validate_on_submit():
            email = form.email.data.lower()
            print(email)
            password = form.password.data
            print(password)

            u = User.query.filter_by(email=email).first()
            print('form validated!!'+str(u))
            if u is None or not u.check_hashed_password(password):
                flash("Incorrect Email/password Combo", "warning")
                return render_template('login.html.j2', form=form)
            print('we have u')
            print(User().hash_password(password))
            print('u.check printed')
            flash('Successfully logged in','warning')
            login_user(u)
            return redirect(url_for('index'))

    return render_template('login.html.j2', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form=RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        try:
            full_name = form.full_name.data.lower()
            llc_name = form.llc_name.data.lower()
            phone = form.phone.data
            referral = form.referral.data.lower()
            email=form.email.data.lower()
            password =form.password.data
            new_user = User(full_name=full_name, llc_name=llc_name, phone=phone, referral=referral,email=email,password=User().hash_password(password))
            db.session.add(new_user)
            db.session.commit()
        except:
            flash('Something went wrong!', "alert")
            return redirect(url_for('register'))
        flash('You are now registered!', "warning")
        return redirect(url_for('login'))
    return render_template('register.html.j2', form=form)

@app.route('/apply', methods=['GET', 'POST'])
@login_required
def apply():
    form=ApplyForm()
    if request.method == 'POST' and form.validate_on_submit():
        try:
            loan_type = form.loan_type.data.lower()
            loan_amount = form.loan_amount.data
            property_type = form.property_type.data.lower()
            property_address = form.property_address.data
            under_contract = form.under_contract.data
            close_date = form.close_date.data
            new_loan = LoanApp(loan_type=loan_type, loan_amount=loan_amount, property_type=property_type, property_address=property_address, under_contract=under_contract, close_date=close_date)
            current_user.loan.append(new_loan)
            db.session.add(new_loan)
            db.session.commit()
        except:
            flash('Something went wrong!', "alert")
            return redirect(url_for('apply'))
        flash('Someone Will Contact You Soon!', "warning")
        return redirect(url_for('index'))
    return render_template('apply.html.j2', form=form)




@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(obj=current_user)

    if request.method == 'POST' and form.validate_on_submit():
        edited_user_data={
                "full_name":form.full_name.data.title(),
                "llc_name":form.llc_name.data.title(),
                "phone":form.phone.data,
                "referral":form.referral.data.lower(),
                "email":form.email.data.lower(),
                "password":form.password.data,

            }
        print(edited_user_data)
        user = User.query.get(current_user.id)
        if user and user.email != current_user.email:
            flash('Email already exists!', 'danger')
            return redirect(url_for('edit_profile'))
        try:
            current_user.from_dict(edited_user_data)
            current_user.save()
            flash('Profile updated!', 'success')
        except:
            flash('Error updating profile!', 'danger')
            return redirect(url_for('edit_profile'))
        return redirect(url_for('index'))
    return render_template('edit_profile.html.j2', form=form)

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('Logout successful', 'info')
    return redirect(url_for('index'))


# #                app.login_user(u)
#                 if login_user(u):
#                     print('login success')
#                     return redirect(url_for('index'))
#                 else:
#                     print('login failed')
#                     return redirect(url_for('login'))
#                return redirect(url_for('index'))