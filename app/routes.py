from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.forms import RegistrationForm, LoginForm
from app.models import User

main = Blueprint("main", __name__)

# Home route
@main.route('/')
def home():
    return render_template('home.html')

# About route
@main.route('/about')
def about():
    return render_template('about.html')

# Contact route
@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter(
            (User.username == form.username.data) | (User.email == form.email.data)
        ).first()

        if existing_user:
            flash('Username or email already exists.', 'danger')
            return redirect(url_for('main.register'))

        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash('Registration successful. Please login.', 'success')
        return redirect(url_for('main.login'))

    return render_template('register.html', form=form)

# Route for creating posts
@main.route('/create-post', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        # Logic for creating a post
        flash('Post created successfully!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html')

# Route for viewing posts
@main.route('/posts')
def view_posts():
    # Logic to retrieve posts
    return render_template('view_posts.html')

# Login route
@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('main.home'))

        flash('Invalid email or password.', 'danger')

    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('main.home'))

# Search functionality
@main.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    # Logic for searching posts
    return render_template('search_results.html', query=query)
